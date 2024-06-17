# python3
# base.py

import sqlite3
import os.path

class Database:
    """DB接続の基底クラス"""
    def __init__(self, db_name="projecttime.db") -> None:
        """DBに接続する

        Args:
            db_name (str) : DBファイル名 (デフォルト -> "projecttime.db")

        Raises:
            sqlite3.OperationalError: DBファイルが無いか、接続に失敗した場合 

        """
        if not os.path.exists(db_name):
            raise sqlite3.OperationalError(f"DBファイルが見つかりません: {db_name}")

        try:
            self.conn = sqlite3.connect(db_name) #接続
        except sqlite3.Error as e:
            print(f"DB接続エラー: {e}")
            raise

    def __enter__(self):
        """with構文に入った時呼び出される"""
        return self

    def __exit__(self, _exc_type, _exc_value, _traceback) -> None:
        """with構文から抜ける時に呼び出される"""
        self.conn.close()

    def execute(self, sql: str, parameters: tuple =()) -> sqlite3.Cursor:
        """SQLクエリ実行

        Args:
            sql (str): 実行するsqlクエリ
            parameters (tuple) クエリのパラメータ (デフォルト -> 空のタプル)
        Returns:
            sqlite3.Cursor: カーソルオブジェクト
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, parameters)
        self.conn.commit()
        return cursor
