from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
from scipy.spatial import distance

# initialize dlib's face detector (HOG-based)
# then create the facial landmark predictor
detector = dlib.get_frontal_face_detector()

predictor_file = "model/shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_file)

# load the input image, resize it, and convert it to grayscale
image_file = "eye_closed.jpg"
image = cv2.imread(image_file)
image = imutils.resize(image, width=500)

# cvtColor: Converts an image from one color space to another.
# Here, convert a RGB image to gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
# The 1 in the second argument indicates that we should upsample the image 1 time.
# This will make everything bigger and allow us to detect more faces.
rects = detector(gray, 1)

# FUNCTION CALCULATING THE ASPECT RATIO FOR
# THE Eye BY USING EUCLIDEAN DISTANCE FUNCTION
def Detect_Eye(eye):
    poi_A = distance.euclidean(eye[1], eye[5])
    poi_B = distance.euclidean(eye[2], eye[4])
    poi_C = distance.euclidean(eye[0], eye[3])
    aspect_ratio_Eye = (poi_A+poi_B)/(2*poi_C)
    return aspect_ratio_Eye

# loop over the face detections
for (i, rect) in enumerate(rects):
    # determine the facial landmarks for the face region
    shape = predictor(gray, rect)
	
    leftEye = []
    rightEye = []

    # THESE ARE THE POINTS ALLOCATION FOR THE 
    # LEFT EYES IN .DAT FILE THAT ARE FROM 42 TO 47
    for n in range(42, 48):
        x = shape.part(n).x
        y = shape.part(n).y
        rightEye.append((x, y))
        next_point = n+1
        if n == 47:
            next_point = 42
        x2 = shape.part(next_point).x
        y2 = shape.part(next_point).y
        cv2.line(image, (x, y), (x2, y2), (0, 255, 0), 1)

    # THESE ARE THE POINTS ALLOCATION FOR THE 
    # RIGHT EYES IN .DAT FILE THAT ARE FROM 36 TO 41
    for n in range(36, 42):
        x = shape.part(n).x
        y = shape.part(n).y
        leftEye.append((x, y))
        next_point = n+1
        if n == 41:
            next_point = 36
        x2 = shape.part(next_point).x
        y2 = shape.part(next_point).y
        cv2.line(image, (x, y), (x2, y2), (0, 255, 0), 1)
    
    # CALCULATING THE ASPECT RATIO FOR LEFT 
    # AND RIGHT EYE
    right_Eye = Detect_Eye(rightEye)
    left_Eye = Detect_Eye(leftEye)
    Eye_Rat = (left_Eye+right_Eye)/2

    #NOW ROUND OF THE VALUE OF AVERAGE MEAN 
    # OF RIGHT AND LEFT EYES
    Eye_Rat = round(Eye_Rat, 2)

    # THIS VALUE OF 0.25 (YOU CAN EVEN CHANGE IT) 
    # WILL DECIDE WHETHER THE PERSONS'S EYES ARE CLOSE OR NOT
    if Eye_Rat < 0.25:
        cv2.putText(image, "DROWSINESS DETECTED", (50, 100),
                    cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)
        cv2.putText(image, "Alert!!!! WAKE UP DUDE", (50, 450),
                    cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 212), 3)

# show the output image with the face detections + facial landmarks
cv2.imshow("Output", image)
cv2.waitKey(0)