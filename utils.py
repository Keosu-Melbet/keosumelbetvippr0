import json
import os
from config import (
    AFF_LINK, PROMO_CODE, FORM_LINK_EN,
    WEB_LINK, PHONE, EMAIL, API_KEY
)

# 📁 Đường dẫn file dữ liệu người dùng
DATA_FILE = "data.json"

# 💾 Tải dữ liệu người dùng từ file JSON
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

# 💾 Lưu dữ liệu người dùng vào file JSON
def save_data(data: dict):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 🔗 Getter cho các thông tin cấu hình
def get_affiliate_link() -> str:
    return AFF_LINK

def get_promo_code() -> str:
    return PROMO_CODE

def get_form_link(lang: str = "en") -> str:
    return FORM_LINK_EN  # Có thể mở rộng theo ngôn ngữ nếu cần

def get_web_link() -> str:
    return WEB_LINK

def get_phone() -> str:
    return PHONE

def get_email() -> str:
    return EMAIL

def get_api_key() -> str:
    return API_KEY

# 🏆 Tạo bảng xếp hạng giả lập
def get_leaderboard_text() -> str:
    # Có thể thay bằng dữ liệu thật nếu bạn lưu điểm người dùng
    return (
        "🏆 Bảng xếp hạng:\n"
        "1. Alice – 500 coins\n"
        "2. Bob – 420 coins\n"
        "3. Charlie – 390 coins"
    )
