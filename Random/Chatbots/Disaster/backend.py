import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")
        return None

# Database connection credentials
host = "localhost"  # For example, "localhost" or an IP address
user = "root"  # Your MySQL username
password = "shreyas"  # Your MySQL password
database = "IncidentReports"  # Your database name
# Connect to the database
connection = create_server_connection(host, user, password, database)

# Query to select all data
select_all_query = "SELECT * FROM Incidents;"
results = execute_read_query(connection, select_all_query)

# Convert to pandas DataFrame
if results:
    df = pd.DataFrame(results, columns=["IncidentID", "Type", "Description", "Latitude", "Longitude", "Date", "Time", "Severity", "ReportedBy"])
    print(df)
else:
    print("No data found or error in query execution")

# Database connection credentials


# Connect to the database
connection = create_server_connection(host, user, password, database)

# Query to select all data
select_all_query = "SELECT * FROM Incidents;"
execute_query(connection, select_all_query)
