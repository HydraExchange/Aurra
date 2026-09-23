import sqlite3
from pathlib import Path

from config import DATABASE_PATH


def get_connection():
    Path(DATABASE_PATH).parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row

    return conn


def init_db():
    with get_connection() as conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL UNIQUE,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount INTEGER NOT NULL,
            price_usd REAL NOT NULL,
            payment_method TEXT,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );

        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            provider TEXT NOT NULL,
            external_id TEXT,
            amount_usd REAL,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(order_id) REFERENCES orders(id)
        );
        """)


def save_user(
    telegram_id: int,
    username: str | None,
    first_name: str | None,
    last_name: str | None,
):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO users (
                telegram_id,
                username,
                first_name,
                last_name
            )
            VALUES (?, ?, ?, ?)

            ON CONFLICT(telegram_id)
            DO UPDATE SET
                username = excluded.username,
                first_name = excluded.first_name,
                last_name = excluded.last_name,
                updated_at = CURRENT_TIMESTAMP
        """, (
            telegram_id,
            username,
            first_name,
            last_name,
        ))


def get_user(telegram_id: int):
    with get_connection() as conn:
        return conn.execute(
            "SELECT * FROM users WHERE telegram_id = ?",
            (telegram_id,)
        ).fetchone()


if __name__ == "__main__":
    init_db()
    print("SQLite database initialized.")