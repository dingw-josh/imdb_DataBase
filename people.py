import datetime
import string
import random
import psycopg2

conn = psycopg2.connect("hostaddr=139.147.9.154 port=5432 dbname=core user=grp1admin")
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
        with conn:
            with conn.cursor() as cur:
                query = "insert into reviews (movieid,content,voteid) values (" + str(self.movieID) + ", \'" +str(self.content) +"\', " + str(vote.voteID)+ ") returning reviewid;"
                cur.execute(query)
                self.reviewID = cur.fetchall()[0][0]
                query = "insert into review_user(reviewid, userid) values (" + str(self.reviewID) + ", " + str(userID) + ");"
                cur.execute(query)
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
        with conn:
            with conn.cursor() as cur:
                query = "insert into votes (userid,engagement,excitement,quality) values (" + str(self.userID) + ", " +str(self.engagement) +", " + str(self.excitement) + ", " + str(self.quality) + ") returning voteid;"
                cur.execute(query)
                self.voteID = cur.fetchall()[0][0]
#
#print("vote id is ", vote.voteID)
