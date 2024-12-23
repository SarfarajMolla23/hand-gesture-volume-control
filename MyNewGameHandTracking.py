import cv2
import time
import HandTrackingModule as htm

pTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.7, trackCon=0.7)  # Adjust confidence thresholds if needed

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(f"Thumb Tip Position: {lmList[4]}")

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
