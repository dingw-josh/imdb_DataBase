from logs import addLogs
from connection import queryUpdate, getConnection


query = "delete from review_user;"
query += "delete from review_comment;"
query += "delete from comments;"
query += "delete from reviews;"
query += "delete from votes;"
query += "delete from users;"

query += "alter sequence reviews_reviewid_seq restart;"
query += "alter sequence votes_voteid_seq restart;"
query += "alter sequence users_userid_seq  restart;"
query += "alter sequence comments_commentid_seq  restart;"
queryUpdate(query)

file = open("loging.log","r+")
file.truncate(0)
file.close()
