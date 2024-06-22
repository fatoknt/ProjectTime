# python3
# test_database.py

import unittest
import sqlite3
from database.base import Database

class TestDatabase(unittest.TestCase):
    def test_database_connection(self):
        """DB接続テスト"""
        
        # 正常系: 既存のDBファイルに接続できる
        with Database("projecttime.db") as db:
            self.assertIsInstance(db.conn, sqlite3.Connection) 
            #接続オブジェクトがsqlite3.Connectionである事を確認

        # 異常系: 存在しないDBに接続使用とすると例外が発生する
        with self.assertRaises(sqlite3.OperationalError):
            Database("non_existent.db")

    def test_execute(self):
        """SQLクエリ実行テスト"""

        with Database("projecttime.db") as db:
            cursor = db.execute("SELECT * FROM employees") # employees テーブルがある事前提
            self.assertIsInstance(cursor, sqlite3.Cursor) # カーソルオブジェクトである事を確認 

