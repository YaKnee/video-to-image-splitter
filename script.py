import cv2
import os
import argparse


def extract_frames(video_path, output_dir, fps=None, num_images=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("Could not open video.")

    video_fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if fps is not None and num_images is not None:
        raise ValueError("Specify either fps or num_images, not both.")

    if fps is None and num_images is None:
        raise ValueError("You must specify either fps or num_images.")

    if fps is not None:
        frame_step = max(int(video_fps / fps), 1)
    else:
        frame_step = max(total_frames // num_images, 1)

    frame_idx = 0
    saved_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % frame_step == 0:
            output_path = os.path.join(output_dir, f"frame_{saved_idx:05d}.jpg")
            cv2.imwrite(output_path, frame)
            saved_idx += 1

        frame_idx += 1

    cap.release()
    print(f"Saved {saved_idx} frames to '{output_dir}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frames from a video.")
    parser.add_argument("video", help="Path to input video")
    parser.add_argument("output", help="Output directory for images")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fps", type=float, help="Frames per second to extract")
    group.add_argument("--num", type=int, help="Total number of images to extract")

    args = parser.parse_args()

    extract_frames(
        video_path=args.video,
        output_dir=args.output,
        fps=args.fps,
        num_images=args.num
    )