import os
import logging
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)
from handlers import start, handle_message
from config import BOT_TOKEN, WEBHOOK_URL

# 🔧 Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 🚀 Khởi tạo bot Telegram
application = ApplicationBuilder().token(BOT_TOKEN).build()

# 🧩 Đăng ký các handler
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# ▶️ Chạy bot bằng webhook
if __name__ == "__main__":
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        webhook_url=WEBHOOK_URL
    )
