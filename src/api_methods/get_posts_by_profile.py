from atproto import Client
import os
from dotenv import load_dotenv
from pprint import pprint
import time  # Para adicionar delays entre chamadas, se necessário

load_dotenv()

def fetch_posts(client, actor_did, filter_type, page_limit=10, max_pages=5):
    cursor = None  # Cursor inicial vazio
    pages_fetched = 0

    while pages_fetched < max_pages:
        # Faz a chamada para buscar os posts
        data = client.get_author_feed(
            actor=actor_did,
            filter=filter_type,
            limit=page_limit,
            cursor=cursor
        )

        # Processa os posts retornados
        feed = data.feed
        if not feed:
            print("Nenhum post encontrado nesta página. Encerrando busca.")
            break

        for post in feed:
            print("_" * 150)
            print("Post number:", feed.index(post) + 1 + pages_fetched * page_limit)
            # Navegando diretamente pelos campos
            author = post.post.author
            record = post.post.record
            embed = getattr(post.post, 'embed', None)  # Acessando diretamente como atributo

            # Exibindo informações específicas
            print("\nPost Author Information:")
            print("DID:", author.did)
            print("Handle:", author.handle)
            print("Display Name:", author.display_name)
            print("Avatar URL:", author.avatar)
            print("Created At:", author.created_at)

            print("\nPost Content:")
            print("Text:", record.text)
            print("Post URI:", post.post.uri)
            print("Post Created At:", record.created_at)

            print("\nImages:")
            print(embed)  # Exibindo o conteúdo completo de embed para depuração

            print("\nInteractions:")
            print("Like Count:", post.post.like_count)
            print("Quote Count:", post.post.quote_count)
            print("Reply Count:", post.post.reply_count)
            print("Repost Count:", post.post.repost_count)

        # Atualiza o cursor para a próxima página
        cursor = data.cursor
        if not cursor:
            print("Nenhum cursor para a próxima página. Encerrando busca.")
            break

        pages_fetched += 1
        print(f"\nPágina {pages_fetched} processada.\n")
        time.sleep(1)  # Adicione um delay opcional para evitar sobrecarga na API


def main():
    # Obter as credenciais do arquivo .env
    username = os.getenv('BSKY_USERNAME')
    password = os.getenv('BSKY_PASSWORD')

    # Criação do cliente e login
    client = Client()
    client.login(username, password)

    # Handle do usuário que você quer os posts
    user_handle = 'atletico.bsky.social'
    profile = client.get_profile(user_handle)

    # Obter posts paginados
    fetch_posts(
        client=client,
        actor_did=profile.did,
        filter_type='posts_and_autor_threads',  # Tipo de posts

        # posts_with_replies, posts_no_replies, posts_with_media, posts_and_author_threads
        page_limit=100,  # Número de posts por página
        max_pages=30  # Número máximo de páginas a buscar
    )

if __name__ == '__main__':
    main()
