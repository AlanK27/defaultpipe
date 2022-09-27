

import os
import pandas as pd
import pytest
import db_functions as db_func

### Fixtures

@pytest.fixtures
def example_df():
    return pd.read_csv("src\data\df2.csv")

### Test

@pytest.mark.skip(reason="query insert to DB, not real  test")
def test_insert_to_db(example_df):
    assert db_func.insert_to_db






