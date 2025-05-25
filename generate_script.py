import requests
import json

API_KEY = "YOUR_GEMINI_API_KEY"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
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
script_text = data["candidates"][0]["content"]["parts"][0]["text"]

with open("output/script.txt", "w") as f:
    f.write(script_text)
