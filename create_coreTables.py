# Note: the module name is psycopg, not psycopg3
from logs import addLogs
from connection import queryUpdate, getConnection, queryUpdate2
import datetime

count = 0;
# Query the database and obtain data as Python objects.
query = "create table movies(id int not null default '0',name varchar(100) default null,year int default null,rank float default null,PRIMARY KEY(id));\n"
query = query + "CREATE TABLE directors( id int NOT NULL default '0', first_name varchar(100) default NULL,last_name varchar(100) default NULL, PRIMARY KEY (id));\n"
query = query + "create TABLE actors(id int default NULL, genre varchar(100) default NULL, PRIMARY KEY (id));\n"
query = query + "create table roles( actor_id int default NULL, moive_id int default NULL, role varchar(100) default NULL, FOREIGN KEY(actor_id) REFERENCES actors(id),FOREIGN KEY(moive_id) REFERENCES movies(id));\n"
query = query + "CREATE TABLE movies_directors( director_id int default NULL, movie_id int default NULL, FOREIGN KEY (director_id) REFERENCES directors(id), FOREIGN KEY (movie_id) REFERENCES movies (id));\n"
query = query + "create TABLE movie_genres(movie_id int default NULL, genre varchar(100) default NULL, FOREIGN KEY (movie_id) REFERENCES movies (id));\n"
query = query + "create TABLE directors_genres(director_id int default NULL, genre varchar(100) default NULL, prob float default NULL,FOREIGN KEY (director_id) REFERENCES directors (id));"
queryUpdate(query)

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'movies');"
result = queryUpdate2(query)
if result[0][0]:
    count += 1
else:
    addLogs("ERROR: failed to create movies table ====%s\n" % (datetime.datetime.now()))

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'directors');"
result = queryUpdate2(query)
if result[0][0]:
    count += 1
else:
    addLogs("ERROR: failed to create directors table ====%s\n" % (datetime.datetime.now()))

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'actors');"
result = queryUpdate2(query)
if result[0][0]:
    count += 1
else:
    addLogs("ERROR: failed to create actors table ====%s\n" % (datetime.datetime.now()))

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'roles');"
result = queryUpdate2(query)
if result[0][0]:
    count += 1
else:
    addLogs("ERROR: failed to create roles table ====%s\n" % (datetime.datetime.now()))

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'movie_genres');"
result = queryUpdate2(query)
if result[0][0]:
    count += 1
else:
    addLogs("ERROR: failed to create movie_genres table ====%s\n" % (datetime.datetime.now()))

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'movies_directors');"
result = queryUpdate2(query)
if result[0][0]:
    count += 1
else:
    addLogs("ERROR: failed to create movies_directors table ====%s\n" % (datetime.datetime.now()))

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'directors_genres');"
result = queryUpdate2(query)
if result[0][0]:
    count += 1
else:
    addLogs("ERROR: failed to create directors_genres table ====%s\n" % (datetime.datetime.now()))

if count == 7:
    addLogs("Created tables for core data. ====%s" % (datetime.datetime.now()))
else:
    addLogs("ERROR: " + str(count) + " core tables made in total, see above for the missing table(s)%s\n" % (
        datetime.datetime.now()))
