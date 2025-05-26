import ffmpeg

# Create slideshow from sequential images
ffmpeg.input('output/images/img%d.jpg', framerate=1).output(
    'output/temp.mp4',
    vf='scale=1280:720',
    vcodec='libx264'
).run(overwrite_output=True)

# Merge slideshow with audio
ffmpeg.input('output/temp.mp4').output(
    'output/final_video.mp4',
    i='output/voice.mp3',
    codec='copy',
    shortest=None
).run(overwrite_output=True)
