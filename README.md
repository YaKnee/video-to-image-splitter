# Video to Image Splitter

Simple script to read in a video, specify if you want to split by FPS (frames per second), or a number of images evenly spaced throughout video.

# Usage

```
# Extract 2 frames per second
python script.py input.mp4 frames/ --fps 2

# Extract 100 frames evenly spaced
python script.py input.mp4 frames/ --num 100
```