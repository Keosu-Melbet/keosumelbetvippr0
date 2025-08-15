from telegram.ext import ApplicationBuilder, CommandHandler
from ghandlers import (
    help_command,
    vpn_command,
    leaderboard_command,
    spin_command,
    register_command,
    odds_command,
)

def setup_handlers(app):
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("vpn", vpn_command))
    app.add_handler(CommandHandler("leaderboard", leaderboard_command))
    app.add_handler(CommandHandler("spin", spin_command))
    app.add_handler(CommandHandler("register", register_command))
    app.add_handler(CommandHandler("odds", odds_command))
