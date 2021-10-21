from faceHelper import *
from PyQt5.QtWidgets import QMessageBox
from sqlite3Helper import *
from UI.menu import *
from UI.registration import *
import matplotlib.pyplot as plt
import numpy as np

dir = 'faceData'
sql3_helper = SQLITE3_Helper()


class RegistrationWindow(QtWidgets.QDialog,Ui_registrationDialog):
    def __init__(self):
        super(RegistrationWindow,self).__init__()
        self.setupUi(self)

    def takePhoto(self):
        userID = self.idEdit.text()
        if userID != "":
            if not os.path.exists(dir):
                os.mkdir(dir)

            # invoke camera to capture face and save the picture name as ${id}.jpg
            faceCapture(userID)
            img_path=os.path.join(dir,userID + '.jpg')
            if os.path.exists(img_path):
                self.imgEdit.setText(userID + '.jpg')
                face = QtGui.QPixmap(os.path.join(dir,userID + '.jpg'))
                self.face_label.setPixmap(face)

                unknown_image = face_recognition.load_image_file(img_path)
                print("load unknown")
                unknown_encodings = face_recognition.face_encodings(unknown_image)
                if not unknown_encodings:
                    QMessageBox.information(self,"Take Photo","No Face Recognition, Please Retry !")
                    os.remove(img_path)
        else:
            QMessageBox.information(self,"Take Photo","Please enter your name !")

    def addUser(self):
        userID = self.idEdit.text()
        userName = self.nameEdit.text()
        userImg = userID + '.jpg'

        # if photo not exist
        if not os.path.exists(os.path.join(dir,userImg)):
            QMessageBox.information(self,"Registration","Please Take Photo !")
            return

        # if name or id is not input
        if userName == "" or userID == "":
            QMessageBox.information(self,"Registration","Either ID or Name is empty !")
            return
        else:
            print('ID:{0}, Name:{1}, Image:{2}'.format(userID,userName,userImg))

            # sql = "insert into record values (null,'{}',0)".format(userName)
            # result1 = dbHelper.execute(sql, None)

            testsql = "SELECT * FROM Student WHERE sid = '{}'".format(userID)
            if len(sql3_helper.query(cmd=testsql)) == 0:

                try:
                    sql = "INSERT INTO Student VALUES ('" + userID + "','" + userName + "','" + userImg + "')"
                    sql3_helper.insert(cmd=sql)
                    QMessageBox.information(self,"Registration","Registration Succeed !")
                    print("Insert successfully")
                    self.close()

                except:
                    QMessageBox.information(self,"Registration","Registration Fail !")
                    print("Insert fail")
            else:
                QMessageBox.information(self,"Registration","Same ID or same name !")
                return


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.count = 0
        self.MAX = 5

    def execRegistration(self):
        if self.registrationButton.clicked:
            registrationDialog = RegistrationWindow()
            registrationDialog.show()
            registrationDialog.exec_()

    def execIdentification(self):
        if self.identificationButton.clicked:
            opened=faceCapture('unknown')
            if not opened:
                QMessageBox.information(self,"Hardware Error","Cannot Open Camera")
                return
            unknown_file = 'unknown.jpg'
            unknown_path = os.path.join(os.path.abspath(dir),unknown_file)
            print(unknown_path)
            if os.path.exists(unknown_path):
                face = QtGui.QPixmap(unknown_path)
                self.gridLayout.itemAt(self.count).widget().setPixmap(face)
                if self.count < self.MAX:
                    self.count += 1
                else:
                    self.count = 0
                print("picture added")

            success,msg = faceRecognize(sql3_helper,unknown_path,dir)
            if success != False:
                userID = success[0]
                userName = success[1]
                courseID = 1
                sql = "INSERT INTO SignIn (Sid,Cid) VALUES('{}',{})".format(userID,courseID)
                sql3_helper.insert(sql)
                QMessageBox.information(self,"Sign In","Sign in succeed !\nWelcome {}".format(userName))
            else:
                QMessageBox.information(self,"Sign In","Sign in fail ! \n{}\nWill Restart Automatically".format(msg))

                # automatically retry
                self.execIdentification()

    def execDrawPlot(self):
        sqlcmd = "SELECT * FROM SignIn"
        re = sql3_helper.query(sqlcmd)
        today = "2021-10-19"
        # print(re)

        # get time record
        record = []
        for each in re:
            if list(each)[3].split()[0] == today:
                s = list(each)[3].split()[1]
                record.append(str(s.split(":")[0]) + ":" + str(s.split(":")[1]))

        # print(record)

        dic = {}
        for key in record:
            dic[key] = dic.get(key, 0) + 1

        # print(dic)

        time = list(dic)
        num = list(dic.values())
        # print(time)
        # print(num)

        # set parameters
        data_num = len(time)
        data_max = max(num)
        fig_width = 8 + 0.5 * data_num
        fig_height = 4 + 0.5 * data_num

        # draw plot
        plt.figure(figsize=(fig_width, fig_height))
        plt.title("Sign-in Record on " + str(today) + "          Total students: " + str(len(num)))
        plt.xlabel("Sign-in Time")
        plt.ylabel("Number of Students")
        plt.ylim(0, 1.2 * data_max)
        plt.yticks([])
        plt.bar(time, num, color=["#707070", "#949494", "#B8B8B8", "#DCDCDC"], width=0.4)

        for a, b in zip(time, num):
            plt.text(a, b + 0.02, '%.0f' % b, ha='center', va='bottom', fontsize=11)

        plt.show()