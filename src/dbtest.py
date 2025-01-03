from pymongo import MongoClient

# Conexão com o MongoDB na porta padrão (localhost)
client = MongoClient("mongodb://localhost:27017/")

# Selecionar o banco de dados
db = client["bsky"]

# Selecionar uma coleção
collection = db["bskyapi"]

print("Conexão estabelecida com sucesso!")
