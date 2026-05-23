from ultralytics import YOLO
import cv2
import time
import yaml
import os
import shutil
from collections import defaultdict
import ultralytics

# ──────────────────────────────────────────────
# Find the built-in botsort.yaml and patch only track_buffer
# This avoids AttributeError from missing required fields
# ──────────────────────────────────────────────
ultralytics_path = os.path.dirname(ultralytics.__file__)
builtin_config = os.path.join(ultralytics_path, "cfg", "trackers", "botsort.yaml")
custom_config = "custom_botsort.yaml"

shutil.copy(builtin_config, custom_config)

with open(custom_config, "r") as f:
    cfg = yaml.safe_load(f)

cfg["track_buffer"] = 120  # DEFAULT 30 → 120 (4 seconds @ 30fps)

with open(custom_config, "w") as f:
    yaml.dump(cfg, f)

print(f"Tracker config loaded from: {builtin_config}")
print(f"track_buffer set to: {cfg['track_buffer']}")

# ──────────────────────────────────────────────
# Load model
# ──────────────────────────────────────────────
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

prev_time = 0
PERSON_CLASS_ID = 0
track_history = defaultdict(list)
id_colors = {}
seen_ids = set()


def get_id_color(track_id):
    """Assign a stable color to each track ID."""
    if track_id not in id_colors:
        import random
        random.seed(track_id * 137)
        id_colors[track_id] = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )
    return id_colors[track_id]


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_height, frame_width, _ = frame.shape

    zone_x1 = int(frame_width * 0.3)
    zone_y1 = int(frame_height * 0.3)
    zone_x2 = int(frame_width * 0.7)
    zone_y2 = int(frame_height * 0.8)

    intrusion_detected = False
    intruder_ids = []

    results = model.track(
        frame,
        persist=True,
        tracker=custom_config,
        verbose=False,
        classes=[PERSON_CLASS_ID],
    )

    boxes = results[0].boxes

    if boxes is not None:
        for box in boxes:
            cls = int(box.cls[0])
            if cls != PERSON_CLASS_ID:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])

            track_id = None
            if box.id is not None:
                track_id = int(box.id[0])

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            color = get_id_color(track_id) if track_id is not None else (0, 255, 0)

            if track_id is not None:
                seen_ids.add(track_id)
                track_history[track_id].append((cx, cy))
                if len(track_history[track_id]) > 50:
                    track_history[track_id].pop(0)

                points = track_history[track_id]
                for i in range(1, len(points)):
                    alpha = i / len(points)
                    thickness = max(1, int(3 * alpha))
                    fade_color = tuple(int(c * alpha) for c in color)
                    cv2.line(frame, points[i - 1], points[i], fade_color, thickness)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.circle(frame, (cx, cy), 5, color, -1)

            label = f"ID:{track_id}  {conf:.2f}" if track_id is not None else f"?  {conf:.2f}"
            label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv2.rectangle(
                frame,
                (x1, y1 - label_size[1] - 10),
                (x1 + label_size[0] + 4, y1),
                color, -1,
            )
            cv2.putText(
                frame, label, (x1 + 2, y1 - 6),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2,
            )

            if zone_x1 < cx < zone_x2 and zone_y1 < cy < zone_y2:
                intrusion_detected = True
                if track_id is not None:
                    intruder_ids.append(track_id)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)

    # Draw restricted zone
    zone_color = (0, 0, 255) if intrusion_detected else (0, 165, 255)
    zone_thickness = 4 if intrusion_detected else 2

    overlay = frame.copy()
    alpha_zone = 0.15 if intrusion_detected else 0.08
    cv2.rectangle(overlay, (zone_x1, zone_y1), (zone_x2, zone_y2), zone_color, -1)
    cv2.addWeighted(overlay, alpha_zone, frame, 1 - alpha_zone, 0, frame)

    cv2.rectangle(frame, (zone_x1, zone_y1), (zone_x2, zone_y2), zone_color, zone_thickness)
    cv2.putText(
        frame, "RESTRICTED ZONE", (zone_x1 + 5, zone_y1 - 8),
        cv2.FONT_HERSHEY_SIMPLEX, 0.7, zone_color, 2,
    )

    if intrusion_detected:
        ids_str = ", ".join(str(i) for i in intruder_ids)
        cv2.putText(
            frame, f"!! INTRUSION DETECTED  ID: {ids_str} !!",
            (30, 55), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3,
        )
        cv2.rectangle(frame, (0, 0), (frame_width - 1, frame_height - 1), (0, 0, 255), 6)

    new_time = time.time()
    fps = 1 / (new_time - prev_time + 1e-6)
    prev_time = new_time

    info_lines = [
        f"FPS: {int(fps)}",
        f"Tracked IDs: {len(seen_ids)}",
        f"Buffer: {cfg['track_buffer']} frames",
    ]
    for i, line in enumerate(info_lines):
        cv2.putText(
            frame, line, (10, frame_height - 20 - i * 25),
            cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2,
        )

    cv2.imshow("YOLOv8 Security Tracking System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
if os.path.exists(custom_config):
    os.remove(custom_config)

print(f"\nSession ended. Total unique IDs seen: {len(seen_ids)}")