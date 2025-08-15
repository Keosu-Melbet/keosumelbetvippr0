from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import *
from utils import load_data, save_data, search_google
from responses import responses
import random, logging
from datetime import datetime

logger = logging.getLogger(__name__)
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
        await application.bot.set_my_commands(command_descriptions[lang])
        logger.info(f"Bot commands set for user {user_id}, lang: {lang}")
    except Exception as e:
        logger.error(f"Error setting bot commands: {e}")
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
        responses[lang]["hi"].format(coins=0),
        parse_mode='Markdown', reply_markup=reply_markup
    )

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
        responses[lang]["hi"].format(coins=0),
        parse_mode='Markdown'
    )
    await set_bot_commands(user_id, context.application)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.lower()
    data = load_data()
    lang = data.get(str(user_id), {}).get("lang", "vi")
    user_data = data.get(str(user_id), {})
    coins = user_data.get("coins", 0)

    if any(keyword in text for keyword in ["how", "hướng dẫn", "comment", "cara"]):
        reply = responses[lang]["how to play"].format(coins=coins)
    elif text in ["help", "/help"]:
        reply = responses[lang]["help"].format(coins=coins)
    else:
        reply = responses[lang].get(text, responses[lang]["default"].format(coins=coins))

    await update.message.reply_text(reply, parse_mode='Markdown', disable_web_page_preview=True)
def format_response(key: str, user_data: dict) -> str:
    lang = user_data.get("lang", "en")
    response = get_response(lang, key)
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
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = get_user_data(update)
    text = format_response("help", user_data)
    await update.message.reply_text(text, parse_mode="Markdown")

async def vpn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = get_user_data(update)
    text = format_response("vpn", user_data)
    await update.message.reply_text(text, parse_mode="Markdown")

async def leaderboard_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = get_user_data(update)
    text = format_response("leaderboard", user_data)
    await update.message.reply_text(text, parse_mode="Markdown")
async def spin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = get_user_data(update)
    result = random.choice(["🍒", "🍋", "🔔", "💎", "💰", "💀"])
    coins_earned = random.randint(0, 50)
    user_data["coins"] = user_data.get("coins", 0) + coins_earned
    update_user_data(update, user_data)

    if coins_earned > 0:
        text = get_response(user_data["lang"], "spin_win").format(
            result=result,
            coins_earned=coins_earned,
            total_coins=user_data["coins"],
            AFF_LINK=get_affiliate_link(),
            PROMO_CODE=get_promo_code(),
            FORM_LINK_EN=get_form_link("en"),
        )
    else:
        text = get_response(user_data["lang"], "spin_lose").format(
            result=result,
            AFF_LINK=get_affiliate_link(),
            PROMO_CODE=get_promo_code(),
            FORM_LINK_EN=get_form_link("en"),
        )

    await update.message.reply_text(text, parse_mode="Markdown")

async def register_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = get_user_data(update)
    already_registered = user_data.get("registered", False)

    if already_registered:
        key = "register_exists"
    else:
        key = "register_new"
        user_data["registered"] = True
        update_user_data(update, user_data)

    text = get_response(user_data["lang"], key).format(
        AFF_LINK=get_affiliate_link(),
        PROMO_CODE=get_promo_code(),
        FORM_LINK_EN=get_form_link("en"),
        coins=user_data.get("coins", 0),
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def odds_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = get_user_data(update)
    text = format_response("hi", user_data)
    await update.message.reply_text(text, parse_mode="Markdown")

