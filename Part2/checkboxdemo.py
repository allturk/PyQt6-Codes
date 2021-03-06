# Form implementation generated from reading ui file 'CheckboxDemo.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(576, 376)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.addStretch(3)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbox_pizza = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbox_pizza.setFont(font)
        self.cbox_pizza.setObjectName("cbox_pizza")

        self.verticalLayout.addWidget(self.cbox_pizza)
        self.cbox_salad = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbox_salad.setFont(font)
        self.cbox_salad.setObjectName("cbox_salad")
        self.verticalLayout.addWidget(self.cbox_salad)
        self.cbox_sausage = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbox_sausage.setFont(font)
        self.cbox_sausage.setObjectName("cbox_sausage")
        self.verticalLayout.addWidget(self.cbox_sausage)
        self.verticalLayout_2.addStretch(5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("QLabel{color:blue;font:bold 16px;font-family:Arial}")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.cbox_sausage.stateChanged.connect(self.check_selected)
        self.cbox_salad.toggled.connect(self.check_selected)
        self.cbox_pizza.toggled.connect(self.check_selected)
        self.verticalLayout_2.addStretch(10)
        self.verticalLayout_2.addWidget(self.label_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Regular Tuna Price: 10"))
        self.label_2.setText(_translate("Dialog", "Select More:"))
        self.cbox_pizza.setText(_translate("Dialog", "Pizza: 3"))
        self.cbox_salad.setText(_translate("Dialog", "Salad: 4"))
        self.cbox_sausage.setText(_translate("Dialog", "Sausage: 2"))
        self.label_3.setText(_translate("Dialog", ""))

    def check_selected(self):
        price = 10
        if self.cbox_pizza.isChecked():
            price += 3
        if self.cbox_salad.isChecked():
            price += 4
        if self.cbox_sausage.isChecked():
            price += 2
        self.label_3.setText(f"Total price is {price}" )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
