from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

# create a data base or connect to one
conn = sqlite3.connect('ab.db')
# create a cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE if not exists tone(
    first_name text,
    last_name text,
    phone_number integer,
    email_address text,
    address text
    )""")

# commit our changes
conn.commit()

# close our connection
conn.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 653)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fn_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.fn_lineedit.setGeometry(QtCore.QRect(40, 60, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.fn_lineedit.setFont(font)
        self.fn_lineedit.setObjectName("fn_lineedit")
        self.ln_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_lineedit.setGeometry(QtCore.QRect(40, 150, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ln_lineedit.setFont(font)
        self.ln_lineedit.setObjectName("ln_lineedit")
        self.pn_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.pn_lineedit.setGeometry(QtCore.QRect(40, 240, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pn_lineedit.setFont(font)
        self.pn_lineedit.setObjectName("pn_lineedit")
        self.ea_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.ea_lineedit.setGeometry(QtCore.QRect(40, 330, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ea_lineedit.setFont(font)
        self.ea_lineedit.setObjectName("ea_lineedit")
        self.fn_label = QtWidgets.QLabel(self.centralwidget)
        self.fn_label.setGeometry(QtCore.QRect(40, 20, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.fn_label.setFont(font)
        self.fn_label.setObjectName("fn_label")
        self.ln_label = QtWidgets.QLabel(self.centralwidget)
        self.ln_label.setGeometry(QtCore.QRect(40, 110, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ln_label.setFont(font)
        self.ln_label.setObjectName("ln_label")
        self.pn_label = QtWidgets.QLabel(self.centralwidget)
        self.pn_label.setGeometry(QtCore.QRect(40, 200, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pn_label.setFont(font)
        self.pn_label.setObjectName("pn_label")
        self.ea_label = QtWidgets.QLabel(self.centralwidget)
        self.ea_label.setGeometry(QtCore.QRect(40, 290, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ea_label.setFont(font)
        self.ea_label.setObjectName("ea_label")
        self.a_label = QtWidgets.QLabel(self.centralwidget)
        self.a_label.setGeometry(QtCore.QRect(40, 380, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.a_label.setFont(font)
        self.a_label.setObjectName("a_label")
        self.a_textedit = QtWidgets.QTextEdit(self.centralwidget)
        self.a_textedit.setGeometry(QtCore.QRect(40, 420, 201, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.a_textedit.setFont(font)
        self.a_textedit.setObjectName("a_textedit")
        self.add_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.add_it())
        self.add_pushbutton.setGeometry(QtCore.QRect(40, 550, 111, 61))
        self.add_pushbutton.setObjectName("add_pushbutton")
        self.update_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.open_it())
        self.update_pushbutton.setGeometry(QtCore.QRect(170, 550, 111, 61))
        self.update_pushbutton.setObjectName("update_pushbutton")
        self.delete_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.delete_it())
        self.delete_pushbutton.setGeometry(QtCore.QRect(300, 550, 111, 61))
        self.delete_pushbutton.setObjectName("delete_pushbutton")
        self.close_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.update_it())
        self.close_pushbutton.setGeometry(QtCore.QRect(430, 550, 111, 61))
        self.close_pushbutton.setObjectName("close_pushbutton")
        self.save_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.close_it())
        self.save_pushbutton.setGeometry(QtCore.QRect(560, 550, 111, 61))
        self.save_pushbutton.setObjectName("save_pushbutton")
        self.i_listwidget = QtWidgets.QListWidget(self.centralwidget)
        self.i_listwidget.setGeometry(QtCore.QRect(330, 60, 341, 471))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.i_listwidget.setFont(font)
        self.i_listwidget.setObjectName("i_listwidget")
        self.i_label = QtWidgets.QLabel(self.centralwidget)
        self.i_label.setGeometry(QtCore.QRect(330, 20, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.i_label.setFont(font)
        self.i_label.setObjectName("i_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # grabb all the items from the database
        self.grab_all()
        self.disable()
        self.disable_u()
        self.disable_dd()
        self.disable_c()
        self.close_pushbutton.setEnabled(False)
        self.save_pushbutton.setEnabled(False)



    def cls(self):
        self.save_pushbutton.setEnabled(False)


    def disable(self):

    # create a data base or connect to one
        conn = sqlite3.connect('ab.db')
        # create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM tone")

        records = c.fetchall()

        conn.commit()
        conn.close()

        if not records:
            self.update_pushbutton.setEnabled(False)
        else:
            pass

    def disable_u(self):

    # create a data base or connect to one
        conn = sqlite3.connect('ab.db')
        # create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM tone")

        records = c.fetchall()

        conn.commit()
        conn.close()

        if not records:
            self.close_pushbutton.setEnabled(False)
        else:
            pass

    def disable_dd(self):

    # create a data base or connect to one
        conn = sqlite3.connect('ab.db')
        # create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM tone")

        records = c.fetchall()

        conn.commit()
        conn.close()

        if not records:
            self.delete_pushbutton.setEnabled(False)
        else:
            pass


    def disable_c(self):

    # create a data base or connect to one
        conn = sqlite3.connect('ab.db')
        # create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM tone")

        records = c.fetchall()

        conn.commit()
        conn.close()

        if not records:
            self.save_pushbutton.setEnabled(False)
        else:
            pass
        



     # Add item to list
    def add_it(self):

        # create a data base or connect to one
        conn = sqlite3.connect('ab.db')
        # create a cursor
        c = conn.cursor()

        item1 = self.fn_lineedit.text()
        item2 = self.ln_lineedit.text()
        item3 = self.pn_lineedit.text()
        item4 = self.ea_lineedit.text()
        item5 = self.a_textedit.toPlainText()

        if self.fn_lineedit.text() == '':
            msg = QMessageBox()
            msg.setWindowTitle("!!!")
            msg.setText("The first name is mandatory!")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
        else:
            self.i_listwidget.addItem(str(item1))




            # add item to list
            # clear the item box
            self.fn_lineedit.setText("")
            self.ln_lineedit.setText("")
            self.pn_lineedit.setText("")
            self.ea_lineedit.setText("")
            self.a_textedit.setText("")

            
            self.disable()
            self.disable_u()
            self.disable_dd()
            self.disable_c()
            


            items = []
            # loop through the list widget and pull out each item
            for index in range(self.i_listwidget.count()):
                items.append(self.i_listwidget.item(index))

            

            c.execute('''INSERT INTO tone(first_name, last_name, phone_number, email_address, address)
                                        VALUES (?, ?, ?, ?, ?)''',
                                        ( item1, 
                                          item2,
                                          item3,
                                          item4,
                                          item5)
                                    )


            self.update_pushbutton.setEnabled(True)
            self.close_pushbutton.setEnabled(False)
            self.delete_pushbutton.setEnabled(True)
            self.save_pushbutton.setEnabled(False)

            
            conn.commit()

            conn.close()

            # pop up box
            msg = QMessageBox()
            msg.setWindowTitle("Added your contact!!!")
            msg.setText("Your contact has been added!")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()



    def open_it(self):
        # create a data base or connect to one
        conn = sqlite3.connect('ab.db')
        # create a cursor
        c = conn.cursor()

        global symbol

        # grab the selected row
        symbol = self.i_listwidget.currentItem().text()

        # symbol = "Humaira";

        c.execute("SELECT * FROM tone WHERE first_name = '%s'" % symbol)


        result = c.fetchall()

        self.disable()
        self.disable_dd()
        self.disable_u()
        self.disable_c()
        self.close_pushbutton.setEnabled(True)
        self.save_pushbutton.setEnabled(True)
            


        for results in result:
            a = (results[0])
            b = (results[1])
            c = (results[2])
            d = (results[3])
            e = (results[4])
            
        self.fn_lineedit.setText(str(a))
        self.ln_lineedit.setText(str(b))
        self.pn_lineedit.setText(str(c))
        self.ea_lineedit.setText(str(d))
        self.a_textedit.setText(str(e))

        
        conn.commit()

        conn.close()
    

    def grab_all(self):
        # Create a database or connect to one
        conn = sqlite3.connect('ab.db')
        # Create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM tone")

        global records

        records = c.fetchall()

        # commit the changes
        conn.commit()

        # close our connection
        conn.close()

        # loop thru records and add to screen
        for record in records:
            self.i_listwidget.addItem(str(record[0]))
            

        print(records)


        

    def delete_it(self):

            
        something = self.i_listwidget.currentItem()

        if something == None:
            # pop up box
            msg = QMessageBox()
            msg.setWindowTitle("!!!")
            msg.setText("You have to select something!")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        else:

            symbol = self.i_listwidget.currentItem().text()
        
            msgBox = QMessageBox()
            msgBox.setWindowTitle("!!!")
            msgBox.setText("Are you sure you want to delete " + symbol + "?")
            msgBox.setStandardButtons(QMessageBox.Yes)
            msgBox.addButton(QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.No)

            if(msgBox.exec() == QMessageBox.Yes):
                # create a data base or connect to one
                conn = sqlite3.connect('ab.db')
                # create a cursor
                c = conn.cursor()


                c.execute("DELETE FROM tone WHERE first_name = '%s'" % symbol)

                
                clicked = self.i_listwidget.currentRow()
                self.i_listwidget.takeItem(clicked)

                

                # commit the changes
                conn.commit()

                # close our connection
                conn.close() 

                # clear the item box
                self.fn_lineedit.setText("")
                self.ln_lineedit.setText("")
                self.pn_lineedit.setText("")
                self.ea_lineedit.setText("")
                self.a_textedit.setText("")

                self.close_pushbutton.setEnabled(False)
                self.save_pushbutton.setEnabled(False)

                self.disable()
                self.disable_dd()
                self.disable_u()
                self.disable_c()
            else:

                pass
        
    def close_it(self):
        
        # Create a database or connect to one
        conn = sqlite3.connect('ab.db')
        # Create a cursor
        c = conn.cursor()

        # clear the item box
        self.fn_lineedit.setText("")
        self.ln_lineedit.setText("")
        self.pn_lineedit.setText("")
        self.ea_lineedit.setText("")
        self.a_textedit.setText("")

        self.close_pushbutton.setEnabled(False)
        #self.disable()
        self.disable_dd()
        self.disable_u()
        self.disable_c()
        self.cls()
        
        # commit the changes
        conn.commit()

        # close our connection
        conn.close()
    
    def update_it(self):

        # create a data base or connect to one
        conn = sqlite3.connect('ab.db')
        # create a cursor
        c = conn.cursor()


        aa = self.fn_lineedit.text()
        cc = self.pn_lineedit.text()
        bb = self.ln_lineedit.text()
        dd = self.ea_lineedit.text()
        ee = self.a_textedit.toPlainText()

        c.execute("""
            UPDATE tone
            SET first_name=?, last_name=?, phone_number=?, email_address=?, address=?
            WHERE first_name=?
            """, (aa, bb, cc, dd, ee, symbol))

        self.disable()
        self.disable_dd()
        self.disable_u()
        self.disable_c()
        self.i_listwidget.clear()

        # commit the changes
        conn.commit()

        # close our connection
        conn.close()

        self.grab_all()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fn_label.setText(_translate("MainWindow", "First Name"))
        self.ln_label.setText(_translate("MainWindow", "Last Name"))
        self.pn_label.setText(_translate("MainWindow", "Phone Number:"))
        self.ea_label.setText(_translate("MainWindow", "Email Address"))
        self.a_label.setText(_translate("MainWindow", "Address"))
        self.add_pushbutton.setText(_translate("MainWindow", "Add"))
        self.update_pushbutton.setText(_translate("MainWindow", "Open"))
        self.delete_pushbutton.setText(_translate("MainWindow", "Delete"))
        self.close_pushbutton.setText(_translate("MainWindow", "Update"))
        self.save_pushbutton.setText(_translate("MainWindow", "Close"))
        self.i_label.setText(_translate("MainWindow", "Information"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())