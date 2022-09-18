from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addRoomForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 268)
        self.title = QtWidgets.QPlainTextEdit(Form)
        self.title.setGeometry(QtCore.QRect(110, 10, 281, 31))
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(9, 10, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 91, 31))
        self.label_2.setObjectName("label_2")
        self.personcomboBox = QtWidgets.QComboBox(Form)
        self.personcomboBox.setGeometry(QtCore.QRect(110, 50, 281, 26))
        self.personcomboBox.setObjectName("personcomboBox")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 217, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.description = QtWidgets.QPlainTextEdit(Form)
        self.description.setGeometry(QtCore.QRect(111, 87, 281, 121))
        self.description.setObjectName("description")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 87, 81, 31))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Кабинет"))
        self.label.setText(_translate("Form", "Номер"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>Ответственное<br/>лицо</p></body></html>"))
        self.pushButton.setText(_translate("Form", "Применить"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Описание</p></body></html>"))
