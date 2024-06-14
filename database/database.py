# database.py

import sqlite3
import os.path

def get_connection(db_name="projecttime.db"):
    """DBへの接続を取得する"""
    if not os.path.exists(db_name):
        raise sqlite3.OperationalError(f"データベースファイルが見つかりません: {db_name}")

    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"データベース接続エラー: {e.args[0]}")
        return None

def create_table_employees(conn):
    """employeesテーブルの作成"""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
            )
    ''')
    conn.commit()
