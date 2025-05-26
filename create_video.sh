#!/bin/bash
set -e

mkdir -p output

echo "📦 Generating video from images..."
ffmpeg -y -framerate 1 -start_number 0 -i output/images/img%d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p output/temp.mp4 || {
  echo "❌ Failed to create video from images."
  exit 1
}

VIDEO="output/temp.mp4"
AUDIO="voice.mp3"
OUTPUT="output/final.mp4"

if [[ ! -f "$VIDEO" ]]; then
  echo "❌ Video file not found: $VIDEO"
  exit 1
fi

if [[ ! -f "$AUDIO" ]]; then
  echo "❌ Audio file not found: $AUDIO"
  exit 1
fi

echo "🎬 Merging video and audio..."
ffmpeg -i "$VIDEO" -i "$AUDIO" -c:v copy -c:a aac -strict experimental "$OUTPUT" -y || {
  echo "❌ Failed to merge video and audio"
  exit 1
}

echo "✅ Final video created at: $OUTPUT"
