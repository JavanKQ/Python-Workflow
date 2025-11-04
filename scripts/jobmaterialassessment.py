import pandas as pd
from sqlalchemy import create_engine
import urllib

params = urllib.parse.quote_plus(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=cosmosdbsrv2.database.windows.net;"
    "Database=CCSQLDB_02;"
    "Authentication=ActiveDirectoryIntegrated;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

while True:
    job_number = input("Enter the Job Number you wish to assess the materials of (e.g. JM9456, JB19456): ").strip().upper()

    if len(job_number) < 10:
        job_number = job_number[:2] + job_number[2:].zfill(8)
    elif len(job_number) > 10:
        print("Job Number is too long. Please enter a valid Job Number.")
        continue

    query = f"""
    SELECT job
    FROM ERP_Reporting.job_mst
    WHERE [job] COLLATE SQL_Latin1_General_CP1_CI_AS = '{job_number}';
    """

    try:
        df = pd.read_sql(query, engine)
    except Exception as e:
        print(f"An error occurred while querying the database: {e}")
        continue

    if df.empty:
        print("Job Number not found. Please enter a valid Job Number.")
        continue
    else:
        break

print(f"{job_number} found. Proceeding with material assessment...")
