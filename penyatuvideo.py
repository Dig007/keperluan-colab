from tqdm.notebook import tqdm
import cv2
import os
import numpy as np

# Dapatkan daftar semua file mp4
videos = [video for video in os.listdir() if video.endswith('.mp4')]

# Urutkan video jika perlu
videos.sort()

# Inisialisasi penulis video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = None

with tqdm(total=len(videos), desc="Processing videos", dynamic_ncols=True) as pbar_outer:
    for video in videos:
        # Baca video
        cap = cv2.VideoCapture(video)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        with tqdm(total=total_frames, desc=f"Processing {video}", leave=False, dynamic_ncols=True) as pbar_inner:
            for _ in range(total_frames):
                # Baca frame
                ret, frame = cap.read()
                if not ret:
                    break

                # Inisialisasi penulis video jika belum ada
                if out is None:
                    h, w = frame.shape[:2]
                    out = cv2.VideoWriter('/content/output.mp4', fourcc, 30.0, (w, h))

                # Tulis frame ke video output
                out.write(frame)

                pbar_inner.update()

        # Lepaskan objek video capture
        cap.release()

        pbar_outer.update()

# Lepaskan objek penulis video
if out is not None:
    out.release()
