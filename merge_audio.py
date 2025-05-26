import os
import subprocess

video_input = "output/temp.mp4"
audio_input = "output/voice.mp3"
output_path = "output/final_video.mp4"

if not os.path.exists(video_input):
    raise FileNotFoundError(f"Missing video: {video_input}")
if not os.path.exists(audio_input):
    raise FileNotFoundError(f"Missing audio: {audio_input}")

# Fix odd height issue (e.g., 627 not divisible by 2)
safe_resolution_video = "output/safe_video.mp4"
subprocess.run([
    "ffmpeg", "-y", "-i", video_input,
    "-vf", "scale=iw:ih*trunc(oh/2)*2",  # Ensure height is divisible by 2
    safe_resolution_video
], check=True)

# Merge safe video + voice
subprocess.run([
    "ffmpeg", "-y",
    "-i", safe_resolution_video,
    "-i", audio_input,
    "-c:v", "copy", "-c:a", "aac",
    "-shortest",
    output_path
], check=True)

print(f"✅ Final video created: {output_path}")
