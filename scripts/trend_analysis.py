import pyodbc  # needed to connect to database
import pandas as pd  # needed to store results in a DataFrame; 'pd' is shorthand
import matplotlib.pyplot as plt  # needed for plotting trends

# Define connection string
# DRIVER = exact name of the Access driver, DBQ = path to your Access database, ';' separates parameters
conn_str = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\stl22\Formulation\formulation.accdb;"

# Parameter mapping to match Access column names
param_map = {
    "viscosity": "Viscosity (cP)",
    "density": "Density (lbs/gal)",
    "solids": "Quick Solids (%w/w)",
    "ph": "pH"
}

# Get user inputs
item_number = input("Enter the LQ Code Item Number: ")
user_param = input("Enter the parameter to analyze (viscosity, density, solids, ph): ").lower()
from_date = input("Enter the start date (YYYY-MM-DD): ")
to_date = input("Enter the end date (YYYY-MM-DD): ")

# Validate parameter
parameter = param_map.get(user_param)
if parameter is None:
    print("Invalid parameter entered!")
    exit()

# Use a context manager 'with' to handle connection automatically
# Python will automatically close the connection when the block ends
with pyodbc.connect(conn_str) as conn:
    print("Connected Successfully!")

    # Define SQL query with user inputs
    query = f"""
    SELECT SubmittedTime, [{parameter}]
    FROM qc_results_mst
    WHERE [LQ Code] = '{item_number}'
      AND SubmittedTime BETWEEN #{from_date}# AND #{to_date}#
    ORDER BY SubmittedTime ASC;
    """

    # Execute query and load results into pandas DataFrame
    df = pd.read_sql(query, conn)

    if df.empty:
        print("No data found for the given inputs.")
    else:
        print("Data retrieved successfully.")
        print(df)  # shows the DataFrame in terminal

        # Plotting the trend
        plt.figure(figsize=(10, 5))
        plt.plot(df['SubmittedTime'], df[parameter], marker='o', linestyle='-')
        plt.title(f"{parameter} Trend for {item_number}")
        plt.xlabel("Submitted Time")
        plt.ylabel(parameter)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        output_path = rf"D:\Python312\Python-Workflow\output\{item_number}_{parameter}_{from_date}_{to_date}.pdf"
        plt.savefig(output_path)
        plt.show()