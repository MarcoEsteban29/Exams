**Exams**
-------------------
The objective is to analyze the total quantities of items bought by customers aged 18-35 from a sale conducted by Company XYZ. The extracted data will be stored in a CSV file for further analysis, and two approaches are provided: one using pure SQL and another using Pandas in Python.

**Components**
--------------------
1. **ETL Python Script (ETL_pandas_solution.py)**

**Requirements**: installed pandas and sqlite3 library to use script.
This Python script connects to a SQLite database, retrieves the necessary data based on the assignment requirements, processes the data using both SQL and Pandas, and stores the final output in a CSV file.

Features:
-Connects to the provided SQLite database and extracts customer age and total quantities of items bought by customers aged 18-35.

-Omits items where the quantity is zero and NULL.

-Ensures that quantities are whole numbers, as partial quantities are not applicable.

-Stores the resulting data in a CSV file with a semicolon (;) delimiter.

2. **Database (S30 ETL Assignment.db)**
This SQLite database contains the required tables and relationships for the ETL process. It includes:

orders table

sales table

customers table

items table

Tables are structured below:
![image](https://github.com/user-attachments/assets/8adf3227-8111-446c-8b44-f91402148da6)

**Approach**
-----------------
**A) SQL Approach**

-**SQL_query.py/ SQL Query.txt**

  Purely SQL query to get the desired output
  .
  The results are written directly to a CSV file using Python's sqlite3 and csv modules.
  
**B) Pandas Approach**

-**ETL_pandas_solution.py/ETL_pandas_4_table_solution.py**

  The SQLite data is loaded into a Pandas DataFrame using the read_sql_query method.
  
  Data is processed within Pandas to sum quantities for each item per customer aged 18-35.
  
  The output is filtered to exclude zero or null quantities and is saved to a CSV file with the specified delimiter.
