from atproto_client.models.app.bsky.graph.get_followers import Params
from atproto_client import Client
from dotenv import load_dotenv
from pprint import pprint
import os

load_dotenv()

username = os.getenv('BSKY_USERNAME')
password = os.getenv('BSKY_PASSWORD')

# Criação do cliente e login
client = Client()
client.login(username, password)

# Identificador do usuário (actor)
actor = "did:plc:u2o5onxie3yg3t25oufxlhsz"  # Atlético

# Parâmetros para obter os seguidores
params = Params(actor=actor, limit=50)

# Chamada para o endpoint
response = client.app.bsky.graph.get_followers(params=params)
print(response)
