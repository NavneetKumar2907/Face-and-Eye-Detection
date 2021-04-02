import cv2
def detectAndDisplay(frame):
    # Converting Color to gray
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Equalizing hist of gray image
    frame_gray = cv2.equalizeHist(frame_gray)
    #-- Detect Faces

    faces = face_cascader.detectMultiScale(frame_gray)

    # Detecting Each Faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 1)
        faceROI = frame_gray[y:y+h, x:x+w]
        eyes = eye_cascader.detectMultiScale(faceROI)
        # For each face, detect Eye
        for (x0, y0, w0, h0) in eyes:
            center = (x+x0+w0//2, y+y0+h0//2)
            radius = int((w0+h0)*0.25)
            cv2.circle(frame,center,radius, (0,0,255), 2)

    cv2.imshow('video',frame)

# Face Cascader and Eye Cascader Classifier
face_cascader = cv2.CascadeClassifier()
eye_cascader = cv2.CascadeClassifier()

# Load the cascader
try:
    face_cascader.load('haarcascade_frontalface_default.xml')
    eye_cascader.load('eye_cascade.xml')
except:
    print('ERROR LOADING')
    exit(0)

# Read the video stream and detect face

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print('!!ERROR Opening Camera')
    exit(0)
while(True):
    ret, frame = webcam.read()
    if frame is None:
        print('!! ERROR NO CAPTURED FRAME.')
        break

    detectAndDisplay(frame)
    if cv2.waitKey(10) ==27:
        break

