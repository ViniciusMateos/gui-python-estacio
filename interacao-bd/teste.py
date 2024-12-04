import psycopg2 

# lista de três carros, na qual cada carro possui um código de identificação, um nome e um preço.

carros = (
(1, 'Celta', 35000),
(2, 'Fusca', 30000),
(3, 'Fiat Uno', 32000)
)

# conexão com o banco de dados “BancoExemplo”
con = psycopg2.connect(database='BancoExemplo', user='postgres',
       password='postgres')

# cursor que será usado para realizar as operações sobre o banco de dados
cursor = con.cursor()


query = "INSERT INTO cars (id, nome, preco) VALUES (%s, %s, %s)"

# executada a rotina “executemany”, sendo que ela recebe uma query e uma lista de carros que serão inseridos no banco de dados.
cursor.executemany(query, carros)