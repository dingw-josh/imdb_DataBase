# tested
# can read all the data of movies on the server, ordered by year

# Note: the module name is psycopg, not psycopg3
from random import randrange
import names
import datetime
from connection import getConnection, commit, queryUpdate
from logs import addLogs
    # Open a cursor to perform database operations
for i in range(0,99):

    rand = randrange(1,4)
    firstName = names.get_first_name()
    lastName = names.get_last_name()
    if rand == 1:
        query = "insert into users ( firstname, lastname, usertype) values (" +  " \'"+ str(firstName) +"\',\'"  + str(lastName) + "\', \'Hired\' );"
    elif rand == 2:
        query = "insert into users ( firstname, lastname, usertype)  values (" +   "\'"+ str(firstName) +"\',\'"  + str(lastName) + "\', \'User\' );"
    else:
        query = "insert into users ( firstname, lastname, usertype)  values ("  +   "\'"+ str(firstName) +"\',\'"  + str(lastName) + "\', \'General\');"

    queryUpdate(query)
    addLogs("initializing User data! ====%s\n"%( datetime.datetime.now()))
