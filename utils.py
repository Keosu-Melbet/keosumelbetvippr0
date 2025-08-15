import json, os, requests, re, logging
from config import DATA_FILE, API_KEY, SEARCH_ENGINE_ID

logger = logging.getLogger(__name__)

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Load error: {e}")
        return {}

def save_data(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        logger.error(f"Save error: {e}")

def search_google(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        results = response.json().get("items", [])
        return results[0]["snippet"] if results else None
    except Exception as e:
        logger.error(f"Google search error: {e}")
        return None

def extract_score_or_odds(text):
    score = re.search(r"\b(\d+[:-]\d+)\b", text)
    odds = re.search(r"\b(\d+\.?\d*(?:/-?\d+\.?\d*)?)\b", text) if not score else None
    if score:
        return f"Tỷ số dự đoán: {score.group(0)}"
    elif odds:
        return f"Odds dự đoán: {odds.group(0)}"
    return "Không tìm thấy odds, bro! 😅 Thử lại sau!"
