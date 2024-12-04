# mostra como inserir um registro em uma tabela a partir do python usando a biblioteca psycopg2.

import psycopg2


# a a conexão com o banco de dados
# Observe os parâmetros da função “connect”, pois é necessário que você crie um banco no PostgreSQL com usuário e senha, conforme escrito na função.
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "postgre123", host = "127.0.0.1", port = "5432")

# É exibida uma mensagem de sucesso para o usuário.
print("Conexão com o Banco de Dados aberta com sucesso!")

# criado o cursor que vai permitir realizar operações no banco de dados.
cur = conn.cursor()

# executado o comando SQL para inserir dados na tabela AGENDA.
# registro é formado pelos seguintes dados: O campo “id” recebe o valor 1, o campo “nome” recebe o valor ‘Pessoa 1’ e, por fim, o campo “telefone” recebe o valor ‘02199999999’.

# uso de aspas simples e duplas.
# No caso do banco de dados PostgreSQL, o nome da tabela e dos campos deve estar entre aspas duplas, por causa disso é que o comando insert possui três aspas duplas logo no início e no final. 
# Sendo assim, muita atenção com isso, pois existem algumas variações conforme o sistema gerenciador de banco de dados escolhido.
cur.execute("""INSERT INTO public."AGENDA" ("id", "nome" , "telefone" ) VALUES (1, 'Pessoa 1' , '02199999999' )""") 

# cutada a função “commit” para confirmar a execução das operações SQL
conn.commit()

print("Inserção realizada com sucesso!"); 

# # fechada a conexão com o banco de dados.
conn.close()