import sys
import os
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem
from main_ui import Ui_MainWindow
from addEditCoffeeForm import Ui_Form


def request():
    con = sqlite3.connect(resource_path('data/coffee.sqlite'))
    cur = con.cursor()
    ask = '''SELECT * FROM coffees'''
    result = cur.execute(ask).fetchall()
    con.close()
    return result


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.editBtn.clicked.connect(self.edit_table)
        self.result.setColumnCount(7)
        self.result.setWordWrap(True)
        names = ['id', 'Название', 'Степень обжарки', 'В зернах?', 'Описание вкуса', 'цена (руб/кг)', 'Объем упаковки (грамм)']
        self.result.setHorizontalHeaderLabels(names)
        self.result.resizeColumnsToContents()
        self.update_table()

    def edit_table(self):
        self.edit = EditWidget(self)
        
    def update_table(self):
        cof = request()
        self.result.setRowCount(len(cof))
        for i in range(len(cof)):
            self.result.setItem(i, 0, QTableWidgetItem(str(cof[i][0])))
            self.result.setItem(i, 1, QTableWidgetItem(str(cof[i][1])))
            self.result.setItem(i, 2, QTableWidgetItem(str(cof[i][2])))
            is_core = 'Да' if int(cof[i][3]) else 'Нет'
            self.result.setItem(i, 3, QTableWidgetItem(is_core))
            self.result.setItem(i, 4, QTableWidgetItem(str(cof[i][4])))
            self.result.setItem(i, 5, QTableWidgetItem(str(cof[i][5])))
            self.result.setItem(i, 6, QTableWidgetItem(str(cof[i][6])))
        self.result.resizeColumnsToContents()
        self.result.resizeRowsToContents()


class EditWidget(QWidget, Ui_Form):
    def __init__(self, self1):
        super().__init__()
        self.setupUi(self)
        self.self1 = self1
        self.result.setColumnCount(7)
        self.result.setWordWrap(True)
        names = ['id', 'Название', 'Степень обжарки', 'В зернах?', 'Описание вкуса', 'цена (руб/кг)', 'Объем упаковки (грамм)']
        self.result.setHorizontalHeaderLabels(names)
        self.result.resizeColumnsToContents()
        self.update_table()
        self.updateBtn.clicked.connect(self.update_edit)
        self.appendBtn.clicked.connect(self.adding)
        self.show()

    def update_db(self, _id, name, degree, is_core, description, cost, volume):
        con = sqlite3.connect(resource_path('data/coffee.sqlite'))
        cur = con.cursor()
        cur.execute('''UPDATE coffees SET\n name="{}", degree={}, is_core={},
                    description="{}", cost={}, volume={} WHERE id = {}'''.format(name, degree,
                                                                                 is_core, description, cost, volume, str(_id)))
        con.commit()
        con.close()
        self.update_table()
        self.self1.update_table()

    def update_edit(self):
        for i in range(len(self.cof)):
            _id = i + 1
            name = self.result.item(i, 1).text()
            degree = self.result.item(i, 2).text()
            is_core = '1' if self.result.item(i, 3).text() == 'Да' else '0'
            description = self.result.item(i, 4).text()
            cost = self.result.item(i, 5).text()
            volume = self.result.item(i, 6).text()
            self.update_db(_id, name, degree, is_core, description, cost, volume)

    def insert_to_db(self, name, degree, is_core, description, cost, volume):
        con = sqlite3.connect(resource_path('data/coffee.sqlite'))
        cur = con.cursor()
        cur.execute('''INSERT INTO coffees(name, degree,
                is_core, description, cost, volume) values("{}",{},{},"{}",{},{})'''.format(name,
                                                                                            degree, is_core, description, cost, volume))
        con.commit()
        con.close()
        self.update_table()
        self.self1.update_table()

    def update_table(self):
        cof = request()
        self.result.setRowCount(len(cof))
        self.cof = cof
        for i in range(len(cof)):
            self.result.setItem(i, 0, QTableWidgetItem(str(cof[i][0])))
            self.result.setItem(i, 1, QTableWidgetItem(str(cof[i][1])))
            self.result.setItem(i, 2, QTableWidgetItem(str(cof[i][2])))
            is_core = 'Да' if int(cof[i][3]) else 'Нет'
            self.result.setItem(i, 3, QTableWidgetItem(is_core))
            self.result.setItem(i, 4, QTableWidgetItem(str(cof[i][4])))
            self.result.setItem(i, 5, QTableWidgetItem(str(cof[i][5])))
            self.result.setItem(i, 6, QTableWidgetItem(str(cof[i][6])))
        self.result.resizeColumnsToContents()
        self.result.resizeRowsToContents()

    def adding(self):
        name = self.title.toPlainText()
        degree = str(self.degree.value())
        is_core = '1' if self.core.currentText() == 'Да' else '0'
        description = self.description.toPlainText()
        cost = str(self.cost.value())
        volume = str(self.volume.value())
        self.insert_to_db(name, degree, is_core, description, cost, volume)    


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
