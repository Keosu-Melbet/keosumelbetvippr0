import os
import logging
from flask import Flask, request
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)
from handlers import (
    start, language_callback, spin_command, register_command,
    vpn_command, leaderboard_command, help_command,
    odds_command, dashboard_command, admin_command,
    handle_message
)
from config import BOT_TOKEN, ADMIN_IDS

# 🔧 Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 🌐 Flask app
app = Flask(__name__)

# 🚀 Khởi tạo bot
application = ApplicationBuilder().token(BOT_TOKEN).build()

# 🧩 Đăng ký các handler
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("spin", spin_command))
application.add_handler(CommandHandler("register", register_command))
application.add_handler(CommandHandler("vpn", vpn_command))
application.add_handler(CommandHandler("leaderboard", leaderboard_command))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("odds", odds_command))
application.add_handler(CommandHandler("dashboard", dashboard_command))
application.add_handler(CommandHandler("admin", admin_command))
application.add_handler(CallbackQueryHandler(language_callback))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# 📥 Nhận update từ Telegram
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put(update)
    return "ok"

# 🏠 Trang chủ đơn giản
@app.route("/")
def home():
    return "Bot is running via webhook!"

# 🔁 Route ping để giữ bot online
@app.route("/ping")
def ping():
    return "pong"

# ▶️ Khởi động Flask và set webhook
if __name__ == "__main__":
    WEBHOOK_URL = f"https://{os.environ['RENDER_EXTERNAL_URL']}/webhook"
    application.bot.set_webhook(WEBHOOK_URL)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
