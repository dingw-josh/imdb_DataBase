# Note: the module name is psycopg, not psycopg3
from connection import getConnection, queryUpdate2, queryUpdate
from logs import addLogs

        # Query the database and obtain data as Python objects.
query = "drop table movies_directors;\n"
query = query + "drop table directors_genres;\n"
query = query + "drop table movie_genres;\n"
query = query + "drop table roles;\n"
query = query + "drop table actors;\n"
query = query + "drop table directors;\n"
query = query + "drop table movies;\n"
queryUpdate(query)
addLogs("drop core tables")

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        #for record in cur:
        #    print(record)

        # Make the changes to the database persistent
