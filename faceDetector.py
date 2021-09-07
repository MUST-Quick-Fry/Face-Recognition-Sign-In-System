import cv2


# face detection
def getface(image):
    # import opencv haarcascade package
    model_path = 'haarcascades/haarcascade_frontalface_default.xml'
    # create classifier
    clf = cv2.CascadeClassifier(model_path)
    # set degree of gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # get face and draw a rectangle
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    result = []
    for (x, y, w, h) in faces:
        result.append((x, y, x + w, y + h))
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image, result


# face capture
def faceCapture(name):
    cap = cv2.VideoCapture(0)  # open the camera

    # video
    # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

    while (cap.isOpened()):
        # read the frame of camera
        ret, frame = cap.read()

        # add keyboard event
        key = cv2.waitKey(1) & 0xFF
        if ret == True:
            # get current frame
            faceCapture, result = getface(frame)
            cv2.imshow('Camera', faceCapture)
            if result:
                if key == ord('s'):
                    for x1, y1, x2, y2 in result:
                        face = frame[y1:y2, x1:x2]
                    print(name)
                    # cv2.imwrite(dir + name + '.jpg', face)
                    cv2.imencode('.jpg', face)[1].tofile('faceData/' + name + '.jpg')
                    break
                elif key == ord('q'):
                    break
        else:
            break

    # release resource
    cap.release()
    cv2.destroyAllWindows()