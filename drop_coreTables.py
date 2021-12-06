# Note: the module name is psycopg, not psycopg3
from connection import getConnection, queryUpdate2, queryUpdate
from logs import addLogs
import datetime
import init_500Users

count = 0
        # Query the database and obtain data as Python objects.
query = "drop table movies_directors;\n"
query = query + "drop table directors_genres;\n"
query = query + "drop table movie_genres;\n"
query = query + "drop table roles;\n"
query = query + "drop table actors;\n;"
query = query + "drop table directors;\n"
query = query + "drop table movies;\n"
queryUpdate(query)

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'movies');"
result = queryUpdate2(query)
if result[0][0]:
    print(result[0][0])
    addLogs("ERROR: failed to drop movies table ====%s\n" % (datetime.datetime.now()))
else:
    count += 1

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'directors');"
result = queryUpdate2(query)
if result[0][0]:
    addLogs("ERROR: failed to drop directors table ====%s\n" % (datetime.datetime.now()))
else:
    count += 1

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'actors');"
result = queryUpdate2(query)
if result[0][0]:
    addLogs("ERROR: failed to drop actors table ====%s\n" % (datetime.datetime.now()))
else:
    count += 1

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'roles');"
result = queryUpdate2(query)
if result[0][0]:
    addLogs("ERROR: failed to drop roles table ====%s\n" % (datetime.datetime.now()))
else:
    count += 1

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'movie_genres');"
result = queryUpdate2(query)
if result[0][0]:
    addLogs("ERROR: failed to drop movie_genres table ====%s\n" % (datetime.datetime.now()))
else:
    count += 1

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'movies_directors');"
result = queryUpdate2(query)
if result[0][0]:
    addLogs("ERROR: failed to drop movies_directors table ====%s\n" % (datetime.datetime.now()))
else:
    count += 1

query = "SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'directors_genres');"
result = queryUpdate2(query)
if result[0][0]:
    addLogs("ERROR: failed to drop directors_genres table ====%s\n" % (datetime.datetime.now()))
else:
    count += 1


if count == 7:
    addLogs("Dropped core tables ====%s" % (
        datetime.datetime.now()))
else:
    addLogs("ERROR: " + str(count) + " core tables dropped in total, see above for the table(s) still exist ====%s\n" % (
        datetime.datetime.now()))



        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        #for record in cur:
        #    print(record)

        # Make the changes to the database persistent
