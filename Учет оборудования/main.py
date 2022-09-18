import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from main_ui import Ui_MainWindow
from find_ui import Ui_findWindow
from addRoom_ui import Ui_addRoomForm
from addType_ui import Ui_addTypeForm
from addPerson_ui import Ui_addPersonForm
from addEquip_ui import Ui_addEquipForm

DB_NAME = "equipment.db"


class FindFormWidget(QMainWindow, Ui_findWindow):
    # Класс формы поиска оборудования
    def __init__(self, parent=None):
        super().__init__(parent)
        self.con = sqlite3.connect(DB_NAME)
        self.params_person = {}
        self.params_room = {}
        self.setupUi(self)
        self.select_person()
        self.select_room()
        self.nameradioButton.setChecked(True)
        self.roomradioButton.setChecked(False)
        self.personradioButton.setChecked(False)
        self.invradioButton.setChecked(False) 
        self.invradioButton.clicked.connect(self.update_form)
        self.nameradioButton.clicked.connect(self.update_form)
        self.roomradioButton.clicked.connect(self.update_form)
        self.personradioButton.clicked.connect(self.update_form)
        self.update_form()
        self.pushButton.clicked.connect(self.make_find)
        self.editpushButton.clicked.connect(self.edit_equip)
        self.delpushButton.clicked.connect(self.delete_equip)
    
    def make_find(self):
        # Функция-обработчик кнопки поиска оборудования
        if self.nameradioButton.isChecked():
            self.make_find_name()
        elif self.roomradioButton.isChecked():
            self.make_find_room()
        elif self.personradioButton.isChecked():
            self.make_find_person()
        elif self.invradioButton.isChecked():
            self.make_find_inv()

    def make_find_name(self):
        # Функция поиска оборудования по названию
        cur = self.con.cursor()
        find_name = '%' + self.name.toPlainText() + '%'
        que = f'''SELECT e.id, e.name, r.number, t.type, e.invNumber
                  FROM equipment as e 
                  INNER JOIN types as t ON t.id = e.type
                  INNER JOIN rooms as r ON r.id = e.room
                  WHERE e.name like '{find_name}' 
                  ORDER BY e.id ASC'''
        result = cur.execute(que).fetchall()
        if len(result) > 0:
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels(
                ['ИД', 'Наименование', 'Кабинет', 'Тип', 'Инвентарный номер'])
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.tableWidget.resizeColumnsToContents()
    
    def make_find_room(self):
        # Функция поиска оборудования по кабинету
        cur = self.con.cursor()
        room = self.params_room.get(self.roomcomboBox.currentText())
        que = f'''SELECT e.id, e.name, r.number, t.type, e.invNumber 
                  FROM equipment as e 
                  INNER JOIN types as t ON t.id = e.type
                  INNER JOIN rooms as r ON r.id = e.room
                  WHERE e.room = {room} 
                  ORDER BY e.id ASC'''        
        result = cur.execute(que).fetchall()     
        if len(result) > 0:
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels(
                ['ИД', 'Наименование', 'Кабинет', 'Тип', 'Инвентарный номер'])
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.tableWidget.resizeColumnsToContents()
    
    def make_find_person(self):
        # Функция поиска оборудования по сотруднику(ответственному лицу)
        cur = self.con.cursor()
        person = self.params_person.get(self.personcomboBox.currentText())
        que = f'''SELECT e.id, e.name, r.number, t.type, e.invNumber 
                  FROM equipment as e 
                  INNER JOIN types as t ON t.id = e.type
                  INNER JOIN rooms as r ON r.id = e.room
                  WHERE r.person = {person} 
                  ORDER BY e.id ASC'''        
        result = cur.execute(que).fetchall()     
        if len(result) > 0:
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels(
                ['ИД', 'Наименование', 'Кабинет', 'Тип', 'Инвентарный номер'])
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.tableWidget.resizeColumnsToContents()
    
    def make_find_inv(self):
        # Функция поиска оборудования по инвентарному номеру
        cur = self.con.cursor()
        invnumber = self.invNumber.toPlainText()
        que = f'''SELECT e.id, e.name, r.number, t.type, e.invNumber 
                  FROM equipment as e 
                  INNER JOIN types as t ON t.id = e.type
                  INNER JOIN rooms as r ON r.id = e.room
                  WHERE e.invNumber = {invnumber} 
                  ORDER BY e.id ASC'''        
        result = cur.execute(que).fetchall()     
        if len(result) > 0:
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels(
                ['ИД', 'Наименование', 'Кабинет', 'Тип', 'Инвентарный номер'])
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.tableWidget.resizeColumnsToContents()
    
    def update_form(self):
        # Обновление формы в зависимости от выбранного режима поиска
        if self.nameradioButton.isChecked():
            self.name.setEnabled(True)
            self.roomcomboBox.setEnabled(False)
            self.personcomboBox.setEnabled(False)
            self.invNumber.setEnabled(False)
        elif self.roomradioButton.isChecked():
            self.name.setEnabled(False)
            self.roomcomboBox.setEnabled(True)
            self.personcomboBox.setEnabled(False)
            self.invNumber.setEnabled(False)
        elif self.personradioButton.isChecked():
            self.name.setEnabled(False)
            self.roomcomboBox.setEnabled(False)
            self.personcomboBox.setEnabled(True)
            self.invNumber.setEnabled(False)
        elif self.invradioButton.isChecked():
            self.name.setEnabled(False)
            self.roomcomboBox.setEnabled(False)
            self.personcomboBox.setEnabled(False)
            self.invNumber.setEnabled(True)         
    
    def select_room(self):
        # Выбор кабинета для поиска оборудования
        req = "SELECT id, number from rooms"
        cur = self.con.cursor()
        for value, key in cur.execute(req).fetchall():
            self.params_room[str(key)] = value
        self.roomcomboBox.addItems(list(self.params_room.keys()))  
        
    def select_person(self):
        # Выбор сотрудника для поиска оборудования
        req = "SELECT id, Name from persons"
        cur = self.con.cursor()
        for value, key in cur.execute(req).fetchall():
            self.params_person[str(key)] = value
        self.personcomboBox.addItems(list(self.params_person.keys()))    
    
    def edit_equip(self):
        # Открытие диалога для редактирования выбранного оборудования
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        dialog = AddEquipWidget(self, equip_id=ids[0])
        dialog.show() 
    
    def delete_equip(self):
        # Удаление выбранного оборудования
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        valid = QMessageBox.question(self, '', "Действительно удалить элементы с id " + ",".join(ids),
                                     QMessageBox.Yes,
                                     QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE from equipment WHERE ID in (" + ", ".join('?' * len(ids)) + ")", ids)
            self.con.commit()
            self.update_form()
            self.make_find()
    
    def update_equipments(self):
        self.update_form()
        self.make_find()        


class AddEquipWidget(QMainWindow, Ui_addEquipForm):
    # Класс формы добавления/редактирования оборудования
    def __init__(self, parent=None, equip_id=None):
        super().__init__(parent)
        self.con = sqlite3.connect(DB_NAME)
        self.params_type = {}
        self.params_room = {}
        self.setupUi(self)
        self.select_type()
        self.select_room()
        self.equip_id = equip_id
        if equip_id is not None:
            self.pushButton.clicked.connect(self.edit_elem)
            self.pushButton.setText('Отредактировать')
            self.setWindowTitle('Редактирование записи')
            self.get_elem()

        else:
            self.pushButton.clicked.connect(self.add_elem)

    def get_elem(self):
        # Получение информации об объекте из базы данных
        cur = self.con.cursor()
        que = f'''SELECT e.id, e.name, r.number, t.type, e.invNumber, e.description FROM equipment as e 
                  INNER JOIN types as t ON t.id = e.type
                  INNER JOIN rooms as r ON r.id = e.room
                  WHERE e.id = {self.equip_id} 
                  ORDER BY e.id ASC'''  
        item = cur.execute(que).fetchone()
        self.title.setPlainText(item[1])
        self.roomcomboBox.setCurrentText(str(item[2]))
        self.typecomboBox.setCurrentText(item[3])
        self.invNumber.setPlainText(str(item[4]))
        self.description.setPlainText(str(item[2]))

    def select_type(self):
        # Выбор типа оборудования
        req = "SELECT * from types"
        cur = self.con.cursor()
        for value, key in cur.execute(req).fetchall():
            self.params_type[key] = value
        self.typecomboBox.addItems(list(self.params_type.keys()))
        
    def select_room(self):
        # Выбор кабинета
        req = "SELECT id, number from rooms"
        cur = self.con.cursor()
        for value, key in cur.execute(req).fetchall():
            self.params_room[str(key)] = value
        self.roomcomboBox.addItems(list(self.params_room.keys()))    

    def add_elem(self):
        # Добавление нового объекта в базу данных
        cur = self.con.cursor()
        try:
            id_off = cur.execute("SELECT max(id) FROM equipment").fetchone()[0]
            new_data = (id_off + 1, self.title.toPlainText(),
                        self.params_room.get(self.roomcomboBox.currentText()),
                        self.params_type.get(self.typecomboBox.currentText()),
                        self.invNumber.toPlainText(),
                        self.description.toPlainText())
            cur.execute("INSERT INTO equipment VALUES (?,?,?,?,?,?)", new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_equipments()
            self.close()

    def edit_elem(self):
        # Запись измененного объекта в базу данных
        cur = self.con.cursor()
        try:
            new_data = (self.title.toPlainText(),
                        self.params_room.get(self.roomcomboBox.currentText()),
                        self.params_type.get(self.typecomboBox.currentText()),
                        self.invNumber.toPlainText(),
                        self.description.toPlainText(), self.equip_id)
            cur.execute("UPDATE equipment SET name=?, room=?, type=?, invNumber=?, description=? WHERE id=?", new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_equipments()
            self.close()


class AddRoomWidget(QMainWindow, Ui_addRoomForm):
    # Класс формы добавления/редактирования кабинета
    def __init__(self, parent=None, room_id=None):
        super().__init__(parent)
        self.con = sqlite3.connect(DB_NAME)
        self.params = {}
        self.setupUi(self)
        self.select_person()
        self.room_id = room_id
        if room_id is not None:
            self.pushButton.clicked.connect(self.edit_elem)
            self.pushButton.setText('Отредактировать')
            self.setWindowTitle('Редактирование записи')
            self.get_elem()

        else:
            self.pushButton.clicked.connect(self.add_elem)

    def get_elem(self):
        # Получение кабинета из базы данных
        cur = self.con.cursor()
        item = cur.execute(f'''SELECT r.id, r.number, p.Name, r.description 
                               FROM rooms as r 
                               JOIN persons as p 
                               ON p.id = r.person 
                               WHERE r.id = {self.room_id}''').fetchone()
        self.title.setPlainText(str(item[1]))
        self.personcomboBox.setCurrentText(item[2])
        self.description.setPlainText(item[3])

    def select_person(self):
        # Выбор сотрудника(заведующего кабинетом)
        req = "SELECT * from persons"
        cur = self.con.cursor()
        for value, key in cur.execute(req).fetchall():
            self.params[key] = value
        self.personcomboBox.addItems(list(self.params.keys()))
        
    def add_elem(self):
        # Добавление нового кабинета в базу данных
        cur = self.con.cursor()
        try:
            id_off = cur.execute("SELECT max(id) FROM rooms").fetchone()[0]
            new_data = (id_off + 1, self.title.toPlainText(),
                        self.params.get(self.personcomboBox.currentText()),
                        self.description.toPlainText())
            cur.execute("INSERT INTO rooms VALUES (?,?,?,?)", new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_rooms()
            self.close()

    def edit_elem(self):
        # Запись измененного кабинета в базу данных
        cur = self.con.cursor()
        try:
            new_data = (self.title.toPlainText(),
                        self.params.get(self.personcomboBox.currentText()),
                        self.description.toPlainText(), self.room_id)
            cur.execute(
                "UPDATE rooms SET number=?, person=?, description=? WHERE id=?",
                new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_rooms()
            self.close()


class AddTypeWidget(QMainWindow, Ui_addTypeForm):
    # Класс формы добавления/редактирования типа оборудования
    def __init__(self, parent=None, type_id=None):
        super().__init__(parent)
        self.con = sqlite3.connect(DB_NAME)
        self.params = {}
        self.setupUi(self)
        self.type_id = type_id
        if type_id is not None:
            self.saveButton.clicked.connect(self.edit_elem)
            self.setWindowTitle('Редактирование записи')
            self.get_elem()
        else:
            self.saveButton.clicked.connect(self.add_elem)

    def get_elem(self):
        # Получение типа оборудования из базы данных
        cur = self.con.cursor()
        item = cur.execute(f"SELECT * FROM types WHERE id = {self.type_id}").fetchone()
        self.title.setText(item[1])

    def add_elem(self):
        # Добавление нового типа оборудования в базу данных
        cur = self.con.cursor()
        try:
            id_off = cur.execute("SELECT max(id) FROM types").fetchone()[0]
            new_data = (id_off + 1, self.title.text())
            cur.execute("INSERT INTO types VALUES (?,?)", new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_types()
            self.close()

    def edit_elem(self):
        # Запись измененного типа оборудования в базу данных
        cur = self.con.cursor()
        try:
            new_data = (self.title.text(), self.type_id)
            cur.execute("UPDATE types SET type=? WHERE id=?", new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_types()
            self.close()


class AddPersonWidget(QMainWindow, Ui_addPersonForm):
    # Класс формы добавления/редактирования сотрудника
    def __init__(self, parent=None, person_id=None):
        super().__init__(parent)
        self.con = sqlite3.connect(DB_NAME)
        self.params = {}
        self.setupUi(self)
        self.person_id = person_id
        if person_id is not None:
            self.saveButton.clicked.connect(self.edit_elem)
            self.setWindowTitle('Редактирование записи')
            self.get_elem()
        else:
            self.saveButton.clicked.connect(self.add_elem)

    def get_elem(self):
        # Получение сотрудника из базы данных
        cur = self.con.cursor()
        item = cur.execute(f"SELECT * FROM persons WHERE id = {self.person_id}").fetchone()
        self.title.setText(item[1])

    def add_elem(self):
        # Добавление нового сотрудника в базу данных
        cur = self.con.cursor()
        try:
            id_off = cur.execute("SELECT max(id) FROM persons").fetchone()[0]
            new_data = (id_off + 1, self.title.text())
            cur.execute("INSERT INTO persons VALUES (?,?)", new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_persons()
            self.close()

    def edit_elem(self):
        # Запись измененного сотрудника в базу данных
        cur = self.con.cursor()
        try:
            new_data = (self.title.text(), self.person_id)
            cur.execute("UPDATE persons SET Name=? WHERE id=?", new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_persons()
            self.close()


class MyWidget(QMainWindow, Ui_MainWindow):
    # Класс формы главного окна программы
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect(DB_NAME)
        self.addEquipButton.clicked.connect(self.add_equip)
        self.editEquipButton.clicked.connect(self.edit_equip)
        self.deleteEquipButton.clicked.connect(self.delete_equip)
        self.addTypeButton.clicked.connect(self.add_type)
        self.editTypeButton.clicked.connect(self.edit_type)
        self.deleteTypeButton.clicked.connect(self.delete_type)
        self.addPersonButton.clicked.connect(self.add_person)
        self.editPersonButton.clicked.connect(self.edit_person)
        self.deletePersonButton.clicked.connect(self.delete_person) 
        self.addRoomButton.clicked.connect(self.add_room)
        self.editRoomButton.clicked.connect(self.edit_room)
        self.deleteRoomButton.clicked.connect(self.delete_room) 
        self.EquipTable.doubleClicked.connect(self.edit_equip)
        self.RoomTable.doubleClicked.connect(self.edit_room)
        self.TypeTable.doubleClicked.connect(self.edit_type)
        self.PersonTable.doubleClicked.connect(self.edit_person)
        self.dialogs = list()
        self.findAction.triggered.connect(self.find_form_handler)
        self.exitAction.triggered.connect(self.close_app)
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.update_equipments()
        self.update_rooms()
        self.update_types()
        self.update_persons()

    def update_equipments(self):
        # Обновление таблицы оборудования в главном окне программы
        cur = self.con.cursor()
        que = f'''SELECT e.id, e.name, r.number, t.type, e.invNumber 
                  FROM equipment as e 
                  INNER JOIN types as t ON t.id = e.type
                  INNER JOIN rooms as r ON r.id = e.room
                  ORDER BY e.id ASC'''        
        result = cur.execute(que).fetchall()
        self.EquipTable.setRowCount(len(result))
        self.EquipTable.setColumnCount(len(result[0]))
        self.EquipTable.setHorizontalHeaderLabels(
            ['ИД', 'Наименование', 'Кабинет', 'Тип', 'Инвентарный номер'])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.EquipTable.setItem(i, j, QTableWidgetItem(str(val)))
        self.EquipTable.resizeColumnsToContents()
    
    def update_rooms(self):
        # Обновление таблицы кабинетов в главном окне программы
        cur = self.con.cursor()
        que = '''SELECT r.id, r.number, p.Name, r.description 
                 FROM rooms as r 
                 JOIN persons as p ON p.id = r.person 
                 ORDER BY r.id ASC'''
        result = cur.execute(que).fetchall()
        self.RoomTable.setRowCount(len(result))
        self.RoomTable.setColumnCount(len(result[0]))
        self.RoomTable.setHorizontalHeaderLabels(
            ['ИД', 'Номер', 'Ответственный', 'Описание'])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.RoomTable.setItem(i, j, QTableWidgetItem(str(val)))
        self.RoomTable.resizeColumnsToContents()
    
    def update_types(self):
        # Обновление таблицы типов оборудования в главном окне программы
        cur = self.con.cursor()
        que = "SELECT id, type FROM types"
        result = cur.execute(que).fetchall()
        self.TypeTable.setRowCount(len(result))
        self.TypeTable.setColumnCount(len(result[0]))
        self.TypeTable.setHorizontalHeaderLabels(
            ['ИД', 'Тип оборудования'])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.TypeTable.setItem(i, j, QTableWidgetItem(str(val)))
        self.TypeTable.resizeColumnsToContents()
    
    def update_persons(self):
        # Обновление таблицы сотрудников в главном окне программы
        cur = self.con.cursor()
        que = "SELECT id, Name FROM persons"
        result = cur.execute(que).fetchall()
        self.PersonTable.setRowCount(len(result))
        self.PersonTable.setColumnCount(len(result[0]))
        self.PersonTable.setHorizontalHeaderLabels(
            ['ИД', 'ФИО'])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.PersonTable.setItem(i, j, QTableWidgetItem(str(val)))
        self.PersonTable.resizeColumnsToContents()

    def add_equip(self):
        # Обработчик кнопки добавления оборудования
        dialog = AddEquipWidget(self)
        dialog.show()

    def add_type(self):
        # Обработчик кнопки добавления типа оборудования
        dialog = AddTypeWidget(self)
        dialog.show()
    
    def add_person(self):
        # Обработчик кнопки добавления сотрудника
        dialog = AddPersonWidget(self)
        dialog.show() 
    
    def add_room(self):
        # Обработчик кнопки добавления кабинета
        dialog = AddRoomWidget(self)
        dialog.show() 
    
    def find_form_handler(self):
        # Обработчик кнопки открытия формы поиска оборудования
        self.find_form = FindFormWidget(self)
        self.find_form.show()    

    def edit_equip(self):
        # Обработчик кнопки редактирования выбранного оборудования
        rows = list(set([i.row() for i in self.EquipTable.selectedItems()]))
        ids = [self.EquipTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        dialog = AddEquipWidget(self, equip_id=ids[0])
        dialog.show()

    def edit_type(self):
        # бработчик кнопки редактирования выбранного типа оборудования
        rows = list(set([i.row() for i in self.TypeTable.selectedItems()]))
        ids = [self.TypeTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        dialog = AddTypeWidget(self, type_id=ids[0])
        dialog.show()
    
    def edit_person(self):
        # Обработчик кнопки редактирования выбранного сотрудника
        rows = list(set([i.row() for i in self.PersonTable.selectedItems()]))
        ids = [self.PersonTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        dialog = AddPersonWidget(self, person_id=ids[0])
        dialog.show()
    
    def edit_room(self):
        # Обработчик кнопки редактирования выбранного кабинета
        rows = list(set([i.row() for i in self.RoomTable.selectedItems()]))
        ids = [self.RoomTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        dialog = AddRoomWidget(self, room_id=ids[0])
        dialog.show()
    
    def delete_equip(self):
        # Обработчик кнопки удаления выбранного оборудования
        rows = list(set([i.row() for i in self.EquipTable.selectedItems()]))
        ids = [self.EquipTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        valid = QMessageBox.question(self,
                                     '',
                                     "Действительно удалить элементы с id " + ",".join(ids),
                                     QMessageBox.Yes,
                                     QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE from equipment WHERE ID in (" + ", ".join('?' * len(ids)) + ")", ids)
            self.con.commit()
            self.update_equipments()

    def delete_type(self):
        # Обработчик кнопки удаления выбранного типа оборудования
        rows = list(set([i.row() for i in self.TypeTable.selectedItems()]))
        ids = [self.TypeTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        valid = QMessageBox.question(self,
                                     '',
                                     "Действительно удалить элементы с id " + ",".join(ids),
                                     QMessageBox.Yes,
                                     QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE from types WHERE id in (" + ", ".join('?' * len(ids)) + ")", ids)
            self.con.commit()
            self.update_types()
    
    def delete_person(self):
        # Обработчик кнопки удаления выбранного сотрудника
        rows = list(set([i.row() for i in self.PersonTable.selectedItems()]))
        ids = [self.PersonTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        valid = QMessageBox.question(self,
                                     '',
                                     "Действительно удалить элементы с id " + ",".join(ids),
                                     QMessageBox.Yes,
                                     QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE from persons WHERE id in (" + ", ".join('?' * len(ids)) + ")", ids)
            self.con.commit()
            self.update_persons()

    def delete_room(self):
        # Обработчик кнопки удаления выбранного кабинета
        rows = list(set([i.row() for i in self.RoomTable.selectedItems()]))
        ids = [self.RoomTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        valid = QMessageBox.question(self,
                                     '',
                                     "Действительно удалить элементы с id " + ",".join(ids),
                                     QMessageBox.Yes,
                                     QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE from rooms WHERE ID in (" + ", ".join('?' * len(ids)) + ")", ids)
            self.con.commit()
            self.update_rooms()
    
    def close_app(self):
        # Закрытие программы
        self.close()

    def tab_changed(self, index):
        # Обработчик переключения табличных частей главного окна программы
        if index == 0:
            self.update_equipments()
        elif index == 3:
            self.update_persons()
        elif index == 1:
            self.update_rooms()        
        else:
            self.update_types()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
