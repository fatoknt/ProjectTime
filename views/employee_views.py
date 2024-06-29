# employee_views.py

import click
from models.employee_model import EmployeeModel

class EmployeeViews:
    """従業員ビュークラス"""

    def get_employee_name_input(self) -> str:
        """従業員名を入力させます。

        Ruturns:
            str: 入力された従業員名
        Raises:
            KeyboardInterrupt: 入力が中断された場合
        """
        while True:
            try:
                name = click.prompt("従業員名を入力してください")
                if name:
                    return name
                else:
                    click.echo("エラー: 従業員名は必須です。")
            except KeyboardInterrupt:
                raise # 例外を再送出し、呼び出し元で処理
    
    def display_employee_list(self, employees: list[EmployeeModel]) -> None:
        """従業員情報一覧を表示させます。

        Args:
            employees (list[tuple]) : 従業員情報 (employee_id, name) のリスト
        """
        if not employees:
            click.echo("従業員は登録されていません。")
            return

        click.echo("従業員一覧:")
        for employee in employees:
            click.echo(f"- ID: {employee.employee_id}, 名前: {employee.name}")

    def get_employee_id_input(self) -> int:
        """従業員IDを入力させます。
        
        Returns:
            int: 入力された従業員ID
        """
        while True:
            try:
                employee_id = int(click.prompt("従業員IDを入力してください。"))
                if employee_id > 0:
                    return employee_id
                else:
                    click.echo("エラー: 従業員IDは正の整数で入力してください。")
            except ValueError:
                click.echo("エラー: 従業IDは整数で入力してください。")
