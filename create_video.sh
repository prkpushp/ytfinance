#!/bin/bash
set -e

IMAGE_DIR="output/images"
LIST_FILE="$IMAGE_DIR/list.txt"
AUDIO_FILE="output/voice.mp3"
OUTPUT_VIDEO="output/temp.mp4"

echo "📝 Creating list of image files..."

# Clear old list.txt if exists
> "$LIST_FILE"

# Write list.txt with filenames relative to LIST_FILE location (same dir as images)
shopt -s nullglob
for img in "$IMAGE_DIR"/*.{jpg,jpeg,png}; do
  filename=$(basename "$img")
  echo "file '$filename'" >> "$LIST_FILE"
done
shopt -u nullglob

if [ ! -s "$LIST_FILE" ]; then
  echo "❌ No images found in $IMAGE_DIR"
  exit 1
fi

echo "✅ Created list.txt with image files: "
cat "$LIST_FILE"

# Check audio file exists
if [ ! -f "$AUDIO_FILE" ]; then
  echo "❌ Audio file not found: $AUDIO_FILE"
  exit 1
fi

# Run ffmpeg from the images directory so that list.txt file and image files resolve correctly
echo "🎬 Creating video from images and audio..."

(
  cd "$IMAGE_DIR"
  ffmpeg -y -f concat -safe 0 -i list.txt -r 1 -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -pix_fmt yuv420p temp_no_audio.mp4
)

# Now merge the audio, trim/pad if needed to match video duration
echo "🔊 Merging audio with video..."

ffmpeg -y -i "$IMAGE_DIR/temp_no_audio.mp4" -i "$AUDIO_FILE" -c:v copy -c:a aac -shortest "$OUTPUT_VIDEO"

echo "✅ Video created successfully at $OUTPUT_VIDEO"
