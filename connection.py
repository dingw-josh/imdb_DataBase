import psycopg2

with psycopg2.connect("hostaddr=139.147.9.154 port=5432 dbname=core user=grp1admin") as conn:
    def getConnection():
        return conn
#        with conn.cursor() as cur:
#            return cur
    def queryUpdate(query:str):
        with conn.cursor() as cur:
            cur.execute(query)
            return cur
    def queryUpdate2(query:str):
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
            return cur.fetchall()

    def commit():
        conn.commit()
