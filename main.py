import cv2
import time

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

prev_time = 0

object_id = 0

while cap.isOpened():

    motion_detected = False

    diff = cv2.absdiff(frame1, frame2)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(
        blur,
        35,
        255,
        cv2.THRESH_BINARY
    )

    dilated = cv2.dilate(thresh, None, iterations=3)

    contours, _ = cv2.findContours(
        dilated,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    detected_objects = []

    for contour in contours:

        area = cv2.contourArea(contour)

        if area < 1000:
            continue

        if area > 50000:
            continue

        motion_detected = True

        x, y, w, h = cv2.boundingRect(contour)

        cx = x + w // 2
        cy = y + h // 2

        detected_objects.append((cx, cy))

        # Bounding box
        cv2.rectangle(
            frame1,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Center point
        cv2.circle(
            frame1,
            (cx, cy),
            5,
            (255, 0, 0),
            -1
        )

        # Object ID
        cv2.putText(
            frame1,
            f"ID {object_id}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )

        object_id += 1

    # Motion status
    if motion_detected:

        cv2.putText(
            frame1,
            "Tracking Active",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    # FPS
    new_time = time.time()

    fps = 1 / (new_time - prev_time + 1e-6)

    prev_time = new_time

    cv2.putText(
        frame1,
        f"FPS: {int(fps)}",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imshow(
        "Multi-Object Tracking",
        frame1
    )

    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()