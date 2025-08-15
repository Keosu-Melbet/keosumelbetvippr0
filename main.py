import os
import logging
from flask import Flask, request
from telegram import Update
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

# 🌐 Flask app
app = Flask(__name__)

# 🚀 Khởi tạo bot Telegram
application = ApplicationBuilder().token(BOT_TOKEN).build()

# 🧩 Đăng ký các handler
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# 📥 Route nhận update từ Telegram
@app.route("/webhook", methods=["POST"])
def webhook():
    json_data = request.get_json(force=True)
    logging.info(f"Received update: {json_data}")
    update = Update.de_json(json_data, application.bot)
    application.update_queue.put(update)
    return "ok"

# 🏠 Route trang chủ
@app.route("/")
def home():
    return "Bot is running via webhook!"

# 🔁 Route ping để giữ bot online
@app.route("/ping")
def ping():
    return "pong"

@app.route("/webhook", methods=["POST"])
def webhook():
    json_data = request.get_json(force=True)
    logging.info(f"📩 Received update: {json_data}")
    update = Update.de_json(json_data, application.bot)
    application.update_queue.put(update)
    return "ok"


# ▶️ Khởi động Flask và đăng ký webhook
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Đăng ký webhook với Telegram
    application.bot.set_webhook(WEBHOOK_URL)
    app.run(host="0.0.0.0", port=port)
