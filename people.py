import datetime
import string
import random
import psycopg2
import string
from connection import getConnection, queryUpdate2, queryUpdate
class People:
    def __init__(self, id:int, firstName: str, lastName: str, userType:str):
        self.userID = id
        self.firstName = firstName
        self.lastName = lastName
        self.userType = userType
    def makeComments(self):
        comment = Comment(self.id,)

class Hired(People):
    def __init__(self, id:int, firstName: str, lastName: str):
        super().__init__(id, firstName, lastName, "Hired")

class User(People):
    def __init__(self, id:int, firstName: str, lastName: str):
        super().__init__(id,firstName, lastName, "User")

class General(People):
    def __init__(self, id:int, firstName: str, lastName: str):
        super().__init__(id,firstName, lastName, "General")

class Comment:
    def __init__(self, commentID:int, userID:int):
        self.commentID = commentID
        self.userID = userID
        self.voteID = voteID
        #random generate the context of the comments
        self.content = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, 100))
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
        print("review id is ",self.reviewID)

 #voteid     | integer |           | not null | nextval('votes_voteid_seq'::regclass)
 #userid     | integer |           | not null |
 #engagement | integer |           | not null | 0
 #excitement | integer |           | not null | 0
 #quality    | integer |           | not null | 0
class Vote:
    def __init__(self, voreID:int, userID:int, engagement:int, excitement:int, quality:int):
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
        #
        #print("vote id is ", vote.voteID)

# commentid | integer                |           | not null | nextval('comments_commentid_seq'::regclass)
# userid    | integer                |           | not null |
 #content   | character varying(100) |           | not null |
class Comment:
    def __init__(self, commentID:int, userID:int):
        self.commentID = commentID
        self.userID = userID
        #random generate the context of the comments
        self.content = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, 100))
        f = open("logs.txt", "a")
        f.write("User %s made a comment with vote %s!====%s\n"%(str(self.userID), str(self.voteID), datetime.datetime.now()))
        f.close()

    def __init__(self, userID:int):
        self.userID = userID
        #random generate the context of the comments
        self.content = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, 100))
        query = "insert into comments (userid, content) values (" + str(self.userID) + ", " + ") returning commentid;"
        self.commentID = queryUpdate2(query)[0][0]
        addLogs("User " + str(self.userID) + "created comment " + str(self.commentID))
