# tested
# can read all the data of movies on the server, ordered by year

# Note: the module name is psycopg, not psycopg3
import psycopg2

# Connect to an existing database
with psycopg2.connect("hostaddr=139.147.9.154 port=5432 dbname=core user=grp1admin") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Query the database and obtain data as Python objects.
        query = "SELECT id, name, year, rank "
        query += "FROM  movies "
        query += "ORDER BY year"

        cur.execute(query)

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()
