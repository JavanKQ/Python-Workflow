Python QC Database Tools



This project contains Python scripts I’ve written as I’m learning how to use Python for tasks that support my work in quality control. The goal is to become more comfortable with Python and build small tools that interact with databases, process data, and visualize trends.



Project Overview



The repository currently contains two scripts:



1\. export\_qc\_results.py



This script connects to a Microsoft Access database and exports QC results to a CSV file.



Key Features:



Connects to an Access database using pyodbc.



Executes a SQL query to fetch all QC results submitted after a specific date.



Loads the query results into a pandas DataFrame for easy manipulation.



Exports the DataFrame to a CSV file for further analysis or reporting.



Includes basic error handling to ensure the connection is safely closed even if an error occurs.



2\. plot\_qc\_trends.py



This script allows the user to visualize trends for specific QC parameters over time.



Key Features:



Connects to the same Access database using pyodbc.



Prompts the user for the item number, QC parameter (viscosity, density, solids, pH), and a date range.



Queries the database for the specified parameter and timeframe.



Loads the results into a pandas DataFrame.



Generates a trend plot using matplotlib and saves it as a PDF.



Handles cases where no data is returned.



Learning Goals



Practice connecting to databases with Python.



Learn to write SQL queries and filter data programmatically.



Gain experience using pandas for data manipulation.



Visualize data trends with matplotlib.



Build confidence in creating small, functional tools as a beginner.



Requirements



Python 3.x



Libraries: pyodbc, pandas, matplotlib



Microsoft Access database (.mdb or .accdb) with QC results



Usage



Update the connection string in each script to point to your Access database.



Run the scripts in a Python environment.



Follow prompts (for plot\_qc\_trends.py) or check the exported CSV (for export\_qc\_results.py).

