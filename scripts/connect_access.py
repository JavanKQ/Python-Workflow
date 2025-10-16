import pyodbc # needed to connect to database
import pandas as pd # needed to store results in dataframe, pd is shorthand for pandas so it's easier to type later
# conn_str variable defined as a raw string (r), driver has to be exact name for microsoft access database file, DBQ is the path to database file. ';' seperates parameters in connection.
conn_str = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\stl22\Formulation\formulation.accdb;"

try:
    # conn is variable that tells the pyodbc library to connect using the conn_str variable defined above
    conn = pyodbc.connect(conn_str)
    print("Connected to the database successfully.")  # confirms connection worked

    # Define SQL query as a string
    # Triple quotes """ allow the query to span multiple lines (optional here, could use single line too, but triple is cleaner for longer queries)
    query = """
    SELECT * FROM qc_results_mst
    WHERE SubmittedTime >= #2024-01-01#;
    """ # when defining what your query is, you must talk to the database using SQL syntax, * means "all columns", WHERE adds filters, #SubmittedTime is a date field so we use # to wrap the date value

    # Execute the SQL query and store results in a pandas DataFrame
    # pd.read_sql(query, conn) reads the SQL data using the connection and loads it into a table-like object (DataFrame)
    df = pd.read_sql(query, conn)

    print("Sample QC Results:")  # simple header so you know what the next print is
    print(df)  # prints the DataFrame to the terminal

    # Export the DataFrame to a CSV file
    # index=False means we don't write the row numbers to the CSV
    output_path = r"D:\Python312\Python-Workflow\output\qc_results_sample.csv" # 
    df.to_csv(output_path, index=False)
    print(f"Data exported to {output_path}")  # confirms export was successful

except Exception as e:
    # If anything goes wrong in the try block, Python jumps here
    # 'e' contains details about what error occurred
    print("Error connecting to the database:", e)

finally:
    # This runs whether or not there was an error
    # Safely closes the connection if it exists
    if 'conn' in locals():
        conn.close()
