import os
import pymysql

# Get username from Gitpod Workspace
# (modify this variable if running on another environment)
username = os.getenv('carhul')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password="",
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    # Close the connection
    # Regardless of whether or not the above was successful
    connection.close()
