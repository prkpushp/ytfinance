import requests
import json
import os
import sys

API_KEY = "AIzaSyBaHx9w6G6Ffz2Wq37wyEZYVi6b4REN8GQ"
if not API_KEY:
    print("❌ GEMINI_API_KEY is not set.")
    sys.exit(1)

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
headers = {"Content-Type": "application/json"}
prompt = "Write a YouTube video script on '5 Passive Income Ideas for 2025'"

payload = {
    "contents": [
        {
            "parts": [{"text": prompt}]
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
data = response.json()

if "candidates" not in data:
    print("❌ Gemini API failed. Response:")
    print(json.dumps(data, indent=2))
    sys.exit(1)

script_text = data["candidates"][0]["content"]["parts"][0]["text"]

os.makedirs("output", exist_ok=True)
with open("output/script.txt", "w") as f:
    f.write(script_text)

print("✅ Script generated successfully.")
