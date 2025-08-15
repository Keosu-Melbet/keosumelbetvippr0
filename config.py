import os
import pytz

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
ADMIN_ID = [5923493385]  # ← Đây là Telegram user ID của bạn
AFFILIATE_LINK = os.getenv("AFF_LINK")
FORM_LINK_EN = os.getenv("FORM_LINK_EN")
FORM_LINK_VN = os.getenv("FORM_LINK_VN")
WEB_LINK = os.getenv("WEB_LINK")
AGENT_CODE = os.getenv("AGENT_CODE")
HOTLINE = os.getenv("PHONE")
EMAIL = os.getenv("EMAIL")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
TZ = pytz.timezone('Asia/Ho_Chi_Minh')
DATA_FILE = "users.json"
DIFY_API_KEY = os.getenv("DIFY_API_KEY")
DIFY_API_URL = "https://api.dify.ai/v1/chat-messages"
PORT=8443

