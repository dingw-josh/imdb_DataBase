
# can read all the data of movies on the server, ordered by year

# Note: the module name is psycopg, not psycopg3
from logs import addLogs
import datetime
import sys
import random
import string
from random import randrange
from people import Hired, User, General, Vote, Review, Comment
from connection import getConnection, commit, queryUpdate, queryUpdate2
# Connect to an existing database

args = sys.argv
if len(args) == 2:
    query = "SELECT * "
    query += "FROM users where userid = " + str(args[1])
    results = queryUpdate2(query)
else:
    query = "SELECT * FROM users order by random() limit 1"
    results = queryUpdate2(query)


if results[0][3] == "Hired":
    user = Hired(results[0][0], results[0][1],results[0][2])
elif results[0][3] == "User":
    user = User(results[0][0], results[0][1],results[0][2])
else:
    user = General(results[0][0], results[0][1],results[0][2])

if user.userType == "Hired":
    fun_list = [user.makeReview(),user.makeComments(),user.inviteUser(),user.inviteUserSurvey()]
    # rand = randrange(1,5)
    # if rand == 1:
    #     user.makeReview()
    # if rand == 2:
    #     user.makeComments()
    # if rand == 3:
    #     user.inviteUser()
    # if rand == 4:
    #     user.inviteUserSurvey()
    random.choice(fun_list)

if user.userType == "User":
    rand = randrange(1,4)
    if rand == 1:
        user.makeReview()
    if rand == 2:
        user.makeComments()
    if rand == 3:
        user.inviteUserSurvey()

if user.userType == "General":
    user.makeComments()
