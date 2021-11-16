import cv2
import face_recognition.api as face_recognition
import os
import numpy as np


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
        minSize=(30,30),
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
    if not cap.isOpened():
        print('Camera close')
        return False

    # video
    while (cap.isOpened()):
        # read the frame of camera
        ret, frame = cap.read()
        # add keyboard event
        key = cv2.waitKey(1) & 0xFF
        if ret == True:
            # get current frame
            faceCapture, result = getface(frame)
            cv2.imshow('Camera, press "s" to save, press "q" to quit', faceCapture)
            if result:
                if key == ord('s'):
                    for x1, y1, x2, y2 in result:
                        face = frame[y1:y2, x1:x2]

                    cv2.imencode('.jpg', face)[1].tofile('faceData/' + name + '.jpg')
                    break
                elif key == ord('q'):
                    break
        else:
            break

    # release resource
    cap.release()
    cv2.destroyAllWindows()
    return True


def faceRecognize(sql3_helper, unknown_path, dir):
    unknown_image = face_recognition.load_image_file(unknown_path)
    print("load unknown")
    unknown_encodings = face_recognition.face_encodings(unknown_image)
    if not unknown_encodings:
        return False, "No face recognized"
    unknown_encoding = unknown_encodings[0]
    print("encode unknown")

    # 从数据库中获取已注册的用户脸部图片
    sql_command = "SELECT * FROM tasks_student"

    all_result = sql3_helper.query(cmd=sql_command)
    print(all_result)

    # 将jpg文件加载到numpy数组中
    imgs = []
    labels = []
    known_encoding = []

    os.chdir(dir)
    print(os.getcwd())

    for i in range(len(all_result)):

        if os.path.exists(all_result[i][2]):
            print("Loading ", all_result[i][2])
            labels.append(all_result[i])
            imgs.append(face_recognition.load_image_file(all_result[i][2]))

            # 获取每个图像文件中每个面部的面部编码
            encode = face_recognition.face_encodings(imgs[i])[0]
            known_encoding.append(encode)
        else:
            return False, "Face Data Missing"

    print("total face:", len(known_encoding))
    os.chdir('../')
    print(os.getcwd())

    try:
        results = face_recognition.face_distance(known_encoding,unknown_encoding)
        print(results)
        print(np.min(results))

        # confidence interval
        if np.min(results) > 0.47:
            return False, "Low Confidence "

        # find minimum
        minIndex=np.argmin(results)
        return labels[minIndex], "success"

    except Exception as e:
        print(e)
        return False, "exception"
