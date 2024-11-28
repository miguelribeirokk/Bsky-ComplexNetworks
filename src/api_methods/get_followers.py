from atproto_client.models.app.bsky.graph.get_followers import Params
from atproto import Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

username = os.getenv('BSKY_USERNAME')
password = os.getenv('BSKY_PASSWORD')

# Create client and log in
client = Client()
client.login(username, password)

# User actor identifier (DID for the user)
actor = "did:plc:sc2mo2yyi7cdxbfhp275jgzl"  # Replace with the actual actor DID

# Initialize parameters with limit (max 100)
params = Params(actor=actor, limit=100)

# List to store all followers
all_followers = []

while True:
    # Fetch followers using the API
    response = client.app.bsky.graph.get_followers(params=params)

    # Add current page followers to the list
    all_followers.extend(response.followers)
    print(f"Followers retrieved: {len(response.followers)}")

    # Check if there is a cursor for the next page
    if response.cursor:
        params.cursor = response.cursor  # Update params with the cursor
    else:
        break  # Exit the loop if no more pages

# Total followers count
print(f"Total followers: {len(all_followers)}")

# (Optional) Print follower details
for follower in all_followers:
    print(f"Display Name: {follower.display_name}")
    print(f"Handle: {follower.handle}")
    print(f"DID: {follower.did}")
    print("-" * 40)