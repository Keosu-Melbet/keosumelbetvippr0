import aiosqlite
from datetime import datetime

DB_PATH = "keosu.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                spins INTEGER DEFAULT 0,
                coins INTEGER DEFAULT 0,
                last_spin TEXT
            )
        """)
        await db.commit()

async def register_user(user_id: int, username: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT OR IGNORE INTO users (user_id, username, last_spin) VALUES (?, ?, '')
        """, (user_id, username))
        await db.commit()

async def can_spin_today(user_id: int):
    today = datetime.now().strftime("%Y-%m-%d")
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT last_spin FROM users WHERE user_id = ?", (user_id,)) as cursor:
            row = await cursor.fetchone()
            return row is None or row[0] != today

async def update_spin(user_id: int, coins_won: int):
    today = datetime.now().strftime("%Y-%m-%d")
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            UPDATE users SET spins = spins + 1, coins = coins + ?, last_spin = ? WHERE user_id = ?
        """, (coins_won, today, user_id))
        await db.commit()

async def get_user_stats(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT spins, coins FROM users WHERE user_id = ?", (user_id,)) as cursor:
            return await cursor.fetchone()

async def get_leaderboard(limit=5):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT username, coins FROM users ORDER BY coins DESC LIMIT ?", (limit,)) as cursor:
            return await cursor.fetchall()
