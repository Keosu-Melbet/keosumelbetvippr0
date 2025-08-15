import os
import json
import random
import logging
import requests
import re
from datetime import datetime
import pytz
import asyncio
from flask import Flask
import threading

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes
)

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Biến môi trường
BOT_TOKEN = os.environ.get("BOT_TOKEN")
AFF_LINK = os.environ.get("AFF_LINK")
FORM_LINK_EN = os.environ.get("FORM_LINK_EN")
FORM_LINK_VN = os.environ.get("FORM_LINK_VN")
WEB_LINK = os.environ.get("WEB_LINK")
PROMO_CODE = os.environ.get("PROMO_CODE")
PHONE = os.environ.get("PHONE")
EMAIL = os.environ.get("EMAIL")
API_KEY = os.environ.get("API_KEY")
SEARCH_ENGINE_ID = os.environ.get("SEARCH_ENGINE_ID")

# Múi giờ
TZ = pytz.timezone('Asia/Ho_Chi_Minh')
DATA_FILE = "users.json"
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Lỗi load data: {e}")
        return {}

def save_data(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        logger.error(f"Lỗi save data: {e}")
def get_daily_characters():
    GAME_CHARACTERS = {
        "day1": ["Messi", "Ronaldo", "Neymar", "Mbappe", "De Bruyne"],
        "day2": ["Haaland", "Lewandowski", "Benzema", "Kane", "Salah"],
        "day3": ["Modric", "Ramos", "Beckham", "Zidane", "Henry"],
        "day4": ["Ronaldinho", "Pele", "Maradona", "Cruyff", "Beckenbauer"],
        "day5": ["Bale", "Pogba", "Hazard", "Griezmann", "Mane"]
    }
    day_index = (datetime.now(TZ) - datetime(2025, 8, 3, tzinfo=TZ)).days % 5 + 1
    return GAME_CHARACTERS.get(f"day{day_index}", GAME_CHARACTERS["day1"])

responses = {
    "vi": {
        "hi": f"*Chào cược thủ! 🎉*\n👉 Đặt kèo tại: [{AFF_LINK}]({AFF_LINK}) với mã [{PROMO_CODE}]\n📞 {PHONE} | ✉️ {EMAIL}",
        "help": f"*Trợ giúp! 🚀*\n- /start: Chọn ngôn ngữ\n- /spin: Quay thưởng\n- /register: Đăng ký\n- /vpn: VPN\n- /leaderboard: BXH\n- /odds: Xem kèo",
        "default": "*Kèo sư hơi mệt! 😅*\nGõ /help để xem chức năng nha!",
        "register_new": f"*Đăng ký thành công! 🎉*\n👉 [{FORM_LINK_VN}]({FORM_LINK_VN})",
        "register_exists": f"*Bạn đã đăng ký rồi! 😄*\n👉 [{FORM_LINK_VN}]({FORM_LINK_VN})",
        "spin_result": f"*Quay thưởng! 🎰*\nKết quả: {{result}}",
        "spin_win": f"*Bạn nhận được: {{result}} + {{coins_earned}} Coins* 💰",
        "spin_lose": f"*Không trúng rồi 😅*\nThử lại nha!",
        "vpn": f"*VPN hướng dẫn:*\n1. Tải NordVPN\n2. Chọn server gần\n3. Truy cập [{AFF_LINK}]({AFF_LINK})",
        "leaderboard": "*🏆 Bảng xếp hạng 🏆*\n{{leaderboard_text}}",
        "how to play": f"*Hướng dẫn chơi:*\nQuay /spin, xem /odds, đăng ký tại [{FORM_LINK_VN}]({FORM_LINK_VN})"
    }
}
async def set_bot_commands(user_id: int):
    await application.bot.set_my_commands([
        ('start', 'Chọn ngôn ngữ'),
        ('spin', 'Quay thưởng'),
        ('register', 'Đăng ký'),
        ('vpn', 'VPN'),
        ('leaderboard', 'BXH'),
        ('odds', 'Xem kèo'),
        ('help', 'Trợ giúp')
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    await set_bot_commands(user_id)
    keyboard = [[InlineKeyboardButton("🇻🇳 Tiếng Việt", callback_data="vi")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(responses["vi"]["hi"], parse_mode='Markdown', reply_markup=reply_markup)

async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = query.data
    data = load_data()
    data[str(user_id)] = {"lang": lang, "coins": 0}
    save_data(data)
    await query.message.edit_text(responses[lang]["hi"], parse_mode='Markdown')
    await set_bot_commands(user_id)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.lower()
    data = load_data()
    lang = data.get(str(user_id), {}).get("lang", "vi")
    reply = responses[lang].get(text, responses[lang]["default"])
    await update.message.reply_text(reply, parse_mode='Markdown')

async def spin_wheel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    prizes = ["100 Coins", "500 Coins", "Không trúng 😅"]
    result = random.choice(prizes)
    data = load_data()
    lang = data.get(str(user_id), {}).get("lang", "vi")
    coins = data.get(str(user_id), {}).get("coins", 0)
    await update.message.reply_text(responses[lang]["spin_result"].format(result=result), parse_mode='Markdown')
    if "Coins" in result:
        coins_earned = int(result.split()[0])
        total = coins + coins_earned
        data[str(user_id)]["coins"] = total
        save_data(data)
        await update.message.reply_text(responses[lang]["spin_win"].format(result=result, coins_earned=coins_earned), parse_mode='Markdown')
    else:
        await update.message.reply_text(responses[lang]["spin_lose"].format(result=result), parse_mode='Markdown')

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    data = load_data()
    lang = data.get(str(user_id), {}).get("lang", "vi")
    if str(user_id) not in data:
        data[str(user_id)] = {"lang": lang, "coins": 0}
        save_data(data)
        await update.message.reply_text(responses[lang]["register_new"], parse_mode='Markdown')
    else:
        await update.message.reply_text(responses[lang]["register_exists"], parse_mode='Markdown')

async def vpn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    lang = load_data().get(str(user_id), {}).get("lang", "vi")
    await update.message.reply_text(responses[lang]["vpn"], parse_mode='Markdown')

async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    lang = load_data().get(str(user_id), {}).get("lang", "vi")
    leaderboard_text = ""
    for i, name in enumerate(get_daily_characters(), 1):
        leaderboard_text += f"{i}. *{name}*: {random.randint(1000, 5000)} Coins\n"
    await update.message.reply_text(responses[lang]["leaderboard"].format(leaderboard_text=leaderboard_text), parse_mode='Markdown')

application = Application.builder

async def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Đăng ký các handler
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("spin", spin_wheel))
    application.add_handler(CommandHandler("register", register))
    application.add_handler(CommandHandler("vpn", vpn))
    application.add_handler(CommandHandler("leaderboard", leaderboard))
    application.add_handler(CommandHandler("help", handle_message))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(language_callback))

    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
