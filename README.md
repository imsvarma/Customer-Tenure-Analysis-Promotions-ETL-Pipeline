Customer Tenure Analysis & Promotion Pipeline
Project Overview
This project implements a complete ETL (Extract, Transform, Load) pipeline that processes customer data to 
identify loyal customers based on tenure, loads the cleaned data into a SQL Server database, 
and creates visual dashboards in Power BI for targeted promotions.

1. Install required Python packages
   pip install pandas sqlalchemy pyodbc

2. Configure your database connection
   server = 'YOUR_SERVER_NAME'
   database = 'YOUR_DATABASE_NAME'
   driver = 'ODBC Driver 17 for SQL Server'  # or your installed driver

3.Run the ETL script
  python etl_task.py
  
4. Connect Power BI (optional)
   Open Power BI Desktop.
   Connect to your SQL Server database using your configured connection details.
   Use the Customer table to build dashboards and reports.

