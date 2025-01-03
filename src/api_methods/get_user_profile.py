from atproto import Client
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    # Obter as credenciais do arquivo .env
    username = os.getenv('BSKY_USERNAME')
    password = os.getenv('BSKY_PASSWORD')

    # Criação do cliente e login
    client = Client()
    client.login(username, password)

    # Handle do usuário cujo perfil você deseja buscar
    user_handle = 'litona.bsky.social'
    profile = client.get_profile(user_handle)

    # Exibe as informações do perfil
    print("User Profile:")
    print(f"Display Name: {profile.display_name or 'N/A'}")
    print(f"Description: {profile.description or 'N/A'}")
    print(f"Handle: {profile.handle or 'N/A'}")
    print(f"Followers Count: {profile.followers_count or 'N/A'}")
    print(f"Following Count: {profile.follows_count or 'N/A'}")
    print(f"Posts Count: {profile.posts_count or 'N/A'}")
    print(f"Avatar URL: {profile.avatar or 'N/A'}")
    print(f"Banner URL: {profile.banner or 'N/A'}")
    print(f"DID: {profile.did or 'N/A'}")


if __name__ == '__main__':
    main()
