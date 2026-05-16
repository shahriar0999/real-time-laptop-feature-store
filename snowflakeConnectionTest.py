import snowflake.connector, os
from dotenv import load_dotenv
load_dotenv()

conn = snowflake.connector.connect(
    account=os.environ["SNOWFLAKE_ACCOUNT"],
    user=os.environ["SNOWFLAKE_USER"],
    password=os.environ["SNOWFLAKE_PASSWORD"],
    warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
)
print("✅ Connected!", conn.cursor().execute("SELECT CURRENT_VERSION()").fetchone())
conn.close()