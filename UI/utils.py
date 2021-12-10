from faceHelper import *
from PyQt5.QtWidgets import QMessageBox
from sqlite3Helper import *
from UI.menu import *
from UI.registration import *
import matplotlib.pyplot as plt
import numpy as np
import re
import time_recorder


dir = 'faceData'
sql3_helper = SQLITE3_Helper()
today = time_recorder.get_today()

class RegistrationWindow(QtWidgets.QDialog,Ui_registrationDialog):
    def __init__(self):
        super(RegistrationWindow, self).__init__()
        self.setupUi(self)

    def takePhoto(self):
        userID = self.idEdit.text()
        # id not obey the rule
        if userID =="":
            QMessageBox.information(self, "Warning", "Please enter your ID !")
        elif re.match("^[0-9]{4}853[a-zA-Z0-9]{5}[0-9]{4}$",userID):
            if not os.path.exists(dir):
                os.mkdir(dir)

            # invoke camera to capture face and save the picture name as ${id}.jpg
            opened=faceCapture(userID)
            if not opened:
                QMessageBox.information(self,"Warning","No camera")
                return

            img_path = os.path.join(dir, userID + '.jpg')
            if os.path.exists(img_path):
                self.imgEdit.setText(userID + '.jpg')
                face = QtGui.QPixmap(os.path.join(dir, userID + '.jpg'))
                self.face_label.setPixmap(face)

                unknown_image = face_recognition.load_image_file(img_path)
                print("load unknown")
                unknown_encodings = face_recognition.face_encodings(unknown_image)
                if not unknown_encodings:
                    QMessageBox.information(self, "Warning", "No Face Recognition, Please Retry !")
                    os.remove(img_path)
        else:
            QMessageBox.information(self, "Warning", "User ID not obey the rule, e.g. 1809853zi0110099")

    def addUser(self):
        userID = self.idEdit.text()
        userName = self.nameEdit.text()
        userImg = userID + '.jpg'

        # if photo not exist
        if not os.path.exists(os.path.join(dir, userImg)):
            QMessageBox.information(self, "Warning", "Please Take Photo !")
            return

        # if name or id is not input
        if userName == "" or userID == "":
            QMessageBox.information(self, "Warning", "Either ID or Name is empty !")
            return
        else:
            print('ID:{0}, Name:{1}, Image:{2}'.format(userID, userName, userImg))

            # sql = "insert into record values (null,'{}',0)".format(userName)
            # result1 = dbHelper.execute(sql, None)

            testsql = "SELECT * FROM tasks_student WHERE sid = '{}'".format(userID)
            if len(sql3_helper.query(cmd=testsql)) == 0:

                try:
                    sql = "INSERT INTO tasks_student VALUES ('" + userID + "','" + userName + "','" + userImg + "')"
                    sql3_helper.insert(cmd=sql)
                    QMessageBox.information(self, "Tip", "Registration Succeed !")
                    print("Insert successfully")
                    self.close()

                except:
                    QMessageBox.information(self, "Warning", "Registration Fail !")
                    print("Insert fail")
            else:
                QMessageBox.information(self, "Warning", "Same ID or same name !")
                return


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.count = 0
        self.MAX = 5

    def execRegistration(self):
        if self.registrationButton.clicked:
            self.registrationDialog = RegistrationWindow()
            self.registrationDialog.show()
            self.registrationDialog.exec_()

    def execIdentification(self):
        if self.identificationButton.clicked:
            opened=faceCapture('unknown')
            if not opened:
                QMessageBox.information(self, "Warning", "Hardware Error, cannot Open Camera")
                return
            unknown_file = 'unknown.jpg'
            unknown_path = os.path.join(os.path.abspath(dir), unknown_file)
            print(unknown_path)
            if os.path.exists(unknown_path):
                face = QtGui.QPixmap(unknown_path)
                self.gridLayout.itemAt(self.count).widget().setPixmap(face)
                if self.count < self.MAX:
                    self.count += 1
                else:
                    self.count = 0
                print("picture added")

            success, msg = faceRecognize(sql3_helper, unknown_path, dir)
            if success != False:
                userID = success[0]
                userName = success[1]
                courseID = 1

                # check if the student has signed in before
                sqlcmd = "SELECT COUNT(*) FROM tasks_signin WHERE Date(time) = '" + str(today) + "' AND sid_id = '" + str(userID) + "'"
                out = sql3_helper.query(sqlcmd)

                if int(out[0][0]) > 0:
                    QMessageBox.information(self, "Warning", "Hello {}, you have already signed in !".format(userName))

                else:
                    # print(time_recorder.get_time_record())
                    if time_recorder.is_class_time("9:00:00", "23:50:00"):

                        sqlcmd = "SELECT COUNT(*) FROM tasks_signin"
                        total = sql3_helper.query(sqlcmd)
                        # print(int(total[0][0]+1))

                        sql = "INSERT INTO tasks_signin VALUES (" + str(total[0][0]+1) + "," + str(courseID) + ",'" + \
                              userID + "','" + time_recorder.get_time_record() + "')"
                        sql3_helper.insert(sql)
                        QMessageBox.information(self, "Tip", "Sign in succeed !\nWelcome {}".format(userName))

                    else:
                        QMessageBox.information(self, "Warning", "The course is not open now, sign-in is unavailable !")
            else:
                QMessageBox.information(self, "Warning", "Sign in fail ! \n{}\nWill Restart Automatically".format(msg))

                # automatically retry
                self.execIdentification()

    def execDrawPlot(self):

        # pie plot about attendance & absence rate
        sqlcmd = "SELECT COUNT(*) FROM tasks_signin WHERE Date(time) = '" + str(today) + "' AND cid_id = 1"
        re = sql3_helper.query(sqlcmd)

        attend = re[0][0]

        sqlcmd = "SELECT COUNT(*) FROM tasks_student"
        re2 = sql3_helper.query(sqlcmd)

        absence = re2[0][0] - attend

        y = np.array([attend, absence])

        plt.pie(y,
                labels=['Attendance: ' + str(attend), 'Absence: ' + str(absence)],
                colors=["#d5695d", "#a564c9"],
                explode=(0.25, 0),
                autopct='%.2f%%',
                )
        plt.title("CS001 Attendance & Absence Rate", pad=30)
        plt.show()

        # bar plot about time record
        sqlcmd = "SELECT * FROM tasks_signin WHERE Date(time) = '" + str(today) + "'"
        re1 = sql3_helper.query(sqlcmd)

        # get time record
        record = []
        for each in re1:
            s = list(each)[3].split()[1]
            record.append(str(s.split(":")[0]) + ":" + str(s.split(":")[1]))

        if len(record) == 0:
            QMessageBox.information(self, "Tips", "No record!")

        else:
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
            plt.title("CS001 Sign-in Record on " + str(today) + "          Total students: " + str(len(num)))
            plt.xlabel("Sign-in Time")
            plt.ylabel("Number of Students")
            plt.ylim(0, 1.2 * data_max)
            plt.yticks([])
            plt.bar(time, num, color=["#707070", "#949494", "#B8B8B8", "#DCDCDC"], width=0.4)

            for a, b in zip(time, num):
                plt.text(a, b + 0.02, '%.0f' % b, ha='center', va='bottom', fontsize=11)

            plt.show()