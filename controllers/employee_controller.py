# employee_controller.py

import click
from models.employee_model import EmployeeModel
from database.employee import EmployeeTable
from views.employee_views import EmployeeViews

class EmployeeContoroller:
    """従業員コントロールクラス"""

    def __init__(self, db_name: str = "projecttime.db") -> None:
        """データベースに接続します。"""
        self.table: EmployeeTable = EmployeeTable(db_name)
        self.views: EmployeeViews = EmployeeViews()

    def add_employee(self) -> None:
        """従業員を追加します。"""
        pass
