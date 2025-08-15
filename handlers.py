from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import ADMIN_ID, AGENT_CODE, PHONE, AFF_LINK, FORM_VI, FORM_EN

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🇻🇳 Tiếng Việt", callback_data="vi")],
        [InlineKeyboardButton("🇺🇸 English", callback_data="en")]
    ]
    await update.message.reply_text("Chọn ngôn ngữ / Choose your language:", reply_markup=InlineKeyboardMarkup(keyboard))

# Callback ngôn ngữ
async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = query.data
    if lang == "vi":
        await query.message.reply_text(f"Đăng ký tại đây: {FORM_VI}\nMã đại lý: {AGENT_CODE}\nHotline: {PHONE}\nLink: {AFF_LINK}")
    else:
        await query.message.reply_text(f"Register here: {FORM_EN}\nAgent Code: {AGENT_CODE}\nHotline: {PHONE}\nLink: {AFF_LINK}")

# /info
async def register_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Website: {AFF_LINK}\nAgent Code: {AGENT_CODE}\nHotline: {PHONE}")

# /keosu
async def vpn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kèo sư: https://keosu.com")
    await context.bot.forward_message(chat_id=ADMIN_ID, from_chat_id=update.effective_chat.id, message_id=update.message.message_id)

# /spin
user_spins = {}

async def spin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_spins.get(user_id):
        await update.message.reply_text("Bạn đã quay rồi!")
    else:
        import random
        prize = random.choice(["🎁 100k", "🎉 50k", "😢 Không trúng"])
        user_spins[user_id] = prize
        await update.message.reply_text(f"Kết quả quay: {prize}")
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"User {user_id} quay được: {prize}")

# /leaderboard
async def leaderboard_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "\n".join([f"{uid}: {prize}" for uid, prize in user_spins.items()])
    await update.message.reply_text(f"Bảng xếp hạng:\n{text}")

# /dashboard
async def dashboard_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    total_users = len(user_spins)
    await update.message.reply_text(f"Tổng số người đã quay: {total_users}")

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Các lệnh có sẵn: /start /spin /leaderboard /info /keosu")

# /admin
async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        await update.message.reply_text("Chào admin!")
    else:
        await update.message.reply_text("Bạn không phải admin.")

# Tin nhắn tự do
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.forward_message(chat_id=ADMIN_ID, from_chat_id=update.effective_chat.id, message_id=update.message.message_id)

# odds_command (placeholder)
async def odds_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tỷ lệ quay: 50% trúng, 50% không trúng.")
