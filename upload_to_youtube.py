from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

if os.path.exists("token.pickle"):
    with open("token.pickle", "rb") as token:
        creds = pickle.load(token)
else:
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    creds = flow.run_local_server(port=0)
    with open("token.pickle", "wb") as token:
        pickle.dump(creds, token)

youtube = build("youtube", "v3", credentials=creds)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "5 Passive Income Ideas for 2025",
            "description": "Discover passive income ideas to boost your earnings.",
            "tags": ["finance", "passive income", "2025"]
        },
        "status": {"privacyStatus": "public"}
    },
    media_body="output/final_video.mp4"
)
response = request.execute()
print(response)
