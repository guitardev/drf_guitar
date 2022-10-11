import psycopg2
conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="postgres")
cur = conn.cursor()
cur.execute('SELECT * FROM blog_post')

