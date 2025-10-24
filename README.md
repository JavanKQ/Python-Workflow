\# Python Workflow Projects



This repository contains a collection of beginner-to-intermediate Python scripts written as part of a learning journey to become a more skilled developer and data analyst. Each script focuses on practical database interaction, data manipulation, and analysis workflows — primarily using `pyodbc`, `pandas`, and `matplotlib`.



The goal of this repository is to learn by doing: writing working code that connects to live data sources, extracts insights, and builds useful outputs.



---



\## Project Overview



\### `connectcosmosdb.py`



A test script for connecting to a Microsoft SQL Server (Azure Cosmos) database using Active Directory Integrated Authentication.

\*\*Note:\*\* Only works on domain-joined machines with the proper credentials (not on personal computers).



\*\*Key Concepts:\*\*



\* Using `pyodbc` for SQL Server connections

\* Secure authentication via Active Directory Integrated



---



\### `connectformulationdb.py`



Connects to an Access database on a shared network drive to verify connection capability.



\*\*Key Concepts:\*\*



\* Access database connection strings (`.accdb`)

\* Basic `pyodbc` connection testing



---



\### `cosmosdbquery.py`



An interactive script that queries a SQL Server database (`CCSQLDB\_02`) for manufacturing data.



\*\*Features:\*\*



\* User input with validation and retry logic

\* Two query modes:



&nbsp; \* \*\*Job Material Lot\*\* – returns material and lot information for a given job number

&nbsp; \* \*\*FG Material List\*\* – finds items used in a finished good’s first formulation reference

\* Results displayed via `pandas` DataFrame



\*\*Key Concepts:\*\*



\* SQL querying with parameters

\* Input validation loops

\* Conditional query logic

\* Basic data retrieval and display with `pandas`



---



\### `driver\_test.py`



Lists all installed ODBC drivers available on the system.



\*\*Key Concepts:\*\*



\* Enumerating ODBC drivers with `pyodbc.drivers()`



---



\### `exportqcresults.py`



Pulls recent QC (Quality Control) results from the Formulation Access Database and exports them to a CSV file.



\*\*Features:\*\*



\* SQL querying and data extraction

\* Data export to CSV

\* Try/except/finally error handling



\*\*Key Concepts:\*\*



\* Querying Access data with `pyodbc`

\* Using `pandas` to structure and export data

\* Safe connection management with exception handling



---



\### `trendanalyzer.py`



Performs parameter-based trend analysis (e.g., viscosity, density, solids, pH) for a specific LQ Code over a date range.



\*\*Features:\*\*



\* User-defined parameters, item, and date range

\* Fetches QC data and spec limits

\* Visual trend plotting using `matplotlib`

\* Saves trend charts as PDFs



\*\*Key Concepts:\*\*



\* Joining data from multiple tables

\* SQL filters with dynamic inputs

\* Plotting and saving results with `matplotlib`

\* Data validation and visualization



---



\## Requirements



\* Python 3.12+

\* Installed Libraries:



```bash

pip install pyodbc pandas matplotlib

```



\* Drivers:



&nbsp; \* ODBC Driver 18 for SQL Server

&nbsp; \* Microsoft Access Database Engine (for `.accdb` connections)



---



\## Folder Structure



```

Python-Workflow/

│

├── scripts/

│   ├── connectcosmosdb.py

│   ├── connectformulationdb.py

│   ├── cosmosdbquery.py

│   ├── driver\_test.py

│   ├── exportqcresults.py

│   ├── trendanalyzer.py

│

├── output/

│   ├── qc\_results\_sample.csv

│   └── \[auto-generated trend PDFs]

│

└── README.md

```



---



\## Learning Focus



This repository is part of an ongoing growth in:



\* Writing clean, functional Python code

\* Working with real-world data sources

\* Strengthening SQL and database fundamentals

\* Building analytical workflows that connect data → logic → insight



Each script represents a small, self-contained project — the goal is progress and learning.



---



\## Future Plans



\* Add logging and error reporting

\* Build reusable helper modules for shared database logic

\* Create a simple CLI interface to select and run scripts

\* Explore visualization dashboards with Plotly or Streamlit



---



Author



Javan

Missions \& Outreach Director | Quality Control Technician





