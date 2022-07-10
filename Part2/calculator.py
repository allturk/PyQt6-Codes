# Form implementation generated from reading ui file 'Calc.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(479, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lnEd_first = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lnEd_first.setFont(font)
        self.lnEd_first.setObjectName("lnEd_first")
        self.horizontalLayout.addWidget(self.lnEd_first)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Preferred,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lnEd_snd = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lnEd_snd.setFont(font)
        self.lnEd_snd.setObjectName("lnEd_snd")
        self.horizontalLayout_2.addWidget(self.lnEd_snd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_add = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.btn_add.clicked.connect(self.add)
        self.horizontalLayout_3.addWidget(self.btn_add)
        self.btn_sub = QtWidgets.QPushButton(Form)
        self.btn_sub.clicked.connect(self.sub)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_sub.setFont(font)
        self.btn_sub.setObjectName("btn_sub")
        self.horizontalLayout_3.addWidget(self.btn_sub)
        self.btn_mul = QtWidgets.QPushButton(Form)
        self.btn_mul.clicked.connect(self.mul)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mul.setFont(font)
        self.btn_mul.setObjectName("btn_mul")
        self.horizontalLayout_3.addWidget(self.btn_mul)
        self.btn_div = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.btn_div.clicked.connect(self.div)
        self.horizontalLayout_3.addWidget(self.btn_div)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.lbl_result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_result.setFont(font)
        self.lbl_result.setStyleSheet("QLabel{color:blue}")
        self.lbl_result.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_result.setObjectName("lbl_result")
        self.verticalLayout.addWidget(self.lbl_result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def add(self):
        first_number = float(self.lnEd_first.text())
        second_number = float(self.lnEd_snd.text())
        result = first_number + second_number
        self.lbl_result.setText(str(result))

    def sub(self):
        first_number = float(self.lnEd_first.text())
        second_number = float(self.lnEd_snd.text())
        result = first_number - second_number
        self.lbl_result.setText(str(result))

    def mul(self):
        first_number = float(self.lnEd_first.text())
        second_number = float(self.lnEd_snd.text())
        result = first_number * second_number
        self.lbl_result.setText(f"{result}")

    def div(self):
        first_number = float(self.lnEd_first.text())
        second_number = float(self.lnEd_snd.text())
        result = "%.3f"%(first_number / second_number)
        self.lbl_result.setText("{}".format(result))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "First Number :"))
        self.lnEd_first.setPlaceholderText(_translate("Form", "Please enter first number"))
        self.label_2.setText(_translate("Form", "Second Number :"))
        self.lnEd_snd.setPlaceholderText(_translate("Form", "Please enter second number"))
        self.btn_add.setText(_translate("Form", "+"))
        self.btn_sub.setText(_translate("Form", "-"))
        self.btn_mul.setText(_translate("Form", "x"))
        self.btn_div.setText(_translate("Form", "/"))
        self.lbl_result.setText(_translate("Form", "..."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
