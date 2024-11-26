from atproto_client.models.app.bsky.graph.get_followers import Params
from atproto_client import Client
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('BSKY_USERNAME')
password = os.getenv('BSKY_PASSWORD')

# Criação do cliente e login
client = Client()
client.login(username, password)

# Identificador do usuário (actor)
actor = "did:plc:u2o5onxie3yg3t25oufxlhsz"  # Atlético

# Inicialize os parâmetros com o limite de 100 (máximo permitido pela API)
params = Params(actor=actor, limit=100)

# Lista para armazenar todos os seguidores
all_followers = []

while True:
    # Chamada para o endpoint para obter os seguidores
    response = client.app.bsky.graph.get_followers(params=params)

    # Adiciona os seguidores da página atual à lista de todos os seguidores
    all_followers.extend(response.followers)
    print(f"Quantidade de seguidores obtidos: {len(response.followers)}")
    # Verifica se existe um cursor para a próxima página
    cursor = response.cursor  # Acessa diretamente o atributo 'cursor'
    if cursor:
        # Se houver um cursor, inclui ele nos parâmetros para a próxima requisição
        params.cursor = cursor
    else:
        # Se não houver cursor, significa que todas as páginas foram obtidas
        break

# Imprime o total de seguidores
print(f"Quantidade total de seguidores: {len(all_followers)}")

# Imprimir os dados dos seguidores
# for follower in all_followers:
#     print(f"did = {follower.did}")
#     print(f"handle = {follower.handle}")
#     print(f"associated = {follower.associated}")
#     print(f"avatar = {follower.avatar}")
#     print(f"created_at = {follower.created_at}")
#     print(f"description = {follower.description}")
#     print(f"display_name = {follower.display_name}")
#     print(f"indexed_at = {follower.indexed_at}")
#     print(f"labels = {follower.labels}")
#
#     # Para o campo 'viewer', que é um objeto, podemos acessar seus atributos internos também:
#     print(f"blocked_by = {follower.viewer.blocked_by}")
#     print(f"blocking = {follower.viewer.blocking}")
#     print(f"following = {follower.viewer.following}")
#     print(f"muted = {follower.viewer.muted}")
#     print(f"py_type = {follower.py_type}")
#     print("-" * 40)  # Separando os seguidores para melhor leitura
