
import pandas as pd
from sqlalchemy.sql import text
import time, traceback

import dblib 
from cel_log import Logger

log = Logger()

redshift_engine = dblib.DB

def insert_to_db(data):
    sql = f""" insert into some_table 
            (some_keys, keys1, key2)
            values {data}
    """
    pass
    with redshift_engine.connect() as conn:
        conn.execute(sql)

