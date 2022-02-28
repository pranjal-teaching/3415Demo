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
            # print(all_cities)
            city_list = []
            for city in all_cities:
                city_list.append(city[1])
    return city_list


cities = get_all_cities()
print(cities)


def get_actors_for_movie_by_title(title: str) -> list:
    """
    This function takes the name of the movie and returns a list of all the actors in the movie

    SQL Query (May need a small modification):

    SELECT
        f.film_id, f.title, fa.actor_id, a.first_name, a.last_name
    FROM
        film f
            INNER JOIN
        film_actor fa ON f.film_id = fa.film_id
            INNER JOIN
        actor a ON fa.actor_id = a.actor_id
    WHERE
        f.title = 'FARGO GANDHI'
    ORDER BY f.title;
    """
    with connect(host=HOSTNAME, user=USER_NAME, password=PASSWORD) as mysql_connection:
        # Step 2: Create cursor object
        with mysql_connection.cursor() as cursor:
            # Step 3: Execute Query
            query = f"""SELECT
                            f.film_id, f.title, fa.actor_id, a.first_name, a.last_name
                        FROM
                            sakila.film f
                                INNER JOIN
                            sakila.film_actor fa ON f.film_id = fa.film_id
                                INNER JOIN
                            sakila.actor a ON fa.actor_id = a.actor_id
                        WHERE
                            f.title = '{title}'
                        ORDER BY f.title;"""
            cursor.execute(query)
            # Step 4: Fetch all data returned after query execution
            all_actors = cursor.fetchall()
    return all_actors


def get_film_names_by_category(self):
    pass


actors = get_actors_for_movie_by_title("FARGO GANDHI")
print()
for actor in actors:
    print(actor)
