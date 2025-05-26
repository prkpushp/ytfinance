import requests
import json
import os

API_KEY = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={API_KEY}"
headers = {"Content-Type": "application/json"}
prompt = "Write a YouTube video script on '5 Passive Income Ideas for 2025'"

payload = {
  "contents": [
    {
      "parts": [
        {"text": prompt}
      ]
    }
  ]
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
data = response.json()

try:
    script_text = data["candidates"][0]["content"]["parts"][0]["text"]
    with open("output/script.txt", "w") as f:
        f.write(script_text)
    print("✅ Script generated successfully.")
except KeyError:
    print("❌ Gemini API failed. Response:")
    print(json.dumps(data, indent=2))
    exit(1)
