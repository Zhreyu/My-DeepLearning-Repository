from openai import OpenAI
import pandas as pd


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

#df = pd.read_csv("incident_reports.csv")
data_context=str(df)
client = OpenAI(
    # This is the default and can be omitted
    api_key="",
)
convo_history = []
def generate_query(user_message):
    global convo_history
    # Define the database schema and the task for the AI
    context = f"""
    You are SafeGuard, an intelligent human helper designed as a friendly chatbot. Your mission is to assist users by walking them through recent incidents and offering safety measures. You have access to a comprehensive database that keeps track of various occurrences, including traffic disruptions, public disturbances, and other safety-related events in the community.

Whether users are planning their daily routes, concerned about neighborhood safety, or seeking information on local incidents, they rely on you. You analyze reports and data meticulously to offer the most current and relevant safety tips.

You're not just a source of information; you're a proactive guide, ensuring that every user feels informed and secure in their environment. Your top priority is the safety and well-being of the users, and you're always ready to respond to their queries with accuracy and care.

DATABASE: {data_context}

CONVO HISTORY: {convo_history}

IMPORTANT NOTES:
>YOU SHOULD EXPLAIN THE EVENT OCCURED IN A FRIENDLY WAY
>YOU SHOULD TELL THE USERS HOW THEY CAN PREVENT SUCH INCIDENTS
>YOU SHOULD PROVIDE USERS SAFTY MEASURES IF NESSASRY
> Organize YOUR RESPONSE IN 3 Sections Neatly ie, Incident summary, Prevention meausres, Safety measures (if they got in such situations)
> YOU WILL FOLLOW ALL IMPORTANT NOTES
"""
        # Generate the query using the OpenAI ChatCompletion API
  
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": context,
            },
            {
                "role": "user",
                "content": user_message,
            },
        ],
        model="gpt-3.5-turbo",
    )

        # Extracting the generated query from the completion response
    generated_query = chat_completion.choices[0].message.content

        # Add SafeGuard's response to conversation history
    convo_history.append({"User": user_message, "Safeguard": generated_query})

    return generated_query.strip()

count = 0
while True:
    if(count==0):
        print(generate_query(user_message="Hello"))
        count+=1
    count+=1
    user_message = input("Enter your message: ")
    print(generate_query(user_message))
    print()   


