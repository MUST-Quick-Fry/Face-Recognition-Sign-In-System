import numpy as np
import sys, os
import face_recognition
import face_recognition.api as face_recognition
import matplotlib.pyplot as plt
from faceDetector import *
from UI.menu import *
from UI.registration import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from sqlite3_helper import *


dir='faceData'
sql3_helper = SQLITE3_Helper()

class RegistrationWindow(QtWidgets.QDialog, Ui_registrationDialog):
    def __init__(self):
        super(RegistrationWindow, self).__init__()
        self.setupUi(self)

    def takePhoto(self):
        name = self.nameEdit.text()
        if name != "":
            if not os.path.exists(dir):
                os.mkdir(dir)

            faceCapture(name)
            self.imgEdit.setText(name + '.jpg')

        else:
            QMessageBox.information(self, "Take Photo", "Please enter your name !")

    def addUser(self):
        userID = self.idEdit.text()
        userName = self.nameEdit.text()
        userImg = userName + '.jpg'

        if userName == "" or userID == "" or userImg == "":
            QMessageBox.information(self, "Registration", "Either ID or Name is empty !")
        else:
            print('ID:{0}, Name:{1}, Image:{2}'.format(userID, userName, userImg))

            # sql = "insert into record values (null,'{}',0)".format(userName)
            # result1 = dbHelper.execute(sql, None)

            testsql = "SELECT * FROM Student WHERE sid = '" + userID + "' or stuname = '" + userName + "'"
            if len(sql3_helper.query(cmd=testsql)) == 0:

                try:
                    sql = "INSERT INTO Student VALUES ('" + userID + "','" + userName + "','" + userImg + "')"
                    sql3_helper.insert(cmd=sql)
                    QMessageBox.information(self, "Registration", "Registration Succeed !")
                    print("Insert successfully")

                except:
                    QMessageBox.information(self, "Registration", "Registration Fail !")
                    print("Insert fail")
            else:
                QMessageBox.information(self, "Registration", "Same ID or same name !")

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def execRegistration(self):
        if self.registrationButton.clicked:
            registrationDialog = RegistrationWindow()
            registrationDialog.show()
            registrationDialog.exec_()

    def execIdentification(self):
        if self.identificationButton.clicked:
            faceCapture('unknown')
            face = QtGui.QPixmap(dir + '/unknown.jpg').scaled(115, 120)
            self.faceView.setAlignment(Qt.AlignCenter)
            self.faceView.setPixmap(face)

        if self.identificationButton.clicked:
            print("hi")
            info = faceRecognize()
            if info != False:
                self.infoLabel.setText("Sign-in succeed ! " + info)

            else:
                self.infoLabel.setText("Sign-in fail ！" + info)

    def showStatis(self):
        print("打卡统计")
        #drawPane()


def faceRecognize():
    # 从数据库中获取已注册的用户脸部图片

    sql_command = "SELECT * FROM Student"

    all_result = sql3_helper.query(cmd=sql_command)
    print(all_result)

    # 将jpg文件加载到numpy数组中
    imgs = []
    labels = []
    known_encoding = []

    os.chdir(dir)
    print(os.getcwd())

    for i in range(len(all_result)):
        print(all_result[i][2])
        labels.append(all_result[i][1])
        imgs.append(face_recognition.load_image_file(all_result[i][2]))
        print("识别中...")

        # 获取每个图像文件中每个面部的面部编码
        encode = face_recognition.face_encodings(imgs[i])[0]
        known_encoding.append(encode)

    unknown_image = face_recognition.load_image_file('test.jpg')
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    os.chdir('../')
    print(os.getcwd())


    try:
        results = face_recognition.face_distance(known_encoding, unknown_encoding)
        print(results)
        print(np.min(results))
        if np.min(results) > 0.30:
            return False
        # 找出最小值的下标
        min = 1.0
        minIndex = 0
        for i in range(len(results)):
            if results[i] < min:
                min = results[i]
                minIndex = i
        print(labels[minIndex])
        return labels[minIndex]
    except:
        return False


def drawPane():
    print("绘制饼状图")
    labels = ['Success', 'Failure']
    colors = ['red', 'blue']
    explode = [0.1, 0]
    sizes = []

    sql = "select count(*) from record where success=%s"
    # success = dh.fetchall(sql, 1)[0][0]
    # sizes.append(success)
    # print(success)
    # sql1 = "select count(*) from record where success=%s"
    # fail = dh.fetchall(sql1, 0)[0][0]
    # sizes.append(fail)
    # print(fail)
    # plt.axes(aspect=1)
    # plt.pie(x=sizes, labels=labels, explode=explode, autopct='%3.1f %%',
    #         shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6)
    # plt.title("Card Record")
    # plt.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

    sys.exit(0)