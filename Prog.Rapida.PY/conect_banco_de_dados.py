import dataset

db = dataset.connect('sqlite:///:memory:')

table = db['usuario']
table.insert(dict(name='rafael dantas', idade=22))
table.insert(dict(name='Bruna leao', idade=24))

table.update(dict(nome='Bruna leao',idade=24),['name'])

usuarios= db['usuario'].all()

for usuario in db['usuario']:
    print(usuario['name']) 

