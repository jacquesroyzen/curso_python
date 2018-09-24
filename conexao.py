import psycopg2

try:
    con = psycopg2.connect('host=127.0.0.1 dbname=curso user=jroyzen password=mypw01nt')
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

cur  = con.cursor()
cur.execute("select * from usuarios2;")
var = cur.fetchall()
for x in var:
    print('id:{} nome:{} idade:{}'.format(x[0], x[1],x[2]))
# print(cur.fetchone())
con.commit()
cur.close()
con.close()
#vagrant rsync-auto
# cur.execute("update usuarios set nome='daniel' where id = 1;")
