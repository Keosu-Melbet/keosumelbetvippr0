import logging
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, filters
)
from handlers import (
    start, language_callback, spin_command, register_command,
    vpn_command, leaderboard_command, help_command,
    odds_command, handle_message
)
from config import BOT_TOKEN

# 🔧 Cấu hình logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 🚀 Khởi tạo bot
def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # 🧩 Đăng ký các handler
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("spin", spin_command))
    application.add_handler(CommandHandler("register", register_command))
    application.add_handler(CommandHandler("vpn", vpn_command))
    application.add_handler(CommandHandler("leaderboard", leaderboard_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("odds", odds_command))
    application.add_handler(CallbackQueryHandler(language_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # ▶️ Chạy bot
    application.run_polling()

if __name__ == "__main__":
    main()
