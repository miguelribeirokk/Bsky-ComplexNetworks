import os

from atproto_client import Client
from dotenv import load_dotenv

load_dotenv()


class AtProtoClientContextManager:
    def __init__(self):
        self.username = os.getenv('BSKY_USERNAME')
        self.password = os.getenv('BSKY_PASSWORD')
        self.client = None

    def __enter__(self):
        self.client = Client()
        self.client.login(self.username, self.password)
        return self.client

    def __exit__(self, exc_type, exc_value, traceback):
        self.client = None
