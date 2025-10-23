import pandas as pd
import pyodbc

conn_str = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=cosmosdbsrv2.database.windows.net;"
    "Database=CCSQLDB_02;"
    "Authentication=ActiveDirectoryIntegrated;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)
request_type = input("Enter the Request Type, Job Material Lot or Item Material List: ").lower

if request_type == "job material lot":
    job_number = input("Enter the Job Number (e.g. JM00009456): ").upper()

elif request_type == "item material list":
    item_number = input("Enter the Item Number: ").upper()
else:
    print("Invalid Request Type")

with pyodbc.connect(conn_str) as conn:
    if request_type == "job material lot":
        query = f"""
        SELECT item, lot
        FROM ERP_Reporting.matltran_mst 
        WHERE [ref_num] = '{job_number}'
            AND [lot] <> '';
        """