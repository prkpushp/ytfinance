import os
import ffmpeg

# Create images.txt for ffmpeg concat
image_list = [f"file '../images/img{i}.jpg'" for i in range(3)]  # Adjusted path
os.makedirs("output", exist_ok=True)

with open("output/images.txt", "w") as f:
    f.write("\n".join(image_list))

# Create slideshow video from images
(
    ffmpeg
    .input("output/images.txt", format='concat', safe=0)
    .output("output/temp.mp4", framerate=0.2, vf="scale=1280:720", vcodec="libx264")
    .run(overwrite_output=True)
)

# Combine slideshow with voice.mp3
(
    ffmpeg
    .input("output/temp.mp4")
    .input("output/voice.mp3")
    .output("output/final_video.mp4", vcodec="copy", acodec="aac", shortest=None)
    .run(overwrite_output=True)
)
