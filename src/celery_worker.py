


from celery import Celery
import concurrent.futures
import pandas as pd
import random
import time, traceback

from config import config
import db_functions as db_func
import functions as func
from cel_log import Logger

log = Logger()

cel_redis_url= config['redis_url']
# cel_redis_url = "redis://localhost:6379/0"

try:
    celery = Celery(__name__)
    celery.conf.broker_url = cel_redis_url
except Exception as e:
    log.error(e)
    log.error(f'couldnt connect to celery {cel_redis_url}')


class celery_works:


    def __init__(self):
        self.m_lis = []

    @celery.task(bind=True)
    def process(self, path):
        m_lis = []
        self.marker = random.randint(0,999)
        df = pd.read_csv(path)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            try:
                futures = []

                for df_ in df.itertuples():
                    futures.append(executor.submit(func.processing_segment, 
                            range = df_.range, id = df_.id, date = df_.date))

                for future in concurrent.futures.as_completed(futures):
                    log.info(self.marker)
                    m_lis.append(future.result())
            except:
                log.info('failed')

        return m_lis
    

