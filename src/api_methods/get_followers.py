from time import sleep

from atproto_client.models.app.bsky.graph.get_followers import Params

from model.client import AtProtoClientContextManager


def get_followers(actor_did: str, client, max_followers: int):
    params = Params(actor=actor_did, limit=100)
    all_followers = []
    curr_num_followers = 0

    while curr_num_followers < max_followers or max_followers == 0:
        response = client.app.bsky.graph.get_followers(params=params)

        if not response.followers:
            print("Nenhum seguidor retornado. Encerrando.")
            break

        all_followers.extend(response.followers)
        curr_num_followers += len(response.followers)

        if response.cursor:
            params.cursor = response.cursor
        else:
            break
        print(f"Obtidos {curr_num_followers} seguidores. Aguardando 0.15s para próxima requisição.")
        sleep(0.15)

    return all_followers


def get_followers_count(actor_did: str):
    with AtProtoClientContextManager() as client:
        response = client.get_profile(actor_did)
        return response.followers_count
