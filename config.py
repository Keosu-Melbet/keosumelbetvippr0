import os
import pytz

BOT_TOKEN = os.getenv("BOT_TOKEN")
AFF_LINK = os.getenv("AFF_LINK")
FORM_LINK_EN = os.getenv("FORM_LINK_EN")
FORM_LINK_VN = os.getenv("FORM_LINK_VN")
WEB_LINK = os.getenv("WEB_LINK")
PROMO_CODE = os.getenv("PROMO_CODE")
PHONE = os.getenv("PHONE")
EMAIL = os.getenv("EMAIL")
API_KEY = os.getenv("API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
TZ = pytz.timezone('Asia/Ho_Chi_Minh')
DATA_FILE = "users.json"
