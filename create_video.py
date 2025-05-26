import ffmpeg

# Create slideshow from sequential images
ffmpeg.input('output/images/img%d.jpg', framerate=1).output(
    'output/temp.mp4',
    vf='scale=1280:720',
    vcodec='libx264'
).run(overwrite_output=True)


ffmpeg
    .input('output/temp.mp4')
    .input('output/voice.mp3')
    .output('output/final.mp4', vcodec='copy', acodec='aac', strict='experimental')
    .run()
