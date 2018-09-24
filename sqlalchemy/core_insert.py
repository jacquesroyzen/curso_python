from core import user_table, engine

con = engine.connect()
ins = user_table.insert()

#insere um a um
# new = ins.values(idade=24, nome='daniel', senha='123@mudar')
# con.execute(new)

con.execute(user_table.insert(),[
    {'nome':'marcio', 'idade':20, 'senha':'hao123'},
    {'nome':'joa', 'idade':30, 'senha':'windows'},
    {'nome':'pedro', 'idade':17, 'senha':'baidu'},
])