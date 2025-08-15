import logging
import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN, WEBHOOK_URL, PORT
import handlers
from database import init_db

# Cấu hình logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def main():
    # Khởi tạo database
    await init_db()

    # Tạo ứng dụng bot
    app = Application.builder().token(BOT_TOKEN).build()

    # Đăng ký các lệnh
    app.add_handler(CommandHandler("start", handlers.start))
    app.add_handler(CommandHandler("spin", handlers.spin))
    app.add_handler(CommandHandler("leaderboard", handlers.leaderboard))
    app.add_handler(CommandHandler("dashboard", handlers.dashboard))
    app.add_handler(CommandHandler("info", handlers.info))
    app.add_handler(CommandHandler("keosu", handlers.keosu))
    app.add_handler(CommandHandler("admin", handlers.admin))
    app.add_handler(CommandHandler("vpn", handlers.vpn))
    app.add_handler(CommandHandler("register", handlers.register))
    app.add_handler(CommandHandler("help", handlers.help_command))
    app.add_handler(CommandHandler("odds", handlers.odds))

    # Tin nhắn tự do gửi về admin
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.forward_to_admin))

    # Chạy webhook
    await app.run_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        webhook_url=WEBHOOK_URL
    )

if __name__ == "__main__":
    asyncio.run(main())
