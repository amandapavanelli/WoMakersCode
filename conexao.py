import sqlite3
conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# CURSO WOMAKERS - EXERCICIO BANCO DE DADOS

#1.Crie uma tabela de "alunos" com id, nome, idade e curso 
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#2. Insira pelo menos 5 registros de alunos
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(123, "Amanda", 26, "Ciência de Dados")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(456, "Fernando", 32, "Filosofia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(789, "Isabella", 21, "Matemática")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1011, "Rafael", 45, "Gastronomia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1213, "Carolina", 20, "Engenharia Química")')

#3. Consultas básicas
#a. Selecione todos os registros da tabela "alunos"
#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
#    print(alunos) 

#b. Selecione nome e idade dos alunos com mais de 20 anos
#dados = cursor.execute('SELECT * FROM alunos)')
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
#for alunos in dados:
#    print(alunos)

#c. Selecione os alunos do curso de "Engenharia" em ordem alfabética
#dados = cursor.execute('SELECT nome, curso FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
#for alunos in dados:
#    print(alunos)

#d. Conte o número total de alunos na tabela
#dados = cursor.execute('SELECT COUNT(*) FROM alunos')
#for alunos in dados:
#   print(alunos)

#4. Atualização e Remoção
#a. Atualize a idade de um aluno específico na tabela
#cursor.execute('UPDATE alunos SET idade = 28 WHERE id = 123')

#b. Remova um aluno pelo seu ID
#cursor.execute('DELETE FROM alunos WHERE id = 1213')

#5. Crie a tabela "clientes" com os campos: id, nome, idade, saldo
#cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')

#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(012, "Fernanda", 73, 2133)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(013, "Bernardo", 19, 20)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(014, "Ana Maria", 26, 200)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(015, "Enzo", 37, 12000)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(016, "Valentina", 54, 134)')

#6. Consultas e funções agregadas
#a. Selecione nome e idade dos clientes com idade superior a 30 anos
#dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
#for clientes in dados:
#   print(clientes)

#b. Calcule o saldo médio dos clientes
#dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
#for clientes in dados:
#   print(clientes)

#c. Encontro o cliente com saldo máximo
#dados = cursor.execute('SELECT MAX(saldo) FROM clientes')
#for clientes in dados:
#   print(clientes)

#d. Conte quantos clientes têm saldo acima de 1000
#dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo>1000')
#for clientes in dados:
#   print(clientes)

#7. Atualização e remoção com condições
#a. Atualize o saldo de um cliente em específico
#dados = cursor.execute('UPDATE clientes SET saldo = 200 WHERE idade = 37')
#for clientes in dados:
#   print(clientes)

#b. Remova um cliente pelo seu ID
#cursor.execute('DELETE FROM clientes WHERE id = 013')

#8. Junção de tabelas
# Crie uma tabela chamada "compras" com os campos: id, cliente_id, produto e valor
#cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id));')

# Insira algumas compras associadas a clientes existentes na tabela "clientes"
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(28172, 012, "celular", 1200)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(4535, 013, "máquina de lavar", 3000)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(9768, 014, "escova de dente", 30)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(535, 015, "sabão em pó", 21)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1435, 016, "monitor dell", 756)')

# Escreva uma consulta para exibir o nome do cliente, produto e o valor de cada compra
#dados = cursor.execute('SELECT nome, produto, valor FROM clientes JOIN compras ON clientes.id = compras.cliente_id')
#for clientes in dados:
#   print(clientes)

conexao.commit()
conexao.close
