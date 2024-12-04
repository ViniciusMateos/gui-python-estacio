import psycopg2

# a a conexão com o banco de dados
# Observe os parâmetros da função “connect”, pois é necessário que você crie um banco no PostgreSQL com usuário e senha, conforme escrito na função.
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "postgre123", host = "127.0.0.1", port = "5432")

# É exibida uma mensagem de sucesso para o usuário.
print("Conexão com o Banco de Dados aberta com sucesso!")

# criado o cursor que vai permitir realizar operações no banco de dados.
cur = conn.cursor()

# Uma consulta antes da atualização que mostra os dados do registro antes de serem modificados.
print("Consulta antes da atualização") 
cur.execute("""select * from public."AGENDA" where "id"=1""") 
registro=cur.fetchone() 
print(registro) 

#Atualização de um único registro 
# executado o comando “update” do sql, que atualizará o dado do campo “telefone” do registro, cujo campo “id” contenha o valor “1”.
cur.execute("""Update public."AGENDA" set "telefone"='02188888888' where "id"=1""") 
conn.commit() 
print("Registro Atualizado com sucesso! ")

cur = conn.cursor()

# consulta depois da atualização do registro que mostra como ficaram os dados do registro depois de serem atualizados.
print(" Consulta depois da atualização") 
cur.execute("""select * from public."AGENDA" where "id"=1""") 
registro=cur.fetchone() 
print(registro) 

# cutada a função “commit” para confirmar a execução das operações SQL
conn.commit()

print("Seleção realizada com sucesso!")

# # fechada a conexão com o banco de dados.
conn.close()