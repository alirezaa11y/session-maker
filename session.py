from rubpy import Client
import os

os.makedirs("sey", exist_ok=True)
session_path = "session"
client = Client(session_path)

with client:
    me = client.get_me()
    print(me)

print("Session saved to:", session_path + ".session")
