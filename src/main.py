


from celery_worker import celery_works
from cel_log import Logger
from pathlib import Path

import db_functions as db_func

log = Logger()

class Star(celery_works):

    def __init__(self):
        pass 

    def start(self):
        data_loc = Path(r"/src/data/")
        df_lis = list(data_loc.iterdir())
        mah_lis = []
        for df_path in df_lis:
            k = self.process(df_path)
            k = ', \n'.join(k)
            mah_lis.append(k)

        parse_lis = ', \n'.join(mah_lis)
        write_path = Path(r"/src/") / 'mydf.csv'

        # write to s3
        with open(write_path, 'w') as wf:
            wf.write(parse_lis)

        file_lis = [write_path]
        db_func(file_lis, 'bucket_name')

        # write to Redshift
        db_func.insert_to_db(parse_lis)

        log.info('finished')


if __name__ == '__main__':
    st = Star()
    st.start()