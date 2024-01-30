import numpy as np
import cv2

cap = cv2.VideoCapture(0)

trackbarWindow = 'Ajustes'
cv2.namedWindow(trackbarWindow)

def onChange(v):
    return

cv2.createTrackbar("Min Hue", trackbarWindow, 0, 255, onChange)
cv2.createTrackbar("Max Hue", trackbarWindow, 255, 255, onChange)

cv2.createTrackbar("Min Saturation", trackbarWindow, 0, 255, onChange)
cv2.createTrackbar("Max Saturation", trackbarWindow, 255, 255, onChange)

cv2.createTrackbar("Min Value", trackbarWindow, 0, 255, onChange)
cv2.createTrackbar("Max Value", trackbarWindow, 255, 255, onChange)

min_hue = cv2.getTrackbarPos("Min Hue", trackbarWindow)
max_hue = cv2.getTrackbarPos("Max Hue", trackbarWindow)

min_sat = cv2.getTrackbarPos("Min Saturation", trackbarWindow)
max_sat = cv2.getTrackbarPos("Max Saturation", trackbarWindow)

min_val = cv2.getTrackbarPos("Min Value", trackbarWindow)
max_val = cv2.getTrackbarPos("Max Value", trackbarWindow)

def setLimits():
    hue = {}
    hue['min'] = cv2.getTrackbarPos("Min Hue", trackbarWindow)
    hue['max'] = cv2.getTrackbarPos("Max Hue", trackbarWindow)
    if(hue['min'] > hue['max']):
        cv2.setTrackbarPos("Max Hue", trackbarWindow, hue['min'])
        hue['max'] = cv2.getTrackbarPos("Max Hue", trackbarWindow)

    sat = {}
    sat['min'] = cv2.getTrackbarPos("Min Saturation", trackbarWindow)
    sat['max'] = cv2.getTrackbarPos("Max Saturation", trackbarWindow)
    if(sat['min'] > sat['max']):
        cv2.setTrackbarPos("Max Saturation", trackbarWindow, sat['min'])
        sat['max'] = cv2.getTrackbarPos("Max Saturation", trackbarWindow)

    val = {}
    val['max'] = cv2.getTrackbarPos("Max Value", trackbarWindow)
    val['min'] = cv2.getTrackbarPos("Min Value", trackbarWindow)
    if(val['min'] > val['max']):
        cv2.setTrackbarPos("Max Value", trackbarWindow, val['min'])
        val['max'] = cv2.getTrackbarPos("Max Value", trackbarWindow)

    return hue, sat, val

def tracking(frame, hue, sat, val):

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerColor = np.array([hue['min'], sat["min"], val["min"]])
    upperColor = np.array([hue['max'], sat["max"], val["max"]])
    
    mask = cv2.inRange(hsvImage, lowerColor, upperColor)

    result = cv2.bitwise_and(frame, frame, mask = mask)
    result = frame.copy()
    result[mask == 255] = [0,0,255]

    return result

while True:
    success , frame = cap.read()
    cv2.imshow("cam", frame)

    hue, sat, val = setLimits()
    aux = tracking(frame, hue, sat, val)

    cv2.imshow("Resultado", aux)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   

cap.release()
cv2.destroyAllWindows()

