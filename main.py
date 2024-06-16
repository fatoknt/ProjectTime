#!/usr/bin/env python3
#main.py

import click
from database.database import get_connection, create_table_employees

@click.group()
def cli():
    pass

