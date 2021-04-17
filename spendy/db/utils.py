import os
import yaml

from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from spendy import DB_CONNECTION_STRING


def get_db_engine() -> Engine:
    return create_engine(DB_CONNECTION_STRING)


def get_id(row: str) -> int:
    return int.from_bytes(row.encode('utf-8'), byteorder='big') % (10 ** 16)


def get_process_ts():
    return datetime.datetime.now
