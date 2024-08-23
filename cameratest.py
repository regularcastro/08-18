import cv2
from rembg import remove

def detect_lines(frame):
    frame = remove(frame)
    #gray = cv2.Canny(frame, 1,255,None,3)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lsd = cv2.createLineSegmentDetector()

    lines = lsd.detect(gray)[0]
    drawn_img = lsd.drawSegments(gray, lines)
    return drawn_img

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("noframecap")
        break

    frame_with_lines = detect_lines(frame)
    cv2.imshow('linhascanny',frame_with_lines)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()