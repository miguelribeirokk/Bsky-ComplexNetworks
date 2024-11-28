from atproto import Client
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


def main():
    # Obter as credenciais do arquivo .env
    username = os.getenv('BSKY_USERNAME')
    password = os.getenv('BSKY_PASSWORD')

    # Criação do cliente e login
    client = Client()
    client.login(username, password)

    # URI do Feed Generator
    feed_generator_uri = 'at://did:plc:q6gjnaw2blty4crticxkmujt/app.bsky.feed.generator/cl-brasil'

    # Obter os posts do Feed Generator
    data = client.app.bsky.feed.get_feed({
        'feed': feed_generator_uri,
        'limit': 10  # Número de posts por página (máximo 100)
    })

    # O feed retornado é um objeto, podemos acessar os posts e exibir de forma legível
    feed = data.feed  # Lista de posts
    next_page = data.cursor  # Cursor para a próxima página de resultados

    pprint(feed, depth=3)

    for post in feed:
        print("_" * 150)
        print("Post number:", feed.index(post) + 1)
        # Navegando diretamente pelos campos
        author = post['post']['author']
        record = post['post']['record']
        embed = post['post']['embed']

        # Exibindo informações específicas
        print("\nPost Author Information:")
        print("DID:", author['did'])
        print("Handle:", author['handle'])
        print("Display Name:", author['display_name'])
        print("Avatar URL:", author['avatar'])
        print("Created At:", author['created_at'])

        print("\nPost Content:")
        print("Text:", record['text'])
        print("Post URI:", post['post']['uri'])
        print("Post Created At:", record['created_at'])

        print("\nImage Details:")
        # Verificando se embed não é None antes de acessar
        if embed and 'images' in embed:
            for image in embed['images']:
                print("Image Fullsize URL:", image['fullsize'])
                print("Image Aspect Ratio:", image['aspect_ratio'])
        else:
            print("No images available for this post.")

        print("\nInteractions:")
        print("Like Count:", post['post']['like_count'])
        print("Quote Count:", post['post']['quote_count'])
        print("Reply Count:", post['post']['reply_count'])
        print("Repost Count:", post['post']['repost_count'])


if __name__ == '__main__':
    main()
