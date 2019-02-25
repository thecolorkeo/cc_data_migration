# Keo Chan
# Insight Practice Coding Challenge W2

'''
Read in text from a .zip file in JSON
and convert it to a table in Postgres.
'''

import sys
import os
import zipfile
import json
import pandas as pd
from pandas.io.json import json_normalize
import sqlalchemy
from sqlalchemy import create_engine
import summary_stats


def json_to_df(input_path, output_path):
    # unzip files into output_path folder
    unzipped = zipfile.ZipFile(input_path, 'r')
    os.chdir(output_path)
    unzipped.extractall()
    # read in json files and combine into one df
    results = []
    for file in unzipped.namelist():
        json_file = json.load(open(file, 'r'))
        normal = json_normalize(json_file)
        df = pd.DataFrame.from_dict(normal)
        results.append(pd.DataFrame(df.loc[0][0]))
    return pd.concat(results)

def df_to_postgres(df, table):
    password = 'password'
    database_name = 'cc_data_migration'
    engine = sqlalchemy.create_engine("postgresql://postgres:" + password + "@localhost/" + database_name)
    conn = engine.connect()

    engine.execute("CREATE TABLE IF NOT EXISTS " + table + "()")
    df.to_sql(table, engine, dtype = {'line_items': sqlalchemy.types.JSON}, if_exists = 'replace')

def main(input, output_unzipped):
    df = json_to_df(input, output_unzipped)
    df_to_postgres(df, 'orders')
    summary_stats.calc('order_stats')

if __name__ == '__main__':
    input_log = sys.argv[1]
    output_unzipped = sys.argv[2]
    main(input_log, output_unzipped)
