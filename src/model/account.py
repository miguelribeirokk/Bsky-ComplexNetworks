class Account:
    def __init__(self, id, name):
        self.id = id
        self.nome = name
        self.followers = {}

    def add_follower(self, id, name):
        self.followers[id] = Account(id, name)

    def get_followers(self):
        return [follower.name for follower in self.followers.values()]
