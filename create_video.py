import ffmpeg
import os

images = [f"output/images/img{i}.jpg" for i in range(3)]
inputs = "|".join(images)

ffmpeg.input("output/voice.mp3").output(
    "output/final_video.mp4",
    vcodec='libx264',
    acodec='aac',
    shortest=None,
    vf=f"movie={images[0]},fade=t=in:st=0:d=1"
).run(overwrite_output=True)
