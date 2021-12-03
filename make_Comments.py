import datetime
import string
import random

class Comment:
    def __init__(self, commentID:int, userID:int):
        self.commentID = commentID
        self.userID = userID
        self.voteID = voteID
        #random generate the context of the comments
        self.content = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, 100))
        f = open("logs.txt", "a")
        f.write("User %s made a comment with vote %s!====%s\n"%(str(self.userID), str(self.voteID), datetime.datetime.now()))
        f.close()
