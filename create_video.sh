#!/bin/bash
set -e

mkdir -p output

echo "🧹 Cleaning old list..."
rm -f images/list.txt

echo "📝 Creating list of image files..."
for f in images/*.jpg; do
  echo "file '$f'" >> images/list.txt
done

echo "🎞️ Creating temp video from images..."
ffmpeg -y -f concat -safe 0 -i images/list.txt \
  -vf "fps=1,scale=iw:trunc(ih/2)*2,format=yuv420p" \
  -c:v libx264 output/temp.mp4 || {
    echo "❌ Failed to create video from images."
    exit 1
}

VIDEO="output/temp.mp4"
AUDIO="voice.mp3"
FINAL="output/final.mp4"

if [[ ! -f "$VIDEO" ]]; then
  echo "❌ Video file not found: $VIDEO"
  exit 1
fi

if [[ ! -f "$AUDIO" ]]; then
  echo "❌ Audio file not found: $AUDIO"
  exit 1
fi

echo "🔊 Merging audio with video..."
ffmpeg -y -i "$VIDEO" -i "$AUDIO" -c:v copy -c:a aac "$FINAL" || {
  echo "❌ Failed to merge video and audio"
  exit 1
}

echo "✅ Final video created at: $FINAL"

ffprobe output/final.mp4
