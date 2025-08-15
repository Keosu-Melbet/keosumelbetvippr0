from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import ADMIN_ID, AFFILIATE_CODE, HOTLINE, AFFILIATE_LINK

user_spin_status = {}

def get_language(update: Update):
    return update.effective_user.language_code or "vi"

def translate(texts: dict, lang: str):
    return texts.get(lang, texts["vi"])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_language(update)
    text = translate({
        "vi": "👋 Chào mừng đến với sòng bạc Kèo Sư! Gõ /spin để quay số, biết đâu hôm nay bạn thành đại gia 💸",
        "en": "👋 Welcome to KeoSu Casino! Type /spin to try your luck and maybe become a millionaire 💸"
    }, lang)
    await update.message.reply_text(text)

async def spin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = get_language(update)

    if user_spin_status.get(user_id):
        text = translate({
            "vi": "⛔ Hôm nay quay rồi nha, tham quá là bị khóa nick đó 😤",
            "en": "⛔ You've already spun today! Greedy much? 😤"
        }, lang)
    else:
        user_spin_status[user_id] = True
        prize = "🎁 100 xu thần thánh"
        text = translate({
            "vi": f"🎉 Chúc mừng! Bạn vừa hốt được {prize}. Đi nhậu được rồi đó!",
            "en": f"🎉 Congrats! You just won {prize}. Time to party!"
        }, lang)
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"🔥 User {user_id} spun and won: {prize}")

    await update.message.reply_text(text)

async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏆 Bảng vàng Kèo Sư:\n🥇 Long Rồng - 999 xu\n🥈 Bé Na - 888 xu\n🥉 Bạn - 777 xu")

async def dashboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Dashboard của bạn:\n- Số lần quay: 1\n- Tổng xu: 100\n- Độ may mắn: 69%")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📞 Hotline cứu trợ: {HOTLINE}\n🔗 Link kiếm tiền: {AFFILIATE_LINK}\n💬 Mã đại lý: {AFFILIATE_CODE}"
    )

async def keosu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💸 Kèo thơm hôm nay:\n⚽ Real Madrid thắng 3-1, ăn đủ tiền mua iPhone 17 Pro Max!")

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👮‍♂️ Admin Panel: Chỉ dành cho người có mật mã tuyệt mật. Gõ sai là bị hack não!")

async def vpn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔐 Hướng dẫn VPN:\n1. Tải app 'Ẩn Danh Pro'\n2. Nhập mã 'KEOSU2025'\n3. Lướt web như ninja 🥷")

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_language(update)
    text = translate({
        "vi": "📝 Đăng ký ngay tại đây để nhận xu miễn phí: https://form.com/vi",
        "en": "📝 Register now to get free coins: https://form.com/en"
    }, lang)
    await update.message.reply_text(text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 Trợ giúp Kèo Sư:\n"
        "/start - Khởi động cuộc chơi\n"
        "/spin - Quay số thần tài\n"
        "/leaderboard - Bảng vàng đại gia\n"
        "/dashboard - Thống kê cá nhân\n"
        "/info - Thông tin đại lý\n"
        "/keosu - Kèo thơm hôm nay\n"
        "/admin - Panel tuyệt mật\n"
        "/vpn - Hướng dẫn lướt web an toàn\n"
        "/register - Đăng ký nhận thưởng\n"
        "/odds - Tỷ lệ cược hôm nay"
    )

async def odds(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📈 Tỷ lệ cược hôm nay:\nLiverpool vs MU: 2.0 - 3.3 - 3.8\nĐặt kèo đi, đừng chần chừ!")

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"📩 Tin nhắn từ {update.effective_user.id}:\n{update.message.text}")
        await update.message.reply_text("✅ Tin nhắn đã được gửi đến Kèo Sư. Ngồi đợi hồi âm như đợi crush rep tin nhắn 😎")
