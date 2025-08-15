from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_ID, AGENT_CODE, HOTLINE, AFFILIATE_LINK
from database import register_user, can_spin_today, update_spin, get_user_stats, get_leaderboard

def get_language(update: Update):
    return update.effective_user.language_code or "vi"

def translate(texts: dict, lang: str):
    return texts.get(lang, texts["vi"])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_language(update)
    await register_user(update.effective_user.id, update.effective_user.username)
    text = translate({
        "vi": "👋 Chào mừng đến với sòng bạc Kèo Sư! Gõ /spin để quay số, biết đâu hôm nay bạn thành đại gia 💸",
        "en": "👋 Welcome to KeoSu Casino! Type /spin to try your luck and maybe become a millionaire 💸"
    }, lang)
    await update.message.reply_text(text)

async def spin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await register_user(user.id, user.username)

    if not await can_spin_today(user.id):
        await update.message.reply_text("⛔ Hôm nay quay rồi nha, mai quay tiếp nhé!")
        return

    prize = 100
    await update_spin(user.id, prize)
    await update.message.reply_text(f"🎉 Bạn vừa hốt được {prize} xu! Quá đỉnh 😎")
    await context.bot.send_message(chat_id=ADMIN_ID, text=f"🔥 {user.username} ({user.id}) quay trúng {prize} xu")

async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    top = await get_leaderboard()
    msg = "🏆 Bảng vàng Kèo Sư:\n"
    for i, (username, coins) in enumerate(top, start=1):
        name = username or f"User{i}"
        msg += f"{i}. {name} - {coins} xu\n"
    await update.message.reply_text(msg)

async def dashboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stats = await get_user_stats(update.effective_user.id)
    if stats:
        spins, coins = stats
        await update.message.reply_text(f"📊 Dashboard:\n- Số lần quay: {spins}\n- Tổng xu: {coins}")
    else:
        await update.message.reply_text("📊 Bạn chưa quay lần nào. Gõ /spin để thử vận may!")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📞 Hotline cứu trợ: {HOTLINE}\n🔗 Link kiếm tiền: {AFFILIATE_LINK}\n💬 Mã đại lý: {AGENT_CODE}"
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
