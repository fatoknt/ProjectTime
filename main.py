#!/usr/bin/env python3
#main.py

import click
from database.database import get_connection, create_table_employees

@click.group()
def cli():
    pass

@cli.command()
def test_db_connection():
    """DB接続テスト"""
    conn = get_connection()
    if conn:
        click.echo("DB接続に成功")
    else:
        click.echo("DB接続に失敗")

if __name__ == "__main__":
    cli()

@cli.command()
def create_employee_table():
    """employees テーブルを作成"""
