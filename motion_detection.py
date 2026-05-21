import cv2
import time

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

prev_time = 0

points = []
previous_motion = False

while cap.isOpened():

    motion_detected = False

    # Frame differencing
    diff = cv2.absdiff(frame1, frame2)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    dilated = cv2.dilate(thresh, None, iterations=3)

    contours, _ = cv2.findContours(
        dilated,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:

        if cv2.contourArea(contour) < 1000:
            continue

        motion_detected = True

        x, y, w, h = cv2.boundingRect(contour)

        cx = x + w // 2
        cy = y + h // 2

        points.append((cx, cy))

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.circle(frame1, (cx, cy), 5, (255, 0, 0), -1)

        cv2.putText(
            frame1,
            "Motion Detected",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    #  STATE-BASED RESET
    if motion_detected and not previous_motion:
        # yeni hareket başladı → eski izleri temizle
        points = []

    if not motion_detected:
        # hareket yoksa geçmişi tutma
        points = []

    previous_motion = motion_detected

    # Trail çizimi
    for i in range(1, len(points)):
        cv2.line(frame1, points[i - 1], points[i], (255, 255, 0), 2)

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

    cv2.imshow("State-Based Motion Tracking", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()