from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import *
from utils import (
    load_data, save_data,
    get_affiliate_link, get_promo_code, get_form_link,
    get_web_link, get_phone, get_email, get_api_key,
    get_leaderboard_text
)
from responses import responses
import random, logging

logger = logging.getLogger(__name__)

# 🧠 Lấy dữ liệu người dùng
def get_user_data(update: Update):
    user_id = update.effective_user.id
    data = load_data()
    return data.get(str(user_id), {"lang": "vi", "coins": 0})

# 💾 Cập nhật dữ liệu người dùng
def update_user_data(update: Update, user_data: dict):
    user_id = update.effective_user.id
    data = load_data()
    data[str(user_id)] = user_data
    save_data(data)

# 🗣️ Lấy phản hồi theo ngôn ngữ
def get_response(lang, key):
    return responses.get(lang, responses["vi"]).get(key, "...")

# 🧩 Format nội dung phản hồi
def format_response(key: str, user_data: dict) -> str:
    response = get_response(user_data.get("lang", "vi"), key)
    return response.format(
        AFF_LINK=get_affiliate_link(),
        PROMO_CODE=get_promo_code(),
        FORM_LINK_EN=get_form_link("en"),
        WEB_LINK=get_web_link(),
        PHONE=get_phone(),
        EMAIL=get_email(),
        API_KEY=get_api_key(),
        coins=user_data.get("coins", 0),
        leaderboard_text=get_leaderboard_text(),
    )

# 📋 Cập nhật lệnh bot theo ngôn ngữ
async def set_bot_commands(user_id: int, application):
    data = load_data()
    lang = data.get(str(user_id), {}).get("lang", "vi")
    command_descriptions = {
        "vi": [
            ('start', 'Chọn ngôn ngữ 🌐'),
            ('spin', 'Quay thưởng 💰'),
            ('register', 'Đăng ký 📝'),
            ('vpn', 'Hướng dẫn VPN 🔒'),
            ('leaderboard', 'Bảng xếp hạng 🏆'),
            ('odds', 'Xem kèo ⚽'),
            ('help', 'Trợ giúp ❓')
        ],
        "en": [
            ('start', 'Pick language 🌐'),
            ('spin', 'Spin for Coins 💰'),
            ('register', 'Register 📝'),
            ('vpn', 'VPN guide 🔒'),
            ('leaderboard', 'Rankings 🏆'),
            ('odds', 'Get odds ⚽'),
            ('help', 'Help ❓')
        ]
    }
    try:
        await application.bot.set_my_commands(command_descriptions.get(lang, command_descriptions["vi"]))
        logger.info(f"Bot commands set for user {user_id}, lang: {lang}")
    except Exception as e:
        logger.error(f"Error setting bot commands: {e}")

# 🚀 /start – Chọn ngôn ngữ
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    data = load_data()
    lang = data.get(str(user_id), {}).get("lang", "vi")
    await set_bot_commands(user_id, context.application)

    keyboard = [
        [InlineKeyboardButton("🇻🇳 Tiếng Việt ✨", callback_data="vi"),
         InlineKeyboardButton("🇬🇧 English ✨", callback_data="en")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        get_response(lang, "hi").format(coins=0),
        parse_mode='Markdown', reply_markup=reply_markup
    )

# 🌐 Callback chọn ngôn ngữ
async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = query.data
    data = load_data()
    data[str(user_id)] = data.get(str(user_id), {"lang": "vi", "coins": 0})
    data[str(user_id)]["lang"] = lang
    save_data(data)
    await query.message.edit_text(
        get_response(lang, "hi").format(coins=0),
        parse_mode='Markdown'
    )
    await set_bot_commands(user_id, context.application)

# 💬 Xử lý tin nhắn văn bản
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.lower()
    data = load_data()
    lang = data.get(str(user_id), {}).get("lang", "vi")
    user_data = data.get(str(user_id), {})
    coins = user_data.get("coins", 0)

    if any(keyword in text for keyword in ["how", "hướng dẫn", "comment", "cara"]):
        reply = get_response(lang, "how to play").format(coins=coins)
    elif text in ["help", "/help"]:
        reply = get_response(lang, "help").format(coins=coins)
    else:
        reply = get_response(lang, text) or get_response(lang, "default").format(coins=coins)

    await update.message.reply_text(reply, parse_mode='Markdown', disable_web_page_preview=True)

# ❓ /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = get_user_data(update)
    text = format_response("help", user_data)
    await update.message.reply_text(text, parse_mode="Markdown")

# 🔒 /vpn
async def vpn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = get_user_data(update)
    text = format_response("vpn", user_data)
    await update.message.reply_text(text, parse_mode="Markdown")

# 🏆 /leaderboard
async def leaderboard_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = get_user_data(update)
    text = format_response("leaderboard", user_data)
    await update.message.reply_text(text, parse_mode="Markdown")

# 🎰 /spin
async def spin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = get_user_data(update)
    result = random.choice(["🍒", "🍋", "🔔", "💎", "💰", "💀"])
    coins_earned = random.randint(0, 50)
    user_data["coins"] += coins_earned
    update_user_data(update, user_data)

    key = "spin_win" if coins_earned > 0 else "spin_lose"
    text = get_response(user_data["lang"], key).format(
        result=result,
        coins_earned=coins_earned,
        total_coins=user_data["coins"],
        AFF_LINK=get_affiliate_link(),
        PROMO_CODE=get_promo_code(),
        FORM_LINK_EN=get_form_link("en"),
    )
    await update.message.reply_text(text, parse_mode="Markdown")

# 📝 /register
async def register_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = get_user_data(update)
    key = "register_exists" if user_data.get("registered") else "register_new"
    user_data["registered"] = True
    update_user_data(update, user_data)

    text = get_response(user_data["lang"], key).format(
        AFF_LINK=get_affiliate_link(),
        PROMO_CODE=get_promo_code(),
        FORM_LINK_EN=get_form_link("en"),
        coins=user_data.get("coins", 0),
    )
    await update.message.reply_text(text, parse_mode="Markdown")

# ⚽ /odds
async def odds_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = get_user_data(update)
    text = format_response("hi", user_data)
    await update.message.reply_text(text, parse_mode="Markdown")
