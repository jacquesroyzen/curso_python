from sqlalchemy import select
from core import user_table

selecione = select([user_table])
#selec_where = select([user_table]).where(user_tabele.c.nome=='daniel')


for x in selecione.execute():

    print(x)

print([x for x in selecione.execute()])
print([x for x in selecione_where.execute()])