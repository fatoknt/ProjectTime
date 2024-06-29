# test_employee_controller.py

import unittest
from unittest.mock import patch
from database.employee import EmployeeTable
from controllers.employee_controller import EmployeeContoroller
from views.employee_views import EmployeeViews

class TestEmployeeController(unittest.TestCase):
    def setUp(self) -> None:
        self.db: EmployeeTable = EmployeeTable(":memory:")
        self.db.create_table()
        self.controller: EmployeeContoroller = EmployeeContoroller()
        self.views: EmployeeViews = EmployeeViews()

    def tearDown(self) -> None:
        self.db.conn.close()
