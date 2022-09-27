
import boto3
from datetime import datetime

from cel_log import Logger

log = Logger()

def processing_segment(range, id, date):
    month, day = date.split('-')
    date_type = datetime(2000, int(month), int(day))
    return f"('{range}', '{id}', {date_type})"

def insert_to_s3(files, bucket):
    s3_resource = boto3.resource('s3')
    for key in files:
        try:
            s3_resource.Object(bucket, key)
        
        except Exception as e:
            log.error(e)

