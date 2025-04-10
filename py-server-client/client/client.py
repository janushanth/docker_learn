import requests
import time
import os

SERVER_HOST = os.environ.get("SERVER_HOST", "http://server:6000")
API_TOKEN = os.environ.get("API_TOKEN", "super-secret-token")

def check_server():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }

    while True:
        try:
            response = requests.get(f"{SERVER_HOST}/ping", headers=headers)
            if response.status_code == 200:
                print("✅ Connected to server:", response.json())
            else:
                print(f"❌ Failed with status {response.status_code}: {response.text}")
        except Exception as e:
            print("❌ Connection error:", str(e))

        time.sleep(10)

if __name__ == "__main__":
    check_server()
