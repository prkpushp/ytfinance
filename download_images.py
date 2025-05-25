import requests
import os

keywords = ["money", "business", "finance"]
os.makedirs("output/images", exist_ok=True)

for i, word in enumerate(keywords):
    url = f"https://source.unsplash.com/1280x720/?{word}"
    response = requests.get(url)
    with open(f"output/images/img{i}.jpg", "wb") as f:
        f.write(response.content)
