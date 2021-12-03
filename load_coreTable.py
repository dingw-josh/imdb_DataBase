# Note: the module name is psycopg, not psycopg3
import psycopg2

# Connect to an existing database
with psycopg2.connect("hostaddr=139.147.9.154 port=5432 dbname=core user=postgres") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        # Query the database and obtain data as Python objects.
        query = "COPY" + " movies FROM '/home/grpqadmin/csvData/imdb_movies.csv' WITH DELIMITER',' CSV QUOTE '''' ESCAPE '\\' NULL as 'NULL';\n"
        #query = query + "copy directors FROM '/home/grp1admin/csvData/imdb_directors.csv' WITH DELIMITER',' CSV QUOTE '''' ESCAPE '\';\n"
        #query = query + "copy movie_genres from '/home/grp1admin/csvData/imdb_movies_genres.csv' with DELIMITER',' NULL '0.0';\n"
        #query = query + "copy actors FROM '/home/grp1admin/csvData/imdb_actors.csv' WITH DELIMITER',' CSV QUOTE '''' ESCAPE '\';\n"
        #query = query + "copy roles FROM '/home/grp1admin/csvData/imdb_roles.csv' WITH DELIMITER',' CSV QUOTE '''' ESCAPE '\';\n"
        #query = query + "copy directors_genres FROM '/home/grp1admin/csvData/imdb_directors_genres.csv' WITH DELIMITER',' CSV QUOTE '''' ESCAPE '\';\n"
        #query = query + "copy movies_directors FROM '/home/grp1admin/csvData/imdb_movies_directors.csv' WITH DELIMITER',' CSV QUOTE '''' ESCAPE '\';\n"
        cur.execute(query)

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        #for record in cur:
        #    print(record)

        # Make the changes to the database persistent
        conn.commit()
