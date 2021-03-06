import snowflake.connector
import pandas as pd
import streamlit as st

# set variables
sf_user = "masudar"
sf_password = "Taylor1213"
sf_account = "qp20383.ap-northeast-1.aws"
sf_role = "accountadmin"
sf_warehouse = "COMPUTE_WH"

# set Snowflake Connector
ctx = snowflake.connector.connect(
user=sf_user,
password=sf_password,
account=sf_account
)

cs = ctx.cursor()

# set role
cs.execute("use role " + sf_role)
# set warehouse
cs.execute("use warehouse " + sf_warehouse)

cs.execute("show warehouses")
result = cs.execute('''SELECT "name", "size", "auto_suspend" FROM TABLE(RESULT_SCAN(LAST_QUERY_ID())) order by "size"''').fetchall()
columns1 = ['WAREHOUSE_NAME', 'WAREHOUSE_SIZE', 'AUTO_SUSPEND']
if not result:
    print("[INFO] Check Successed")
    print("[INFO] No Warehouses for the condition")
else:
    print("[INFO] Check Successed")
    df1 = pd.DataFrame(data=result, columns=columns1) 
    df1.index = df1.index + 1
    print('[CHART] Information of all Warehouses order by size')
    st.table(df1)
