import psycopg2


# a a conexão com o banco de dados
# Observe os parâmetros da função “connect”, pois é necessário que você crie um banco no PostgreSQL com usuário e senha, conforme escrito na função.
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "postgre123", host = "127.0.0.1", port = "5432")

# É exibida uma mensagem de sucesso para o usuário.
print("Conexão com o Banco de Dados aberta com sucesso!")

# criado o cursor que vai permitir realizar operações no banco de dados.
cur = conn.cursor()

# feita a consulta na tabela “Agenda” pelo registro com “id” igual a 1, por meio do comando Select do SQL.
cur.execute("""select * from public."AGENDA" where "id"=1""") 

# executado o método “fetchone” que recupera exatamente um registro do “cursor” e atribui para a variável “registro”.
registro=cur.fetchone() 

# impresso na linha de comando o resultado da consulta armazenado na variável “registro”.
print(registro) 

# cutada a função “commit” para confirmar a execução das operações SQL
conn.commit()

print("Seleção realizada com sucesso!"); 

# # fechada a conexão com o banco de dados.
conn.close()