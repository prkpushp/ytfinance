import requests
import os

API_KEY = "TLU46qoXKGtmnkBD1kSb1uEVOQw1DXI9wWMj8YRAhq5ZovdbpmO87hmW"  # Replace this with your real key
headers = {"Authorization": API_KEY}
keywords = ["money", "business", "finance"]
os.makedirs("output/images", exist_ok=True)

for i, keyword in enumerate(keywords):
    params = {"query": keyword, "per_page": 1}
    response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data["photos"]:
            img_url = data["photos"][0]["src"]["landscape"]
            img_data = requests.get(img_url).content
            with open(f"output/images/img{i}.jpg", "wb") as f:
                f.write(img_data)
            print(f"✅ Downloaded: img{i}.jpg")
        else:
            print(f"❌ No images found for '{keyword}'")
    else:
        print(f"❌ API error for '{keyword}', status: {response.status_code}")
