
import pymysql.cursors
from sqlalchemy import create_engine

from cel_log import Logger
from config import config

class DB:


    def __init__(self):
        self.engine = create_engine(f"mysql://{config['cred']}")

    def connect(self):
        return self.engine.connect(0)


