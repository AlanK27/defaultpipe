

import os
import pandas as pd
import pytest
import functions as func



### Fixtures



### Test

def test_processing_segment():
    range = 1
    id = 234
    date = "10-9"
    string = func.processing_segment(range,id,date)
    assert "('1', '234', '2000-10-9')" == string

@pytest.mark.skip(reason='upload file to s3')
def test_insert_to_s3():
    assert func.insert_to_s3('some_file', 'bucket')








