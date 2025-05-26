#!/bin/bash

set -e

VIDEO="output/temp.mp4"
AUDIO="output/voice.mp3"
OUTPUT="output/final.mp4"

# Function to print error and exit
function fail {
  echo "❌ $1"
  exit 1
}

# Check if video exists
if [[ ! -f "$VIDEO" ]]; then
  fail "Video file not found: $VIDEO"
fi

# Check if audio exists
if [[ ! -f "$AUDIO" ]]; then
  fail "Audio file not found: $AUDIO"
fi

# Merge using ffmpeg
echo "✅ Merging $VIDEO and $AUDIO into $OUTPUT ..."
ffmpeg -i "$VIDEO" -i "$AUDIO" -c:v copy -c:a aac -strict experimental "$OUTPUT" -y || fail "ffmpeg merge failed"

echo "✅ Merge complete. Output saved to $OUTPUT"
