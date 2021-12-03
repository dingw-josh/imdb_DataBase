# tested
# can read all the data of movies on the server, ordered by year

# Note: the module name is psycopg, not psycopg3
import psycopg2
from connection import getConnection, queryUpdate, queryUpdate2
# Connect to an existing database

        # Query the database and obtain data as Python objects.
query = "SELECT id, name, year, rank "
query += "FROM  movies "
query += "ORDER BY year"

results = queryUpdate2(query)

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
for record in results:
    print(record)
