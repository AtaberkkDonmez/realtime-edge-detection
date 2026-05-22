import cv2
import time
import math

# Camera
cap = cv2.VideoCapture(0)

# Background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2(
    history=100,
    varThreshold=40,
    detectShadows=True
)

# FPS timer
prev_time = 0

# Persistent tracked objects
objects = {}

# Next object ID
next_object_id = 0

# Distance threshold
DISTANCE_THRESHOLD = 50

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    motion_detected = False

    # Background subtraction
    mask = fgbg.apply(frame)

    # Remove shadows / weak noise
    _, thresh = cv2.threshold(
        mask,
        200,
        255,
        cv2.THRESH_BINARY
    )

    # Noise reduction
    dilated = cv2.dilate(
        thresh,
        None,
        iterations=2
    )

    # Find contours
    contours, _ = cv2.findContours(
        dilated,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    current_objects = {}

    for contour in contours:

        area = cv2.contourArea(contour)

        # Ignore small noise
        if area < 1500:
            continue

        # Ignore extremely large areas
        if area > 60000:
            continue

        motion_detected = True

        x, y, w, h = cv2.boundingRect(contour)

        cx = x + w // 2
        cy = y + h // 2

        same_object_detected = False

        # Compare with existing objects
        for object_id, pt in objects.items():

            distance = math.hypot(
                cx - pt[0],
                cy - pt[1]
            )

            # Same object
            if distance < DISTANCE_THRESHOLD:

                current_objects[object_id] = (cx, cy)

                same_object_detected = True

                # Bounding box
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                # Center point
                cv2.circle(
                    frame,
                    (cx, cy),
                    5,
                    (255, 0, 0),
                    -1
                )

                # Object ID
                cv2.putText(
                    frame,
                    f"ID {object_id}",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 255),
                    2
                )

                break

        # New object
        if not same_object_detected:

            current_objects[next_object_id] = (cx, cy)

            # Bounding box
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Center point
            cv2.circle(
                frame,
                (cx, cy),
                5,
                (255, 0, 0),
                -1
            )

            # Object ID
            cv2.putText(
                frame,
                f"ID {next_object_id}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

            next_object_id += 1

    # Update tracked objects
    objects = current_objects.copy()

    # Tracking status
    if motion_detected:

        cv2.putText(
            frame,
            "Persistent Tracking Active",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    # FPS calculation
    new_time = time.time()

    fps = 1 / (new_time - prev_time + 1e-6)

    prev_time = new_time

    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    # Show frame
    cv2.imshow(
        "Persistent Multi-Object Tracking",
        frame
    )

    # Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()