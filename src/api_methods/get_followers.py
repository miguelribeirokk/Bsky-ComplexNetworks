from atproto_client.models.app.bsky.graph.get_followers import Params

from model.client import AtProtoClientContextManager


def get_followers(actor_did: str, limit: int = 100):
    params = Params(actor=actor_did, limit=limit)
    all_followers = []

    with AtProtoClientContextManager() as client:
        while True:
            response = client.app.bsky.graph.get_followers(params=params)

            all_followers.extend(response.followers)
            print(f"Followers retrieved: {len(response.followers)}")

            if response.cursor:
                params.cursor = response.cursor
            else:
                break

    print(f"Total followers: {len(all_followers)}")
    return all_followers
