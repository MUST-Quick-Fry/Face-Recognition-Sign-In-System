import sys 
import unittest 
from unittest.mock import patch, Mock, MagicMock
from PyQt5.QtWidgets import QApplication
from faceHelper import *
from sqlite3Helper import SQLITE3_Helper
from showplot import *
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest, QSignalSpy
from UI.utils import *

class TestSqlite3Helper(unittest.TestCase):
        
    def test_display(self):
        with patch('sqlite3Helper.sqlite3.connect') as mock_connect:
            mock_connect.cursor.fetchall.return_value = [('1', '2', '3')]
            SQLITE3_Helper().display()
            mock_connect.assert_called_once()
    
    def test_insert(self):
        with patch('sqlite3Helper.sqlite3.connect') as mock_connect:
            mock_connect.return_value.cursor.return_value.fetchall.return_value = [('1', '2', '3')]
            SQLITE3_Helper.insert(mock_connect, r'INSERT INTO Student VALUE("1","2","3")')
            mock_connect.assert_called_once()

      
class TestShowPlot(unittest.TestCase):
    
    def test_plot(self):
        with patch('showplot.plt.show') as mock_show:
            plotpie()
            plotbar()
            mock_show.assert_called()

# using black-box testing and white-box testing to test the registration dialog    
class TestUIRegistration(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = RegistrationWindow()
        self.window.setupUi(self.window)
        self.window.show()
        
    def add_registration_clicked_suit(self, id, name, isTakePhoto):
        self.window.nameEdit.setText(name)
        self.window.idEdit.setText(id)
        if(isTakePhoto):
            QTest.mouseClick(self.window.photoButton,Qt.LeftButton)
        QTest.mouseClick(self.window.addButton,Qt.LeftButton)
        self.assertEqual(self.window.nameEdit.text(), name)
        self.assertEqual(self.window.idEdit.text(), id)
        self.assertEqual(self.window.imgEdit.text(), id + '.jpg')
    
    def test_textEditsWidgetsText(self):
        self.assertEqual(self.ui.nameEdit.placeholderText(), '')
        self.assertEqual(self.ui.idEdit.placeholderText(), '')
        self.assertEqual(self.ui.imgEdit.placeholderText(), '')
        self.assertEqual(self.ui.imgEdit.isEnabled(), False)
    
    def test_take_photo_clicked(self):
        self.ui.photoButton.clicked.emit()
        self.assertFalse(self.ui.imgEdit.isEnabled())
        
    def test_add_registration_clicked_01(self):
        self.add_registration_clicked_suit('1809853zi0110099','cr',True)
       
    def test_add_registration_clicked_02(self):
        self.add_registration_clicked_suit('1809853zi0110098','123',True)
 
    def test_add_registration_clicked_03(self):
        self.add_registration_clicked_suit('1809853ji0110097','',True)
    
    def test_add_registration_clicked_04(self):
        self.add_registration_clicked_suit('1809853@iohqwer!','cyx',True)
    
    def test_add_registration_clicked_05(self):
        self.add_registration_clicked_suit('1809!@#$%^&*()','hpl',True)
    
    def test_add_registration_clicked_06(self):
        self.add_registration_clicked_suit('1809😂😂😂😂','',True)
    
    def test_add_registration_clicked_07(self):
        self.add_registration_clicked_suit('','wyy',True)
    
    def test_add_registration_clicked_08(self):
        self.add_registration_clicked_suit('','(^-^)(^-^)(^-^)',True)
    
    def test_add_registration_clicked_09(self):
        self.add_registration_clicked_suit('','',True)
    
    def test_add_registration_clicked_10(self):
        self.add_registration_clicked_suit('1809853zi0110099','cr',False)
    
    def tearDown(self):
        self.window.close()
        self.app.quit()

class TestUIMainWindow(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.window.setupUi(self.window)
        self.window.show()
        
    def test_menu(self):
        with patch('UI.utils.MainWindow') as mock_window:
            mock_window.return_value.exec_ = Mock()
            mock_window.return_value.exec_()
            mock_window.assert_called_once()
    
    def test_execIdentification(self):
        QTest.mouseClick(self.window.identificationButton,Qt.LeftButton)
    
    def test_execDrawPlot(self):
        QTest.mouseClick(self.window.printButton,Qt.LeftButton)
    
        
    def tearDown(self):
        self.window.close()
        self.app.quit()

# class TestUISuite(unittest.suite):
    
#     def __init__(self):
#         super().__init__()
#         self.addTest(unittest.makeSuite(TestSqlite3Helper))
#         self.addTest(unittest.makeSuite(TestShowPlot))
#         self.addTest(unittest.makeSuite(TestUIRegistration))
#         self.addTest(unittest.makeSuite(TestUIMainWindow))

if __name__ == '__main__':
    unittest.main()