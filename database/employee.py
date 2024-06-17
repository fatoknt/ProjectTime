# python3
# employee.py

import sqlite3
from database.base import Database

class EmployeeTable(Database):
    """employees テーブル操作クラス"""

    def __init__(self, db_name: str ="projecttime.db") -> None:
        super().__init__(db_name)

    def create_table(self) -> bool:
        """employees テーブル作成

        Returns:
            bool: テーブル作成の成功(True) または失敗 (False)
        """
        try:
            with self as db:
                db.execute(sql = '''
                            CREATE TABLE IF NOT EXISTS employees (
                            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL UNIQUE
                                )
                           ''')
            return True
        except sqlite3.Error as e:
            print(f"employee テーブル作成失敗エラー: {e}")
            return False

    def insert_employee(self, name: str) -> int | None:
        """ 従業員を employees テーブルに挿入します。

        Args:
            name (str): 従業員名

        Returns:
            int | None: 追加された従業員のID。失敗した場合は None を返します。
        """
        try:
            with self as db:
                cursor: sqlite3.Cursor = db.execute(
                    "INSERT INTO employees (name) VALUES (?)", (name, ))
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"エラー: 既に同じ名前の従業員が存在します。")
            return None
        except sqlite3.Error as e:
            print(f"データベースエラー: {e}")
            return None

    def select_all_employees(self) -> list[tuple]:
        """ employees テーブルからすべての従業員を取得します。

        Returns:
            list[tuple]: 従業員情報 (employee_id, name), 存在しない場合は None を返します
        """
        with self as db:
            return db.execute("SELECT * FROM employees").fetchall()
