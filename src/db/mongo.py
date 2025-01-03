from datetime import datetime

from pymongo import MongoClient

MONGO_DB = "bsky"
client = MongoClient("mongodb://localhost:27017/")
db = client["bsky"]


def save_to_db(collection_name: str, user_data):
    collection = db[collection_name]

    try:
        collection.update_one(
            {"user_id": user_data['did']},
            {
                "$set": {
                    "display_name": user_data.get('display_name', 'N/A'),
                    "description": user_data.get('description', 'N/A'),
                    "handle": user_data.get('handle', 'N/A'),
                    "updated_at": datetime.now()
                },
                "$setOnInsert": {
                    "created_at": datetime.now()
                }
            },
            upsert=True
        )
    except Exception as e:
        print(f"Erro ao salvar dados do usuário {user_data['did']}: {e}")
