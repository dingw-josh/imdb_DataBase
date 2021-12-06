# read from loging file, check if user do things as its role
import datetime

from connection import queryUpdate2

f = open("loging.log", "r")
file = open("integrity.txt", "w")
for x in f:
    lines = x.split()
    if len(lines) == 11:
        if lines[2] == 'Comment:':
            # comments, all user can make comments
            # so, check whether comment is made by user in table 'comments'
            # check whether comment is made on review in table 'review_comment'
            user = lines[4]
            comment = lines[7]
            review = lines[10]
            result = queryUpdate2("SELECT EXISTS (Select * from comments where commentid = "
                                  + comment + " and userid = " + user + ");")
            if not result[0][0]:
                file.write(str(datetime.datetime.now()) + " ERROR, User " +
                           user + "failed to create comment " + comment + "in table comments.\n")
            else:
                file.write(str(datetime.datetime.now()) + " OK, user "+user+" created comment "+comment + "\n")

        if lines[2] == 'Invitation:':
            # check the user who accomplished invitation
            # check user id and comment id in table 'comments'
            user = lines[5]
            comment = lines[10]
            result = queryUpdate2("SELECT EXISTS (Select * from comments where commentid = "
                                  + comment + " and userid = " + user + ");")
            if not result[0][0]:
                file.write(str(datetime.datetime.now()) + " ERROR, User " +
                           user + "failed to respond to invitation, because there is no created comment " + comment + "in table comments.\n")
            else:
                file.write(str(datetime.datetime.now()) + " OK, user "+user+" successfully created comment "+comment + "\n")
f.close()
