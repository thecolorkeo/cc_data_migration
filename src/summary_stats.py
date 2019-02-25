# Keo Chan
# Insight Practice Coding Challenge W2

'''
Calculates summary statistics TABLE
after data_migration.py has transformed
JSON files into Postgres database.
'''

import sqlalchemy
from sqlalchemy import create_engine

def calc(table):
    password = 'password'
    database_name = 'cc_data_migration'
    engine = sqlalchemy.create_engine("postgresql://postgres:" + password + "@localhost/" + database_name)
    conn = engine.connect()

    engine.execute("CREATE TABLE IF NOT EXISTS " + table + "(colname VARCHAR(250), average NUMERIC, count NUMERIC)")
    engine.execute(
        '''
        INSERT INTO order_stats (colname, average, count)
        SELECT 'total_price_usd' AS colname, avg(total_price_usd::NUMERIC) AS average, count(total_price_usd::NUMERIC) AS count FROM orders GROUP BY user_id;
        '''
    )
