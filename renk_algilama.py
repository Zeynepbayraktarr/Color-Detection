import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # red
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([160, 100, 100])
    upper_red = np.array([179, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    result2 = cv2.bitwise_and(frame, frame, mask=mask2)

    # blue
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    result1 = cv2.bitwise_and(frame, frame, mask=mask1)


    # green
    lower_green = np.array([38, 100, 100])
    upper_green = np.array([75, 255, 255])
    mask3 = cv2.inRange(hsv, lower_green, upper_green)
    result3 = cv2.bitwise_and(frame, frame, mask=mask3)
    # sarı
    lower_yellow = np.array([22, 100, 100])
    upper_yellow = np.array([38, 255, 255])
    mask4 = cv2.inRange(hsv, lower_yellow, upper_yellow)
    result4 = cv2.bitwise_and(frame, frame, mask=mask2)
    contours, _ = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    sum = np.sum(np.nonzero(result4))
    for pic, contour in enumerate(contours, start=0):
        area = cv2.contourArea(contour)
        if( area >= 500):
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y),  (x + w, y + h),  (0, 0, 255), 2)
            cv2.putText(frame, "SARI", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 3.0, (0, 0, 255))
    cv2.imshow('kırmızı', result2)
    cv2.imshow('mavi', result1)
    cv2.imshow('yeşil', result3)
    cv2.imshow('sarı', result4)
    cv2.imshow('anaekran', frame)


    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
