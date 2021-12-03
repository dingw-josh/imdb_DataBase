import datetime
import string
import random
# reviewid | integer                |           | not null |
# movieid  | integer                |           | not null |
# content  | character varying(100) |           | not null |
# voteid

class Review:
    def __init__(self, reviewID:int):
        self.commentID = commentID
        self.userID = userID
        self.voteID = voteID
        #random generate the context of the comments
        self.content = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, 100))
