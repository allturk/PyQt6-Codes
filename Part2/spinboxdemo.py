# Form implementation generated from reading ui file 'SpinBoxDemo.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class Ui_form(QWidget):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(535, 226)
        self.verticalLayout = QtWidgets.QVBoxLayout(form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(form)
        self.label.setStyleSheet("QLabel{color:purple;font-family:Arial; font:Bold;font-size:16px}")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ledit_pprice = QtWidgets.QLineEdit(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_pprice.sizePolicy().hasHeightForWidth())
        self.ledit_pprice.setSizePolicy(sizePolicy)
        self.ledit_pprice.setObjectName("ledit_pprice")
        self.horizontalLayout.addWidget(self.ledit_pprice)
        self.sbox = QtWidgets.QSpinBox(form)
        self.sbox.setObjectName("sbox")
        self.sbox.editingFinished.connect(self.first_result)
        self.horizontalLayout.addWidget(self.sbox)
        self.ledit_ptotal = QtWidgets.QLineEdit(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_ptotal.sizePolicy().hasHeightForWidth())
        self.ledit_ptotal.setSizePolicy(sizePolicy)
        self.ledit_ptotal.setObjectName("ledit_ptotal")
        self.horizontalLayout.addWidget(self.ledit_ptotal)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(form)
        self.label_2.setStyleSheet("QLabel{color:purple;font-family:Arial; font:Bold;font-size:16px}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ledit_sprice = QtWidgets.QLineEdit(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_sprice.sizePolicy().hasHeightForWidth())
        self.ledit_sprice.setSizePolicy(sizePolicy)
        self.ledit_sprice.setObjectName("ledit_sprice")
        self.horizontalLayout_2.addWidget(self.ledit_sprice)
        self.dsbox = QtWidgets.QDoubleSpinBox(form)
        self.dsbox.setObjectName("dsbox")
        self.dsbox.editingFinished.connect(self.second_result)
        self.horizontalLayout_2.addWidget(self.dsbox)
        self.ledit_stotal = QtWidgets.QLineEdit(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_stotal.sizePolicy().hasHeightForWidth())
        self.ledit_stotal.setSizePolicy(sizePolicy)
        self.ledit_stotal.setObjectName("ledit_stotal")
        self.horizontalLayout_2.addWidget(self.ledit_stotal)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.total_price = QtWidgets.QLabel(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.total_price.sizePolicy().hasHeightForWidth())
        self.total_price.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.total_price.setFont(font)
        self.total_price.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.total_price.setStyleSheet("QLabel{color:blue;font-family:Arial; font:Bold;font-size:16px}")
        self.total_price.setText("")
        self.total_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.total_price.setObjectName("total_price")
        self.verticalLayout.addWidget(self.total_price)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def first_result(self):
        pen_price = int(self.ledit_pprice.text())
        totalpenprice = self.sbox.value() * pen_price
        self.ledit_ptotal.setText(str(totalpenprice))

    def second_result(self):
        sugarPrice = int(self.ledit_sprice.text())
        totalsugarprice = self.dsbox.value() * sugarPrice
        self.ledit_stotal.setText(str(totalsugarprice))

        totalpenprice = int(self.ledit_ptotal.text())
        total = totalsugarprice + totalpenprice
        self.total_price.setText(str(total))

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "SpinBox EditFinished Signal"))
        self.label.setText(_translate("form", "Pen Price:"))
        self.label_2.setText(_translate("form", "Sugar Price:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = Ui_form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec())
