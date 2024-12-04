# como criar uma tabela a partir do python

import psycopg2

# a a conexão com o banco de dados
# Observe os parâmetros da função “connect”, pois é necessário que você crie um banco no PostgreSQL com usuário e senha, conforme escrito na função.
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "postgre123", host = "127.0.0.1", port = "5432")

# É exibida uma mensagem de sucesso para o usuário.
print("Conexão com o Banco de Dados aberta com sucesso!")

# criado o cursor que vai permitir realizar operações no banco de dados.
cur = conn.cursor()

# Executa o comando SQL para criar a tabela “Agenda” com os campos “ID”, “Nome” e “Telefone”.
cur.execute('''CREATE TABLE Agenda(ID INT PRIMARY KEY NOT NULL,Nome TEXT NOT NULL,Telefone CHAR(12));''')

# exibida uma mensagem de criação da tabela com sucesso
print("Tabela criada com sucesso!")

# cutada a função “commit” para confirmar a execução das operações SQL
conn.commit()

# fechada a conexão com o banco de dados.
conn.close()