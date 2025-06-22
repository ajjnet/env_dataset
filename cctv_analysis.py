import cv2
import argparse
import os


def analyze_video(video_path, output_dir):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open {video_path}")

    os.makedirs(output_dir, exist_ok=True)
    back_sub = cv2.createBackgroundSubtractorMOG2()

    frame_idx = 0
    object_counts = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        fg_mask = back_sub.apply(frame)
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        detections = [cv2.boundingRect(c) for c in contours if cv2.contourArea(c) > 500]
        for x, y, w, h in detections:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imwrite(os.path.join(output_dir, f"frame_{frame_idx:06d}.jpg"), frame)
        object_counts.append(len(detections))
        frame_idx += 1

    cap.release()
    return object_counts


def main():
    parser = argparse.ArgumentParser(description="Analyze CCTV video for moving objects")
    parser.add_argument("video", help="Path to input video file")
    parser.add_argument("--output-dir", default="output_frames", help="Directory to save annotated frames")
    args = parser.parse_args()
    counts = analyze_video(args.video, args.output_dir)
    print("Processed", len(counts), "frames.")
    print("Object counts per frame:", counts)


if __name__ == "__main__":
    main()
