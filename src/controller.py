from mysql.connector import connect
from auth_data import *


# Write function to list all cities in the Sakila.city table

def get_all_cities():
    # Step 1: Create db connection
    with connect(host=HOSTNAME, user=USER_NAME, password=PASSWORD) as mysql_connection:
        # Step 2: Create cursor object
        with mysql_connection.cursor() as cursor:
            # Step 3: Execute Query
            query = "select * from sakila.city;"
            cursor.execute(query)
            # Step 4: Fetch all data returned after query execution
            all_cities = cursor.fetchall()
            print(all_cities)


get_all_cities()
