from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import ADMIN_IDS

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🇻🇳 Tiếng Việt", callback_data="lang_vi")],
        [InlineKeyboardButton("🇺🇸 English", callback_data="lang_en")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🌐 Vui lòng chọn ngôn ngữ:", reply_markup=reply_markup)

# Callback khi chọn ngôn ngữ
async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "lang_vi":
        await query.edit_message_text("✅ Bạn đã chọn Tiếng Việt.\n📝 Vui lòng gửi thông tin đăng ký theo mẫu:\nHọ tên:\nEmail:\nSở thích:")
    elif query.data == "lang_en":
        await query.edit_message_text("✅ You selected English.\n📝 Please send your registration info:\nName:\nEmail:\nInterests:")
    else:
        await query.edit_message_text("❌ Ngôn ngữ không hợp lệ.")

# /spin
async def spin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎰 Bạn vừa quay spin!")

# /register
async def register_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 Bạn đã được đăng ký!")

# /vpn
async def vpn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔐 Hướng dẫn VPN sẽ được gửi cho bạn.")

# /leaderboard
async def leaderboard_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏆 Bảng xếp hạng hiện chưa có dữ liệu.")

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📖 Các lệnh hỗ trợ: /start /spin /register /vpn /leaderboard /admin /dashboard")

# /odds
async def odds_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Tỷ lệ cược hiện tại là 50/50.")

# /dashboard
async def dashboard_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ Bạn không có quyền truy cập dashboard.")
        return
    await update.message.reply_text("📈 Dashboard: 10 người dùng, 25 lượt spin.")

# /admin
async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ Bạn không có quyền truy cập lệnh này.")
        return
    await update.message.reply_text("✅ Chào admin! Bạn có thể quản lý bot tại đây.")

# Tin nhắn thường
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot không hiểu lệnh này. Vui lòng dùng /help.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot đã hoạt động!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Bạn vừa gửi: {update.message.text}")
