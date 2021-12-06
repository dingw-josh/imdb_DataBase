# read from loging file, check if user do things as its role
import datetime

from connection import queryUpdate2

f = open("loging.log", "r")
file = open("integrity.txt", "w")
total_lines = 0
failed = 0
success = 0
for x in f:
    total_lines += 1
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
                           user + " failed to create comment " + comment + " in table comments.\n")
                failed += 1
            else:
                file.write(str(datetime.datetime.now()) + " OK, user " + user + " created comment " + comment + "\n")
                success += 1

        elif lines[2] == 'Invitation:':
            # check the user who accomplished invitation
            # check user id and comment id in table 'comments'
            user = lines[5]
            comment = lines[10]
            result = queryUpdate2("SELECT EXISTS (Select * from comments where commentid = "
                                  + comment + " and userid = " + user + ");")
            if not result[0][0]:
                file.write(str(datetime.datetime.now()) + " ERROR, User " +
                           user + " failed to respond to invitation, because there is no created comment " + comment + " in table comments.\n")
                failed += 1
            else:
                file.write(str(
                    datetime.datetime.now()) + " OK, user " + user + " successfully responded to invitation by creating comment " + comment + "\n")
                success += 1

        elif lines[2] == 'Survey:':
            owner = lines[4]
            survey = lines[7]
            movie = lines[10]
            result = queryUpdate2("Select Exists (Select * from surveys where userid = " + owner +
                                  " and movieid = " + movie + " and surveyid = " + survey + ");")
            if not result[0][0]:
                file.write(str(datetime.datetime.now()) + " ERROR, User " +
                           lines[5] + " failed to invite user " + owner + " to fill the survey " + survey + ".\n")
                failed += 1
            else:
                file.write(str(datetime.datetime.now()) + " OK, user " + owner + " created survey " + survey + "\n")
                success += 1

    if len(lines) == 9:
        if lines[2] == 'Review:':
            # check if the user created a review in table review_user
            user = lines[4]
            review = lines[8]
            result = queryUpdate2("SELECT EXISTS (Select * from review_user where reviewid = " + review
                                  + " and userid = " + user + ");")
            if not result[0][0]:
                file.write(str(datetime.datetime.now()) + " ERROR, User " +
                           user + " failed to create a review " + review + "in table reviews.\n")
                failed += 1
            else:
                file.write(str(
                    datetime.datetime.now()) + " OK, user " + user + " successfully created a review " + review + "\n")
                success += 1
    if len(lines) == 15:
        if lines[2] == 'Invite:':
            # check if there is any comment in comments table that correpond with user id
            # with comment and review together, check if there is a match in review_comment table
            user = lines[8]
            review = lines[14]
            result = queryUpdate2("SELECT EXISTS (Select * from review_comment " +
                                  "where commentid = " +
                                  "(Select commentid from comments where userid = " + user + ")"
                                  + " and reviewid = " + review + ");")
            if not result[0][0]:
                file.write(str(datetime.datetime.now()) + " ERROR, User " +
                           lines[
                               5] + " failed to invite user " + user + " to create a comment on review " + review + ".\n")
                failed += 1
            else:
                file.write(str(
                    datetime.datetime.now()) + " OK, user " + user + " was invited to created a comment on review " + review + "\n")
                success += 1
    if len(lines) == 12:
        if lines[2] == 'Vote:':
            user = lines[4]
            vote = lines[8]
            survey = lines[11]
            result = queryUpdate2(
                "Select Exists (Select * from survey_vote where voteid = " + vote + " and surveyid = " + survey + ");")
            if not result[0][0]:
                file.write(str(datetime.datetime.now()) + " ERROR, User " +
                           user + " failed to vote on the survey " + survey + ", because there it is not in survey_vote.\n")
                failed += 1
            else:
                result = queryUpdate2("Select Exists (Select * from votes where voteid = " + vote
                                      + " and userid = " + user + ");")
                if not result[0][0]:
                    file.write(str(datetime.datetime.now()) + " ERROR, User " +
                           user + " failed to vote on the survey " + survey + ", because user did not create such a vote.\n")
                    failed += 1

                else:
                    file.write(str(datetime.datetime.now()) + " OK, user " + user + " successfully created a vote on survey " + survey + "\n")
                    success += 1

#
# if len(lines) == :
#     if lines[2] == 'Voted:':
#         user = lines[ ]
#         survey = lines[ ]
#         vote = lines[ ]
#         result = queryUpdate2()
file.write("Total lines from log checked: " + str(total_lines) +
        ". The number of successful tasks is " + str(success) +
        ". The number of failed task is " + str(failed) + ".")

file.close()
f.close()
