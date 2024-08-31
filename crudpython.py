import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'teste',
    password = 'teste',
    database = 'bdcrudpython',
)

##Executa os comandos da conexão
cursor = conexao.cursor() #para iniciar a conexão

#CREATE
nome_produto = "Pastel"
valor = 5
comando = f'INSERT INTO produtos (nome_produto valor) VALUES ("{nome_produto}", {valor})' #O id do produto não precisa ser passado porque ao criar a tabela, coloquei como autoincrement
cursor.execute(comando)
conexao.commit() #para editar algo do banco de dados

#READ
comando = f'SELECT * FROM bdcrudpython.produtos'
cursor.execute(comando)
resultado = cursor.fetchall() #para ler o banco de dados 
print(resultado)
 
#UPDATE
valor = 6
id_produto = 3
comando = f'UPDATE produtos SET valor = {valor} WHERE id_produto = {id_produto}'
cursor.execute(comando)
conexao.commit() #para editar algo do banco de dados

#DELETE
nome_produto = "Coxinha"
comando = f'DELETE FROM produtos WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #para editar algo do banco de dados

cursor.close() #esse comando encerra a conexão 
conexao.close() #esse comando encerra a conexão 