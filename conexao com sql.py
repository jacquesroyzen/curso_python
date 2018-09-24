#!/usr/bin/python3
import psycopg2

try:
    con = psycopg2.connect('host=127.0.0.1 dbname=projeto user=admin passord=4linux')
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

cur = con.cursor()
cur.execute("update usuarios set nome='daniel' where id = 1;")
con.commit()
cur.close()
con.close()
#vagrant rsync-auto
