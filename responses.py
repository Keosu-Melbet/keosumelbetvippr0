from config import AFF_LINK, FORM_LINK_EN, FORM_LINK_VN, WEB_LINK, PROMO_CODE, PHONE, EMAIL, API_KEY

responses = {
    "vi": {
        "hi": f"*Chào cược thủ! 🎉*\nCó kèo ngon không anh em? Gõ /odds để xem tip hot nha! 😎🎯\n👉 Đặt kèo tại: [{AFF_LINK}]({AFF_LINK}) với mã [{PROMO_CODE}]\n📞 Liên hệ: {PHONE} | ✉️ {EMAIL}\n💰 Coins: {{coins}} | 🔑 Key: {API_KEY[:10]}...\n📝 Đăng ký: [{FORM_LINK_VN}]({FORM_LINK_VN})",
        "help": f"*Kèo sư cứu trợ! 🚀*\n- /start: Chọn ngôn ngữ\n- /spin: Quay thưởng kiếm Coins\n- /register: Đăng ký\n- /vpn: Hướng dẫn VPN\n- /leaderboard: Bảng xếp hạng\n- /odds: Xem kèo\n👉 Đăng ký: [{FORM_LINK_VN}]({FORM_LINK_VN}) | 🔗 {WEB_LINK}\n📞 {PHONE} | ✉️ {EMAIL}",
        "how to play": f"*Hướng dẫn cược thủ! ⚽*\nQuay /spin lấy Coins, dùng /odds xem tip kèo, đăng ký qua: [{FORM_LINK_VN}]({FORM_LINK_VN}). Rủ anh em chơi lớn nha! 💰\n👉 Đặt kèo: [{AFF_LINK}]({AFF_LINK}) với mã [{PROMO_CODE}]",
        "default": "*Kèo sư hơi mệt! 😅*\nGõ /help hoặc hỏi kèo gì ngon đi anh em, mình dẫn đường liền! 🚀\n📞 {PHONE} | ✉️ {EMAIL}",
        "register_new": f"*Đăng ký thành công rùi đó, cược thủ! 🎉*\nVui lòng điền form tại: [{FORM_LINK_VN}]({FORM_LINK_VN}) để Kèo Sư kiểm soát và nhận thưởng nhé! 😄\n👉 Đặt kèo: [{AFF_LINK}]({AFF_LINK}) với mã [{PROMO_CODE}]\n💰 Coins: {{coins}}",
        "register_exists": f"*Anh em đã đăng ký rồi nha, cược thủ! 😄*\nVui lòng kiểm tra lại form tại: [{FORM_LINK_VN}]({FORM_LINK_VN}) để Kèo Sư quản lý và nhận thưởng nhé!\n👉 Đặt kèo: [{AFF_LINK}]({AFF_LINK}) với mã [{PROMO_CODE}]\n💰 Coins: {{coins}}",
        "spin_result": f"*Kèo sư quay thưởng đây! 🎰*\nKết quả: {{result}}\n👉 Đặt kèo: [{AFF_LINK}]({AFF_LINK}) với mã [{PROMO_CODE}]",
        "spin_win": f"*Chúc mừng nha, cược thủ! 🎉*\nBạn nhận được: {{result}} + {{coins_earned}} Coins\nTổng Coins: {{total_coins}} 💰\n👉 Đăng ký: [{FORM_LINK_VN}]({FORM_LINK_VN}) | Đặt kèo: [{AFF_LINK}]({AFF_LINK})!",
        "spin_lose": f"*Tiếc quá anh em! 😅*\nKết quả: {{result}}, thử lại vận may nha! 🎲\n👉 Đăng ký: [{FORM_LINK_VN}]({FORM_LINK_VN}) | Đặt kèo: [{AFF_LINK}]({AFF_LINK})!",
        "vpn": f"*Hướng dẫn cược thủ! ⚽*\n1. Tải NordVPN hoặc ExpressVPN.\n2. Chọn server gần nhất.\n3. Vào [{AFF_LINK}]({AFF_LINK}) cược kèo ngon lành! 😎\n📞 {PHONE} | ✉️ {EMAIL}\n👉 Đăng ký: [{FORM_LINK_VN}]({FORM_LINK_VN})",
        "leaderboard": f"*🏆 Bảng xếp hạng cược thủ 🏆*\n{{leaderboard_text}}\n👉 Đặt kèo: [{AFF_LINK}]({AFF_LINK}) với mã [{PROMO_CODE}]"
    },
    "en": {
        "hi": f"*Hey oddster! 🎉*\nGot hot odds? Check /odds for the latest! 😎🎯\n👉 Bet at: [{AFF_LINK}]({AFF_LINK}) with code [{PROMO_CODE}]\n📞 Contact: {PHONE} | ✉️ {EMAIL}\n💰 Coins: {{coins}} | 🔑 Key: {API_KEY[:10]}...\n📝 Register: [{FORM_LINK_EN}]({FORM_LINK_EN})",
        "help": f"*Odds master to the rescue! 🚀*\n- /start: Pick language\n- /spin: Spin for Coins\n- /register: Register\n- /vpn: VPN guide\n- /leaderboard: Rankings\n- /odds: Get odds\n👉 Register: [{FORM_LINK_EN}]({FORM_LINK_EN}) | 🔗 {WEB_LINK}\n📞 {PHONE} | ✉️ {EMAIL}",
        "how to play": f"*Guide for oddsters! ⚽*\nSpin with /spin to earn Coins, check /odds for tips, register here: [{FORM_LINK_EN}]({FORM_LINK_EN}). Go big with your crew! 💰\n👉 Bet: [{AFF_LINK}]({AFF_LINK}) with code [{PROMO_CODE}]",
        "default": "*Odds master is tired! 😅*\nType /help or ask for hot odds, I’ll guide you, bro! 🚀\n📞 {PHONE} | ✉️ {EMAIL}",
        "register_new": f"*Registration successful, oddster! 🎉*\nPlease fill out the form at: [{FORM_LINK_EN}]({FORM_LINK_EN}) for Odds Master to track and reward you! 😄\n👉 Bet: [{AFF_LINK}]({AFF_LINK}) with code [{PROMO_CODE}]\n💰 Coins: {{coins}}",
        "register_exists": f"*You’re already registered, oddster! 😄*\nPlease check the form again at: [{FORM_LINK_EN}]({FORM_LINK_EN}) for Odds Master to manage and reward you!\n👉 Bet: [{AFF_LINK}]({AFF_LINK}) with code [{PROMO_CODE}]\n💰 Coins: {{coins}}",
        "spin_result": f"*Odds master spinning the wheel! 🎰*\nResult: {{result}}\n👉 Bet: [{AFF_LINK}]({AFF_LINK}) with code [{PROMO_CODE}]",
        "spin_win": f"*Congrats, oddster! 🎉*\nYou got: {{result}} + {{coins_earned}} Coins\nTotal Coins: {{total_coins}} 💰\n👉 Register: [{FORM_LINK_EN}]({FORM_LINK_EN}) | Bet: [{AFF_LINK}]({AFF_LINK})!",
        "spin_lose": f"*Tough luck, bro! 😅*\nResult: {{result}}, try your luck again! 🎲\n👉 Register: [{FORM_LINK_EN}]({FORM_LINK_EN}) | Bet: [{AFF_LINK}]({AFF_LINK})!",
        "vpn": f"*Guide for oddsters! ⚽*\n1. Download NordVPN or ExpressVPN.\n2. Connect to the nearest server.\n3. Visit [{AFF_LINK}]({AFF_LINK}) to bet odds like a pro! 😎\n📞 {PHONE} | ✉️ {EMAIL}\n👉 Register: [{FORM_LINK_EN}]({FORM_LINK_EN})",
        "leaderboard": f"*🏆 Oddsters Rankings 🏆*\n{{leaderboard_text}}\n👉 Bet: [{AFF_LINK}]({AFF_LINK}) with code [{PROMO_CODE}]"
    },
    "fr": {
        "hi": f"*Salut parieur ! 🎉*\nDes cotes chaudes ? Vérifie /odds ! 😎🎯\n👉 Parie sur : [{AFF_LINK}]({AFF_LINK}) avec le code [{PROMO_CODE}]\n📞 Contact : {PHONE} | ✉️ {EMAIL}\n💰 Coins : {{coins}} | 🔑 Clé : {API_KEY[:10]}...\n📝 Inscription : [{FORM_LINK_EN}]({FORM_LINK_EN})",
        "help": f"*Maître des cotes à la rescousse ! 🚀*\n- /start : Choisir la langue\n- /spin : Tourne pour des Coins\n- /register : S’inscrire\n- /vpn : Guide VPN\n- /leaderboard : Classement\n- /odds : Voir les cotes\n👉 Inscris-toi : [{FORM_LINK_EN}]({FORM_LINK_EN}) | 🔗 {WEB_LINK}\n📞 {PHONE} | ✉️ {EMAIL}",
        "how to play": f"*Guide pour les parieurs ! ⚽*\nTourne avec /spin pour gagner des Coins, vois /odds pour les cotes, inscris-toi ici : [{FORM_LINK_EN}]({FORM_LINK_EN}). Parie gros avec ton équipe ! 💰\n👉 Parie : [{AFF_LINK}]({AFF_LINK}) avec le code [{PROMO_CODE}]",
        "default": "*Le maître des cotes est fatigué ! 😅*\nTape /help ou demande une cote chaude, je te guide ! 🚀\n📞 {PHONE} | ✉️ {EMAIL}",
        "register_new": f"*Inscription réussie, parieur ! 🎉*\nRemplis le formulaire ici : [{FORM_LINK_EN}]({FORM_LINK_EN}) pour que le maître des cotes puisse te récompenser ! 😄\n👉 Parie : [{AFF_LINK}]({AFF_LINK}) avec le code [{PROMO_CODE}]\n💰 Coins : {{coins}}",
        "register_exists": f"*Tu es déjà inscrit, parieur ! 😄*\nVérifie le formulaire ici : [{FORM_LINK_EN}]({FORM_LINK_EN}) pour recevoir ta récompense !\n👉 Parie : [{AFF_LINK}]({AFF_LINK}) avec le code [{PROMO_CODE}]\n💰 Coins : {{coins}}",
        "spin_result": f"*Le maître des cotes fait tourner la roue ! 🎰*\nRésultat : {{result}}\n👉 Parie : [{AFF_LINK}]({AFF_LINK}) avec le code [{PROMO_CODE}]",
        "spin_win": f"*Félicitations, parieur ! 🎉*\nTu as gagné : {{result}} + {{coins_earned}} Coins\nTotal Coins : {{total_coins}} 💰\n👉 Inscris-toi : [{FORM_LINK_EN}]({FORM_LINK_EN}) | Parie : [{AFF_LINK}]({AFF_LINK})",
        "spin_lose": f"*Pas de chance ! 😅*\nRésultat : {{result}}, retente ta chance ! 🎲\n👉 Inscris-toi : [{FORM_LINK_EN}]({FORM_LINK_EN}) | Parie : [{AFF_LINK}]({AFF_LINK})",
        "vpn": f"*Guide VPN pour parieurs ! 🔒*\n1. Télécharge NordVPN ou ExpressVPN\n2. Connecte-toi à un serveur proche\n3. Parie sur [{AFF_LINK}]({AFF_LINK}) comme un pro ! 😎\n📞 {PHONE} | ✉️ {EMAIL}",
        "leaderboard": f"*🏆 Classement des parieurs 🏆*\n{{leaderboard_text}}\n👉 Parie : [{AFF_LINK}]({AFF_LINK}) avec le code [{PROMO_CODE}]"
   },
    "th": {
        "hi": f"*สวัสดีนักพนัน! 🎉*\nมีอัตราต่อรองเด็ด ๆ ไหม? ดูที่ /odds ได้เลย! 😎🎯\n👉 เดิมพันที่: [{AFF_LINK}]({AFF_LINK}) ด้วยรหัส [{PROMO_CODE}]\n📞 ติดต่อ: {PHONE} | ✉️ {EMAIL}\n💰 Coins: {{coins}} | 🔑 Key: {API_KEY[:10]}...\n📝 ลงทะเบียน: [{FORM_LINK_EN}]({FORM_LINK_EN})",
        "help": f"*เจ้าแห่งอัตราต่อรองมาช่วยแล้ว! 🚀*\n- /start: เลือกภาษา\n- /spin: หมุนรับ Coins\n- /register: ลงทะเบียน\n- /vpn: คู่มือ VPN\n- /leaderboard: อันดับ\n- /odds: ดูอัตราต่อรอง\n👉 ลงทะเบียน: [{FORM_LINK_EN}]({FORM_LINK_EN}) | 🔗 {WEB_LINK}\n📞 {PHONE} | ✉️ {EMAIL}",
        "how to play": f"*คู่มือสำหรับนักพนัน! ⚽*\nหมุน /spin เพื่อรับ Coins, ดู /odds เพื่อรับคำแนะนำ, ลงทะเบียนที่นี่: [{FORM_LINK_EN}]({FORM_LINK_EN}) แล้วไปลุยกับเพื่อน ๆ! 💰\n👉 เดิมพัน: [{AFF_LINK}]({AFF_LINK}) ด้วยรหัส [{PROMO_CODE}]",
        "default": "*เจ้าแห่งอัตราต่อรองเหนื่อยแล้ว! 😅*\nพิมพ์ /help หรือถามหาอัตราต่อรองเด็ด ๆ ได้เลย 🚀\n📞 {PHONE} | ✉️ {EMAIL}",
        "register_new": f"*ลงทะเบียนสำเร็จแล้ว! 🎉*\nกรุณากรอกฟอร์มที่: [{FORM_LINK_EN}]({FORM_LINK_EN}) เพื่อรับรางวัลจากเจ้าแห่งอัตราต่อรอง! 😄\n👉 เดิมพัน: [{AFF_LINK}]({AFF_LINK}) ด้วยรหัส [{PROMO_CODE}]\n💰 Coins: {{coins}}",
        "register_exists": f"*คุณลงทะเบียนแล้ว! 😄*\nตรวจสอบฟอร์มอีกครั้งที่: [{FORM_LINK_EN}]({FORM_LINK_EN}) เพื่อรับรางวัล!\n👉 เดิมพัน: [{AFF_LINK}]({AFF_LINK}) ด้วยรหัส [{PROMO_CODE}]\n💰 Coins: {{coins}}",
        "spin_result": f"*เจ้าแห่งอัตราต่อรองกำลังหมุนวงล้อ! 🎰*\nผลลัพธ์: {{result}}\n👉 เดิมพัน: [{AFF_LINK}]({AFF_LINK}) ด้วยรหัส [{PROMO_CODE}]",
        "spin_win": f"*ยินดีด้วย! 🎉*\nคุณได้รับ: {{result}} + {{coins_earned}} Coins\nรวม Coins: {{total_coins}} 💰\n👉 ลงทะเบียน: [{FORM_LINK_EN}]({FORM_LINK_EN}) | เดิมพัน: [{AFF_LINK}]({AFF_LINK})",
        "spin_lose": f"*โชคไม่ดี! 😅*\nผลลัพธ์: {{result}}, ลองใหม่อีกครั้ง! 🎲\n👉 ลงทะเบียน: [{FORM_LINK_EN}]({FORM_LINK_EN}) | เดิมพัน: [{AFF_LINK}]({AFF_LINK})",
        "vpn": f"*คู่มือ VPN สำหรับนักพนัน! 🔒*\n1. ดาวน์โหลด NordVPN หรือ ExpressVPN\n2. เชื่อมต่อกับเซิร์ฟเวอร์ใกล้ที่สุด\n3. ไปที่ [{AFF_LINK}]({AFF_LINK}) เพื่อเดิมพันอย่างมืออาชีพ! 😎\n📞 {PHONE} | ✉️ {EMAIL}",
        "leaderboard": f"*🏆 อันดับนักพนัน 🏆*\n{{leaderboard_text}}\n👉 เดิมพัน: [{AFF_LINK}]({AFF_LINK}) ด้วยรหัส [{PROMO_CODE}]"
    },
    "id": {
        "hi": f"*Halo penjudi! 🎉*\nAda odds panas? Cek /odds sekarang! 😎🎯\n👉 Taruhan di: [{AFF_LINK}]({AFF_LINK}) dengan kode [{PROMO_CODE}]\n📞 Kontak: {PHONE} | ✉️ {EMAIL}\n💰 Coins: {{coins}} | 🔑 Key: {API_KEY[:10]}...\n📝 Daftar: [{FORM_LINK_EN}]({FORM_LINK_EN})",
        "help": f"*Master odds datang membantu! 🚀*\n- /start: Pilih bahasa\n- /spin: Putar untuk Coins\n- /register: Daftar\n- /vpn: Panduan VPN\n- /leaderboard: Peringkat\n- /odds: Lihat odds\n👉 Daftar: [{FORM_LINK_EN}]({FORM_LINK_EN}) | 🔗 {WEB_LINK}\n📞 {PHONE} | ✉️ {EMAIL}",
        "how to play": f"*Panduan untuk penjudi! ⚽*\nPutar /spin untuk dapat Coins, cek /odds untuk tips, daftar di sini: [{FORM_LINK_EN}]({FORM_LINK_EN}). Main besar bareng teman! 💰\n👉 Taruhan: [{AFF_LINK}]({AFF_LINK}) dengan kode [{PROMO_CODE}]",
        "default": "*Master odds sedang istirahat! 😅*\nKetik /help atau tanya odds panas, saya bantu! 🚀\n📞 {PHONE} | ✉️ {EMAIL}",
        "register_new": f"*Pendaftaran berhasil, penjudi! 🎉*\nIsi formulir di: [{FORM_LINK_EN}]({FORM_LINK_EN}) agar Master odds bisa melacak dan memberi hadiah! 😄\n👉 Taruhan: [{AFF_LINK}]({AFF_LINK}) dengan kode [{PROMO_CODE}]\n💰 Coins: {{coins}}",
        "register_exists": f"*Kamu sudah terdaftar, penjudi! 😄*\nPeriksa kembali formulir di: [{FORM_LINK_EN}]({FORM_LINK_EN}) agar Master odds bisa mengelola dan memberi hadiah!\n👉 Taruhan: [{AFF_LINK}]({AFF_LINK}) dengan kode [{PROMO_CODE}]\n💰 Coins: {{coins}}",
        "spin_result": f"*Master odds memutar roda! 🎰*\nHasil: {{result}}\n👉 Taruhan: [{AFF_LINK}]({AFF_LINK}) dengan kode [{PROMO_CODE}]",
        "spin_win": f"*Selamat, penjudi! 🎉*\nKamu mendapatkan: {{result}} + {{coins_earned}} Coins\nTotal Coins: {{total_coins}} 💰\n👉 Daftar: [{FORM_LINK_EN}]({FORM_LINK_EN}) | Taruhan: [{AFF_LINK}]({AFF_LINK})",
        "spin_lose": f"*Kurang beruntung! 😅*\nHasil: {{result}}, coba lagi ya! 🎲\n👉 Daftar: [{FORM_LINK_EN}]({FORM_LINK_EN}) | Taruhan: [{AFF_LINK}]({AFF_LINK})",
        "vpn": f"*Panduan VPN untuk penjudi! 🔒*\n1. Unduh NordVPN atau ExpressVPN\n2. Hubungkan ke server terdekat\n3. Kunjungi [{AFF_LINK}]({AFF_LINK}) untuk taruhan seperti profesional! 😎\n📞 {PHONE} | ✉️ {EMAIL}",
        "leaderboard": f"*🏆 Peringkat penjudi 🏆*\n{{leaderboard_text}}\n👉 Taruhan: [{AFF_LINK}]({AFF_LINK}) dengan kode [{PROMO_CODE}]"
    }
  }
