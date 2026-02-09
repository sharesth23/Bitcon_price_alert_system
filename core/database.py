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
