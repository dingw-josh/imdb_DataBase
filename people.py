import datetime
import string
import random
import psycopg2
import string
from connection import getConnection, queryUpdate2, queryUpdate
from logs import addLogs
class People:
    def __init__(self, id:int, firstName: str, lastName: str, userType:str):
        self.userID = id
        self.firstName = firstName
        self.lastName = lastName
        self.userType = userType

    def makeComments(self):
        query = "SELECT reviewid FROM reviews order by random() limit 1"
        results = queryUpdate2(query)
        if results:
            comment = Comment(self.userID, results[0][0])
        else:
            print("no REVIEW: ")
    def invitedComment(self,reviewID):
        pass

    def makeVote(self):
        query = "SELECT voteid FROM votes order by random() limit 1"
        results = queryUpdate2(query)
        if results:
            vote = Vote(self.userID, results[0][0])
        else:
            print("no VOTE: ")

class Hired(People):
    def __init__(self, id:int, firstName: str, lastName: str):
        super().__init__(id, firstName, lastName, "Hired")
    def makeReview(self):
        query = "SELECT id FROM movies order by random() limit 1"
        results = queryUpdate2(query)
        content = ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))
        review = Review(results[0][0],content, self.userID)
        addLogs("Review: User " + str(self.userID) +" created a review " + str(review.reviewID))

    def invitedComment(self,reviewID):
        comment = Comment(self.userID, reviewID)

        print(self.userType +" User " + str(self.userID) + " accomplished invitation by comment "+str(comment.commentID))
        addLogs("Invitation: " + self.userType +" User " + str(self.userID) + " accomplished invitation by comment " + str(comment.commentID))

    def makeComments(self):
        query = "SELECT reviewid FROM reviews order by random() limit 1"
        results = queryUpdate2(query)
        if results:
            comment = Comment(self.userID, results[0][0])
        else:
            print("no REVIEW: ")

    def inviteUser(self):
        query = "select reviewid from review_user where userid = " + str(self.userID) +" order by random() limit 1"
        results = queryUpdate2(query)
        if results:
            reviewID = results[0][0]
            query = "SELECT * FROM users order by random() limit 1"
            results = queryUpdate2(query)
            if results:
                if results[0][3] == "Hired":
                    temp = Hired(results[0][0], results[0][1],results[0][2])
                elif results[0][3] == "User":
                    temp = User(results[0][0], results[0][1],results[0][2])
                else:
                    temp = General(results[0][0], results[0][1],results[0][2])

                temp.invitedComment(reviewID)
                print(self.userType +" User " + str(self.userID) + " invited user " + str(temp.userID) + " to make a comment on " + str(reviewID))
                addLogs("Invite: "+self.userType +" User " + str(self.userID) + " invited user " + str(temp.userID) + " to make a comment on " + str(reviewID))
        else:
            print("there is no record in review_user")


    def invitedSurvey(self,surveyID):
        vote = Vote(self.userID)
        query = "insert into survey_vote (surveyid, voteid) values (" + str(surveyID) +", " + str(vote.voteID) + ")"
        queryUpdate(query)


    def inviteUserSurvey(self):
        query = "select id from movies order by random() limit 1"
        results = queryUpdate2(query)
        survey = Survey(self.userID, results[0][0] )
        if results:
            #surveyID = results[0][0]
            query = "SELECT * FROM users order by random() limit 5"
            results = queryUpdate2(query)
            if results:
                for lp in range(1,5):
                    if results[0][3] == "Hired":
                        temp = Hired(results[lp][0], results[lp][1],results[lp][2])
                    elif results[0][3] == "User":
                        temp = User(results[lp][0], results[lp][1],results[lp][2])
                    else:
                        temp = General(results[lp][0], results[lp][1],results[lp][2])
                    temp.invitedSurvey(survey.surveyID)
                    print(self.userType +" User " + str(self.userID) + " invited user " + str(temp.userID) + " to make a survey on " + str(survey.surveyID))


class User(People):
    def __init__(self, id:int, firstName: str, lastName: str):
        super().__init__(id,firstName, lastName, "User")
    def makeReview(self):
        query = "SELECT id FROM movies order by random() limit 1"
        results = queryUpdate2(query)
        content = ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))
        review = Review(results[0][0],content, self.userID)
        addLogs("Review: User " + str(self.userID) +" created a review " + str(review.reviewID))

    def invitedComment(self,reviewID):
        comment = Comment(self.userID, reviewID)
        print(self.userType +" User " + str(self.userID) + " accomplished invitation by comment "+str(comment.commentID))
        addLogs("Invitation: "+ self.userType +" User " + str(self.userID) + " accomplished invitation by comment " + str(comment.commentID))

    def makeComments(self):
        query = "SELECT reviewid FROM reviews order by random() limit 1"
        results = queryUpdate2(query)
        if results:
            comment = Comment(self.userID, results[0][0])
        else:
            print("no REVIEW: ")

    def invitedSurvey(self,surveyID):
        vote = Vote(self.userID)
        query = "insert into survey_vote (surveyid, voteid) values (" + str(surveyID) +", " + str(vote.voteID) + ")"
        queryUpdate(query)


    def inviteUserSurvey(self):
        query = "select id from movies order by random() limit 1"
        results = queryUpdate2(query)
        survey = Survey(self.userID, results[0][0])
        if results:
            #surveyID = results[0][0]
            query = "SELECT * FROM users order by random() limit 5"
            results = queryUpdate2(query)
            if results:
                for lp in range(1,5):
                    if results[0][3] == "Hired":
                        temp = Hired(results[lp][0], results[lp][1],results[lp][2])
                    elif results[0][3] == "User":
                        temp = User(results[lp][0], results[lp][1],results[lp][2])
                    else:
                        temp = General(results[lp][0], results[lp][1],results[lp][2])
                    temp.invitedSurvey(survey.surveyID)
                    print(self.userType +" User " + str(self.userID) + " invited user " + str(temp.userID) + " to make a survey on " + str(survey.surveyID))


class General(People):
    def __init__(self, id:int, firstName: str, lastName: str):
        super().__init__(id,firstName, lastName, "General")

    def invitedComment(self,reviewID):
        comment = Comment(self.userID, reviewID)


        print(self.userType +" User " + str(self.userID) + " accomplished invitation by comment "+str(comment.commentID))
        addLogs("Invitation: "+ self.userType +" User " + str(self.userID) + " accomplished invitation by comment " + str(comment.commentID))

    def makeComments(self):
        query = "SELECT reviewid FROM reviews order by random() limit 1"
        results = queryUpdate2(query)
        if results:
            comment = Comment(self.userID, results[0][0])
        else:
            print("no REVIEW: ")

    def invitedSurvey(self,surveyID):
        vote = Vote(self.userID)
        query = "insert into survey_vote (surveyid, voteid) values (" + str(surveyID) +", " + str(vote.voteID) + ")"
        queryUpdate(query)
        addLogs("Vote: User " + str(self.userID) + " created a vote " + str(vote.voteID) + " on survey " + str(surveyID))

# reviewid | integer                |           | not null |
# movieid  | integer                |           | not null |
# content  | character varying(100) |           | not null |
# voteid
class Review:
    def __init__(self, reviewID:int, movieID:int, content:str, voteID:int):
        self.reviewID = reviewID
        self.movieID = movieID
        self.content = content
        self.voteID = voteID

    def __init__(self, movieID:int, content:str,userID:int):
        self.movieID = movieID
        self.content = content
        vote = Vote(userID)
        query = "insert into reviews (movieid,content,voteid) values (" + str(self.movieID) + ", \'" +str(self.content) +"\', " + str(vote.voteID)+ ") returning reviewid;"
        results = queryUpdate2(query)
        self.reviewID = results[0][0]
        query = "insert into review_user(reviewid, userid) values (" + str(self.reviewID) + ", " + str(userID) + ");"
        queryUpdate(query)
        print("User " + str(userID) +" created review " + str(self.reviewID) + " on movie " + str(movieID))

 #voteid     | integer |           | not null | nextval('votes_voteid_seq'::regclass)
 #userid     | integer |           | not null |
 #engagement | integer |           | not null | 0
 #excitement | integer |           | not null | 0
 #quality    | integer |           | not null | 0
class Vote:
    def __init__(self, voteID:int, userID:int, engagement:int, excitement:int, quality:int):
        self.voteID = voteID
        self.userID = userID
        self.engagement = engagement
        self.excitement = excitement
        self.quality = quality
    def __init__(self, userID:int):
        self.userID = userID
        self.engagement = random.randint(0,10)
        self.excitement = random.randint(0,10)
        self.quality = random.randint(0,10)
        query = "insert into votes (userid,engagement,excitement,quality) values (" + str(self.userID) + ", " +str(self.engagement) +", " + str(self.excitement) + ", " + str(self.quality) + ") returning voteid;"
        results = queryUpdate2(query)
        self.voteID = results[0][0]

        #print("vote id is ", vote.voteID)

# commentid | integer                |           | not null | nextval('comments_commentid_seq'::regclass)
# userid    | integer                |           | not null |
 #content   | character varying(100) |           | not null |
class Comment:
    # def __init__(self, commentID:int, userID:int):
    #     self.commentID = commentID
    #     self.userID = userID
    #     #random generate the context of the comments
    #     self.content = ''.join(random.choices(string.ascii_uppercase +
    #                          string.digits, 100))
    #     f = open("logs.txt", "a")
    #     f.write("User %s made a comment with vote %s!====%s\n"%(str(self.userID), str(self.voteID), datetime.datetime.now()))
    #     f.close()

    def __init__(self, userID:int, reviewID:int):
        self.userID = userID
        self.reviewID = reviewID
        #random generate the context of the comments
        conn = getConnection()
        with conn.cursor() as cur:
                self.content = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k =20))
                query = "insert into comments (userid, content) values (" + str(self.userID) +", \'" +self.content + "\') returning commentid;"
                cur.execute(query)
                self.commentID = cur.fetchall()[0][0]
                query = "insert into review_comment (reviewid, commentid) values (" + str(self.reviewID) +", " + str(self.commentID) + ")"
                cur.execute(query)
                conn.commit()
        addLogs("Comment: User " + str(self.userID) + " created comment " + str(self.commentID) + " on review " + str(self.reviewID))
        print("User " + str(self.userID) + " created comment " + str(self.commentID) + " on review " + str(self.reviewID))

class Survey:
    def __init__(self, surveyID:int,userID:int,movieID:int):
        self.surveyID = surveyID
        self.userID = userID
        self.movieID = movieID
        addLogs("Survey: User %s made a survey with vote %s!====%s\n"%(str(self.userID), str(self.voteID), datetime.datetime.now()))


    def __init__(self, userID:int, movieID:int):
        self.userID = userID
        self.movieID = movieID
        conn = getConnection()
        with conn.cursor() as cur:
            query = "insert into surveys (userid, movieid) values (" + str(self.userID) +", \'" +str(self.movieID) + "\') returning surveyid;"
            cur.execute(query)
            self.surveyID = cur.fetchall()[0][0]
            # query = "insert into survey_vote (surveyid, voteid) values (" + str(self.surveyID) +", " + str(self.voteID) + ")"
            # cur.execute(query)
            conn.commit()
        addLogs("Survey: User " + str(self.userID) + " created survey " + str(self.surveyID) + " on movie " + str(self.movieID))
        print("User " + str(self.userID) + " created survey " + str(self.surveyID) + " on movie " + str(self.movieID))
