# python3
# employee.py

import sqlite3
from database.base import Database

class EmployeeTable(Database):
    """employees テーブル操作クラス"""

    def __init__(self, db_name="projecttime.db"):
        super().__init__(db_name)

    def create_table(self):
    """employeess テーブル作成"""
    with self as db:
        db.execute('''
                    CREATE TABLE IF NOT EXISTS employees (
                    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                        )
                   ''')
