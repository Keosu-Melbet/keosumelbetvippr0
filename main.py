import os
import logging
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)
from handlers import (
    start, handle_message, language_callback,
    spin_command, register_command, vpn_command,
    leaderboard_command, help_command, odds_command,
    dashboard_command, admin_command
)
from config import BOT_TOKEN, WEBHOOK_URL

# 🔧 Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# 🚀 Khởi tạo bot Telegram
application = ApplicationBuilder().token(BOT_TOKEN).build()

# 🧩 Đăng ký các handler
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("spin", spin_command))
application.add_handler(CommandHandler("register", register_command))
application.add_handler(CommandHandler("vpn", vpn_command))
application.add_handler(CommandHandler("leaderboard", leaderboard_command))
application.add_handler(CommandHandler("odds", odds_command))
application.add_handler(CommandHandler("dashboard", dashboard_command))
application.add_handler(CommandHandler("admin", admin_command))
application.add_handler(CallbackQueryHandler(language_callback))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# ▶️ Chạy bot bằng webhook
if __name__ == "__main__":
   application.run_webhook(
    listen="0.0.0.0",
    port=int(os.getenv("PORT", 5000)),
    webhook_url=WEBHOOK_URL,
    webhook_path="/webhook"
)
