# Note: the module name is psycopg, not psycopg3
import psycopg2

# Connect to an existing database
with psycopg2.connect("hostaddr=139.147.9.154 port=5432 dbname=core user=grp1admin") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Query the database and obtain data as Python objects.
        query = "create table movies(id int not null default '0',name varchar(100) default null,year int default null,rank float default null,PRIMARY KEY(id));\n"
        query = query + "CREATE TABLE directors( id int NOT NULL default '0', first_name varchar(100) default NULL,last_name varchar(100) default NULL, PRIMARY KEY (id));\n"
        query = query +"create TABLE actors(id int default NULL, genre varchar(100) default NULL, PRIMARY KEY (id));\n"
        query = query +"create table roles( actor_id int default NULL, moive_id int default NULL, role varchar(100) default NULL, FOREIGN KEY(actor_id) REFERENCES actors(id),FOREIGN KEY(moive_id) REFERENCES movies(id));\n"
        query = query +"CREATE TABLE movies_directors( director_id int default NULL, movie_id int default NULL, FOREIGN KEY (director_id) REFERENCES directors(id), FOREIGN KEY (movie_id) REFERENCES movies (id));\n"
        query = query +"create TABLE movie_genres(movie_id int default NULL, genre varchar(100) default NULL, FOREIGN KEY (movie_id) REFERENCES movies (id));\n"
        query = query +"create TABLE directors_genres(director_id int default NULL, genre varchar(100) default NULL, prob float default NULL,FOREIGN KEY (director_id) REFERENCES directors (id));"
        cur.execute(query)

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        #for record in cur:
        #    print(record)

        # Make the changes to the database persistent
        conn.commit()
