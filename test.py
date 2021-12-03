# I was trying to read all the data from csv file and then upload then to the server database
# Note: the module name is psycopg, not psycopg3
import psycopg2
import csv

filename = "~/Desktop/csvData/imdb_movies.csv"

with open(fileName, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
# Connect to an existing database
with psycopg2.connect("hostaddr=139.147.9.154 port=5432 dbname=core user=grp1admin") as conn:
# initializing the titles and rows list
    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Query the database and obtain data as Python objects.

        query=("INSERT INTO movies(id,name, year, rank) VALUES(1,  'a',  1990,  NULL);")
        cur.execute(query)

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor

        # Make the changes to the database persistent
        conn.commit()
