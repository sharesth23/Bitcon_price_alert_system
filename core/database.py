import sqlite3
import time
from bitcoin_tracker.config import DB_PATH

class Database:
    def __init__(self, path=DB_PATH):
        self.path = path
        self._init_db()

    def _connect(self):
        return sqlite3.connect(self.path)

    def _init_db(self):
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY,
            timestamp INTEGER,
            price REAL,
            currency TEXT,
            source TEXT
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY,
            timestamp INTEGER,
            level TEXT,
            price REAL,
            change REAL,
            message TEXT
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS portfolio (
            id INTEGER PRIMARY KEY,
            btc REAL,
            purchase_price REAL,
            currency TEXT,
            note TEXT
        )
        """)

        conn.commit()
        conn.close()

    def save_price(self, data):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO prices VALUES (NULL, ?, ?, ?, ?)",
            (data["timestamp"], data["price"], data["currency"], ",".join(data["sources"]))
        )
        conn.commit()
        conn.close()


