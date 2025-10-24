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
while True:
    request_type = input("Enter the Request Type, Job Material Lot or FG Material List: ").strip().lower()
    if request_type in ["job material lot", "fg material list"]:
        break
    else:
        print("Invalid input. Please enter 'Job Material Lot' or 'FG Material List'.")

if request_type == "job material lot":
    while True:
        job_number = input("Enter the Job Number (e.g. JM00009456): ").strip().upper()
        if job_number.startswith("JM") and len(job_number) == 10:
            break
        else:
            print("Invalid Job Number format. Please ensure it starts with 'JM' and is 10 characters long.")

elif request_type == "fg material list":
    while True:
        item_number = input("Enter the Item Number: ").strip().upper()
        if item_number:
            break
        else:
            print("Item Number cannot be empty. Please enter a valid Item Number.")
else:
    print("Invalid Request Type")

with pyodbc.connect(conn_str) as conn:
    if request_type == "job material lot":
        query = f"""
        SELECT item, lot
        FROM ERP_Reporting.matltran_mst
        WHERE [ref_num] COLLATE SQL_Latin1_General_CP1_CI_AS = '{job_number}'
        AND [lot] <> '';
        """
        df=pd.read_sql(query, conn)
        print(f"Here are the material lots for {job_number}:")
        print(df)
    elif request_type == "fg material list":
        query = f"""
        ;WITH FirstRef AS (
            SELECT TOP 1 ref_num
            FROM ERP_Reporting.matltran_mst
            WHERE [item] COLLATE SQL_Latin1_General_CP1_CI_AS = '{item_number}'
              AND [trans_type] = 'F'
            ORDER BY ref_num
     )
        SELECT DISTINCT m.[item]
        FROM ERP_Reporting.matltran_mst AS m
        INNER JOIN FirstRef f ON m.ref_num = f.ref_num
        WHERE m.[trans_type] = 'I';
        """
        df=pd.read_sql(query, conn)
        print(f"Here is the material list for {item_number}:")
        print(df)