from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addEquipForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 363)
        self.title = QtWidgets.QPlainTextEdit(Form)
        self.title.setGeometry(QtCore.QRect(110, 10, 281, 31))
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(9, 10, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 91, 31))
        self.label_3.setObjectName("label_3")
        self.typecomboBox = QtWidgets.QComboBox(Form)
        self.typecomboBox.setGeometry(QtCore.QRect(110, 90, 281, 26))
        self.typecomboBox.setObjectName("typecomboBox")
        self.invNumber = QtWidgets.QPlainTextEdit(Form)
        self.invNumber.setGeometry(QtCore.QRect(111, 130, 281, 31))
        self.invNumber.setObjectName("invNumber")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 81, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 310, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.roomcomboBox = QtWidgets.QComboBox(Form)
        self.roomcomboBox.setGeometry(QtCore.QRect(110, 52, 281, 26))
        self.roomcomboBox.setObjectName("roomcomboBox")
        self.description = QtWidgets.QPlainTextEdit(Form)
        self.description.setGeometry(QtCore.QRect(111, 177, 281, 121))
        self.description.setObjectName("description")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 177, 81, 31))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить оборудование"))
        self.label.setText(_translate("Form", "Модель"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>Размещение</p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Тип<br/>оборудования</p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p>Инвентарный<br/> номер</p></body></html>"))
        self.pushButton.setText(_translate("Form", "Применить"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p>Описание</p></body></html>"))
