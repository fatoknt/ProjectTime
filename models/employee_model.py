# employee_model.py

from dataclasses import dataclass

@dataclass
class EmployeeModel:
    """従業員データを表すモデルクラス"""
    employee_id: int
    name: str

    @classmethod
    def from_tuple(cls, data: tuple) -> EmployeeModel: #type: ignore
        """タプルから EmployeeModel を作成します。

        Args:
            data (tuple): 従業員情報 (employee_model, name)
        Returns:
            EmployeeModel: EmployeeModel インスタンス

        """
        return cls(*data)
