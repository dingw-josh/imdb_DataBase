import psycopg2
conn = psycopg2.connect("hostaddr=139.147.9.154 port=5432 dbname=core user=grp1admin")
with conn:
    with conn.cursor() as cur:
        query = "delete from review_user;"
        query += "delete from reviews;"
        query += "delete from votes;"
        query += "delete from users;"
        query += "alter sequence reviews_reviewid_seq restart;"
        query += "alter sequence votes_voteid_seq restart;"
        query += "alter sequence users_userid_seq  restart;"
        cur.execute(query)
