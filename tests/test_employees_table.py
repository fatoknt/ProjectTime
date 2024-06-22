# python3
# test_employees_table.py

import unittest
from database.employee import EmployeeTable

class TestEmployeeTable(unittest.TestCase):
    """ 従業員テーブル接続テスト"""

    IN_MEMORY_DB_NAME = ":memory:"

    """"""
    def test_create_table(self) -> None:
        """employee テーブル作成のテスト"""
        with EmployeeTable(self.IN_MEMORY_DB_NAME) as db:
            result: bool = db.create_table()
            self.assertTrue(result)

    def test_insert_employee(self) -> None:
        """従業員登録のテスト"""

        with EmployeeTable(self.IN_MEMORY_DB_NAME) as db:
            db.create_table()

            # 正常系: 従業員が正常に登録できる事
            employee_id: int|None = db.insert_employee("テスト太郎")
            self.assertIsNotNone(employee_id)
            assert employee_id is not None

            employee = db.get_employee_by_id(employee_id)
            assert employee is not None
            self.assertEqual(employee[1], "テスト太郎")

            # 異常系: 同名の従業員が既に登録済である場合
            employee_id: int|None = db.insert_employee("テスト太郎")
            self.assertIsNone(employee_id)

    def test_select_all_employees(self) -> None:
        """全従業員取得のテスト"""
        with EmployeeTable(self.IN_MEMORY_DB_NAME) as db:
            db.create_table()
            test_employees: list = [
                    ("テスト太郎",),
                    ("テスト二郎",),
                    ("テスト三郎",)
                    ]

            for employee in test_employees:
                db.insert_employee(employee[0]) #従業員登録

            # 全従業員取得
            employees = db.select_all_employees()

            # 取得した従業員の数が正しいか確認
            self.assertEqual(len(employees), len(test_employees))

            # 取得した従業員の情報が正しいか確認
            for i, employee in enumerate(employees):
                self.assertEqual(employee[1], test_employees[i][0])

    def test_get_employee_by_id(self) -> None:
        """従業員検索テスト"""
        with EmployeeTable(self.IN_MEMORY_DB_NAME) as db:
            db.create_table()
            employee_id: int|None = db.insert_employee("テスト太郎")
            
            assert employee_id is not None
            employee = db.get_employee_by_id(employee_id)
            self.assertIsNotNone(employee)
            assert employee is not None
            self.assertEqual(employee[1], "テスト太郎")

            #異常系: 存在しないIDを指定した場合
            not_existent_employee = db.get_employee_by_id(999)
            self.assertIsNone(not_existent_employee)

    def test_update_employee(self) -> None:
        """従業員情報更新のテスト"""
        with EmployeeTable(self.IN_MEMORY_DB_NAME) as db:
            db.create_table()

            # 正常系: 従業員情報を更新できる事
            employee_id: int|None = db.insert_employee("テスト太郎")
            assert employee_id is not None
            success: bool = db.update_employee(employee_id, "テスト二郎")
            self.assertTrue(success) # 更新成功

            employee: tuple|None = db.get_employee_by_id(employee_id)
            self.assertIsNotNone(employee)
            assert employee is not None
            self.assertEqual(employee[1], "テスト二郎")

            # 異常系: 既存の名前で更新しようとした時
            db.insert_employee("テスト太郎")
            success: bool = db.update_employee(employee_id, "テスト太郎")
            self.assertFalse(success)

    def test_delete_employee(self) -> None:
        """従業員削除のテスト"""
        with EmployeeTable(self.IN_MEMORY_DB_NAME) as db:
            db.create_table()
            employee_id: int|None = db.insert_employee("テスト太郎")

            assert employee_id is not None
            db.delete_employee(employee_id)

            employee = db.get_employee_by_id(employee_id)
            self.assertIsNone(employee)
