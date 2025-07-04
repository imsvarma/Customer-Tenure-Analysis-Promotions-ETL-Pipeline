# Customer Tenure Analysis & Promotion Pipeline

## Project Overview

This project implements a complete **ETL (Extract, Transform, Load) pipeline** that processes customer data to identify loyal customers based on tenure, loads the cleaned data into a SQL Server database, and creates visual dashboards in Power BI for targeted promotions.

---

## Getting Started

### 1. Install Required Python Packages

```bash
pip install pandas sqlalchemy pyodbc
```

### 2. Configure Your Database Connection

Edit your configuration in the script:

```python
server = 'YOUR_SERVER_NAME'
database = 'YOUR_DATABASE_NAME'
driver = 'ODBC Driver 17 for SQL Server'  # or your installed driver
```

### 3. Run the ETL Script

```bash
python etl_task.py
```

### 4. Connect Power BI (Optional)

- Open **Power BI Desktop**.
- Connect to your SQL Server database using your configured connection details.
- Use the **Customer** table to build dashboards and reports.

---

