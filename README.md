# env_dataset

This repository contains utilities for analyzing CCTV video data.

## Requirements
- Python 3.8+
- OpenCV (`opencv-python`)

Install dependencies using pip:

```bash
pip install opencv-python
```

## Usage
Run the analysis script with a video file:

```bash
python cctv_analysis.py path/to/video.mp4 --output-dir processed_frames
```

The script processes each frame, detects moving objects using background subtraction, and saves annotated frames to the specified output directory. It also prints the number of detected objects for each frame.
