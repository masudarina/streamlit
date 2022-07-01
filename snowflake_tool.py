#import os
from snowflake.snowpark import Session

connection_parameters = {
"account":"nttdataaiottdp-snowpark",
"user":"masudar",
"password":"Taylor1213",
"role":"SYSADMIN",
"warehouse":"PARK_WH",
"database":"MASUDATEST",
"schema":"PUBLIC"
}

session = Session.builder.configs(connection_parameters).create()


print('[START] Checking All Warehouses...')

session.sql("show warehouses").collect()
result = session.sql('''SELECT "name"  AS WAREHOUSE_NAME ,"size" AS WAREHOUSE_SIZE,"auto_suspend" AS AUTO_SUSPEND_TIME FROM TABLE(RESULT_SCAN(LAST_QUERY_ID())) order by "size"''').collect()
python_df = session.create_dataframe(result)
pandas_df = python_df.to_pandas()
pandas_df.index = pandas_df.index + 1
print('[CHART] All Warehouses')
pandas_df
