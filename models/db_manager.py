import sqlite3
from datetime import datetime
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "expenses.db")

class DatabaseManager:
    def __init__(self):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                amount REAL,
                category TEXT,
                type TEXT,
                notes TEXT
            )
        ''')
        self.conn.commit()

    def add_transaction(self, amount, category, t_type, notes):
        self.cursor.execute('''
            INSERT INTO transactions (date, amount, category, type, notes)
            VALUES (?, ?, ?, ?, ?)
        ''', (datetime.now().strftime("%Y-%m-%d"), amount, category, t_type, notes))
        self.conn.commit()

    def fetch_transactions(self):
        self.cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
        return self.cursor.fetchall()

    def delete_transaction(self, transaction_id):
        self.cursor.execute("DELETE FROM transactions WHERE id=?", (transaction_id,))
        self.conn.commit()

    def get_summary(self):
        self.cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='Income'")
        income = self.cursor.fetchone()[0] or 0

        self.cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='Expense'")
        expense = self.cursor.fetchone()[0] or 0

        return income, expense, income - expense
