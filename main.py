from flask import Flask
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import BOT_TOKEN
from handlers import (
    start, language_callback, spin_wheel, register, vpn,
    leaderboard, help_command, odds, handle_message
)

application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(language_callback, pattern="^(vi|en|fr|th|id)$"))
application.add_handler(CommandHandler("spin", spin_wheel))
application.add_handler(CommandHandler("register", register))
application.add_handler(CommandHandler("vpn", vpn))
application.add_handler(CommandHandler("leaderboard", leaderboard))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("odds", odds))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    import asyncio, nest_asyncio, logging
    nest_asyncio.apply()
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(application.run_polling(drop_pending_updates=True))
