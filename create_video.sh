#!/bin/bash
set -e

# Variables
IMAGE_DIR="output/images"
LIST_FILE="$IMAGE_DIR/list.txt"
VOICE_FILE="output/voice.mp3"
OUTPUT_VIDEO="output/final_video.mp4"
FPS=1           # Set fps for image duration control (1 frame per second)
VIDEO_WIDTH=1280 # Desired width (adjust as needed)
VIDEO_HEIGHT=720 # Desired height (must be divisible by 2)

# Check if image directory exists and has images
if [ ! -d "$IMAGE_DIR" ]; then
  echo "❌ Image directory not found: $IMAGE_DIR"
  exit 1
fi

shopt -s nullglob
images=("$IMAGE_DIR"/*.jpg "$IMAGE_DIR"/*.jpeg "$IMAGE_DIR"/*.png)
if [ ${#images[@]} -eq 0 ]; then
  echo "❌ No images found in $IMAGE_DIR"
  exit 1
fi
shopt -u nullglob

# Create or overwrite list.txt for ffmpeg concat demuxer
echo "📝 Creating list of image files for ffmpeg..."

> "$LIST_FILE"  # Truncate or create file

for img in "${images[@]}"; do
  # ffmpeg concat demuxer needs format: file 'filename'
  echo "file '$img'" >> "$LIST_FILE"
  # Duration per image, e.g., 3 seconds, can add if needed:
  # echo "duration 3" >> "$LIST_FILE"
done

# Optional: repeat last file duration for proper concat
# echo "file '${images[-1]}'" >> "$LIST_FILE"

# Verify voice file exists
if [ ! -f "$VOICE_FILE" ]; then
  echo "❌ Voice file not found: $VOICE_FILE"
  exit 1
fi

echo "🎬 Creating video from images and adding voiceover..."

ffmpeg -y -f concat -safe 0 -i "$LIST_FILE" \
  -r $FPS \
  -vf "scale=$VIDEO_WIDTH:$VIDEO_HEIGHT:flags=lanczos" \
  -c:v libx264 -pix_fmt yuv420p -preset veryfast -crf 23 \
  -i "$VOICE_FILE" \
  -c:a aac -shortest "$OUTPUT_VIDEO"

echo "✅ Video created successfully: $OUTPUT_VIDEO"
