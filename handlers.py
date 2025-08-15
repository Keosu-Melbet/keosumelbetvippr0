from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_IDS

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Xin chào! Bot đang hoạt động.")

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

# Callback (nếu có)
async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("Ngôn ngữ đã được chọn.")

# Tin nhắn thường
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot không hiểu lệnh này.")
