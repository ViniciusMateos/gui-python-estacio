import psycopg2

# a a conexão com o banco de dados
# Observe os parâmetros da função “connect”, pois é necessário que você crie um banco no PostgreSQL com usuário e senha, conforme escrito na função.
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "postgre123", host = "127.0.0.1", port = "5432")

# É exibida uma mensagem de sucesso para o usuário.
print("Conexão com o Banco de Dados aberta com sucesso!")

# criado o cursor que vai permitir realizar operações no banco de dados.
cur = conn.cursor()

# consulta na tabela “Agenda” pelo registro com “id” igual a 1, por meio do comando Select do SQL
# executado o comando “delete” do sql que excluirá o registro cujo campo “id” seja igual a “1”.
cur.execute("""Delete from public."AGENDA" where "id"=1""") 
conn.commit() 

# propriedade “rowcount” do “cursor” retorna a quantidade de registros que foram excluídos da tabela “Agenda”.
cont=cur.rowcount 

# impresso na linha de comando o total de registros que foram excluídos.
print(cont, "Registro excluído com sucesso!") 
print("Exclusão realizada com sucesso!"); 

# fechada a conexão com o banco de dados.
conn.close()