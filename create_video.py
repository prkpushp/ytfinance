import os
import ffmpeg

# Write image list for concat
image_inputs = "".join(
    f"file 'output/images/img{i}.jpg'\n" for i in range(3)
)
with open("output/images.txt", "w") as f:
    f.write(image_inputs)

# Create slideshow from images
ffmpeg.input("output/images.txt", format='concat', safe=0).output(
    "output/temp.mp4", framerate=1, vf="scale=1280:720", vcodec="libx264"
).run(overwrite_output=True)

# Merge slideshow with audio
ffmpeg.input("output/temp.mp4").output(
    "output/final_video.mp4",
    i="output/voice.mp3",
    codec="copy",
    shortest=None
).run(overwrite_output=True)
