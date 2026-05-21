import cv2
import time

cap = cv2.VideoCapture(0)
prev_frame_time = 0
new_frame_time = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 100, 200)

    if not ret:
        print("Camera not found")
        break

    new_frame_time = time.time()

    fps = 1 / (new_frame_time - prev_frame_time)

    prev_frame_time = new_frame_time

    fps_text = f"FPS: {int(fps)}"

    cv2.putText(
    edges,
    fps_text,
    (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

    cv2.imshow("Edge Detection", edges)


    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        cv2.imwrite("screenshot.png", edges)
    print("Screenshot saved")

    if key == ord('q'):
         break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()