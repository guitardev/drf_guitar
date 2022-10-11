import psycopg2
conn = psycopg2.connect(
    host="db",
    dbname="postgres",
    user="postgres",
    password="postgres")
cur = conn.cursor()
cur.execute('SELECT * FROM notes')