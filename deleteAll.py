import psycopg2
conn = psycopg2.connect("hostaddr=139.147.9.154 port=5432 dbname=core user=grp1admin")
with conn:
    with conn.cursor() as cur:
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
        cur.execute(query)

file = open("loging.log","r+")
file.truncate(0)
file.close()
