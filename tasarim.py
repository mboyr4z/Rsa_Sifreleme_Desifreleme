

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(539, 238)

        self.lbl_Tum = QtWidgets.QLabel(Form)
        self.lbl_Tum.setGeometry(0,0,539,238)
        self.lbl_Tum.setObjectName("lbl_Tum")

        self.lbl_mesajAd = QtWidgets.QLabel(Form)
        self.lbl_mesajAd.setGeometry(QtCore.QRect(240, 6, 41, 16))
        self.lbl_mesajAd.setObjectName("lbl_mesajAd")

        self.line_mesaj = QtWidgets.QLineEdit(Form)
        self.line_mesaj.setGeometry(QtCore.QRect(282, 6, 121, 21))
        self.line_mesaj.setObjectName("line_mesaj")

        self.btn_sifrele = QtWidgets.QPushButton(Form)
        self.btn_sifrele.setGeometry(QtCore.QRect(420, 5, 111, 23))
        self.btn_sifrele.setObjectName("btn_sifrele")

        self.btn_sifreCoz = QtWidgets.QPushButton(Form)
        self.btn_sifreCoz.setGeometry(QtCore.QRect(420, 30, 111, 23))
        self.btn_sifreCoz.setObjectName("btn_sifreCoz")

        self.lbl_pAd = QtWidgets.QLabel(Form)
        self.lbl_pAd.setGeometry(QtCore.QRect(10, 55, 21, 16))
        self.lbl_pAd.setObjectName("lbl_pAd")

        self.lbl_qAd = QtWidgets.QLabel(Form)
        self.lbl_qAd.setGeometry(QtCore.QRect(10, 85, 21, 16))
        self.lbl_qAd.setObjectName("lbl_qAd")

        self.lbl_nAd = QtWidgets.QLabel(Form)
        self.lbl_nAd.setGeometry(QtCore.QRect(10, 115, 21, 16))
        self.lbl_nAd.setObjectName("lbl_nAd")

        self.lbl_eAd = QtWidgets.QLabel(Form)
        self.lbl_eAd.setGeometry(QtCore.QRect(10, 145, 21, 16))
        self.lbl_eAd.setObjectName("lbl_eAd")

        self.lbl_fiAd = QtWidgets.QLabel(Form)
        self.lbl_fiAd.setGeometry(QtCore.QRect(10, 175, 21, 16))
        self.lbl_fiAd.setObjectName("lbl_fiAd")

        self.lbl_dAd = QtWidgets.QLabel(Form)
        self.lbl_dAd.setGeometry(QtCore.QRect(10, 205, 21, 16))
        self.lbl_dAd.setObjectName("lbl_dAd")

        self.lbl_p = QtWidgets.QLabel(Form)
        self.lbl_p.setGeometry(QtCore.QRect(30, 56, 50, 16))
        self.lbl_p.setObjectName("lbl_p")

        self.lbl_q = QtWidgets.QLabel(Form)
        self.lbl_q.setGeometry(QtCore.QRect(30, 86, 50, 16))
        self.lbl_q.setObjectName("lbl_q")

        self.lbl_n = QtWidgets.QLabel(Form)
        self.lbl_n.setGeometry(QtCore.QRect(30, 116, 50, 16))
        self.lbl_n.setObjectName("lbl_n")

        self.lbl_e = QtWidgets.QLabel(Form)
        self.lbl_e.setGeometry(QtCore.QRect(30, 146, 50, 16))
        self.lbl_e.setObjectName("lbl_e")

        self.lbl_fi = QtWidgets.QLabel(Form)
        self.lbl_fi.setGeometry(QtCore.QRect(30, 176, 50, 16))
        self.lbl_fi.setObjectName("lbl_fi")

        self.lbl_d = QtWidgets.QLabel(Form)
        self.lbl_d.setGeometry(QtCore.QRect(30, 206, 50, 16))
        self.lbl_d.setObjectName("lbl_d")

        self.text_yazi = QtWidgets.QTextBrowser(Form)
        self.text_yazi.setGeometry(QtCore.QRect(110, 60, 420, 170))
        self.text_yazi.setObjectName("text_yazi")

        self.lbl_sifre = QtWidgets.QLabel(Form)
        self.lbl_sifre.setGeometry(QtCore.QRect(130, 32, 281, 21))
        self.lbl_sifre.setObjectName("lbl_sifre")
        self.lbl_sifre.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.lbl_sifreAd = QtWidgets.QLabel(Form)
        self.lbl_sifreAd.setGeometry(QtCore.QRect(110, 30, 35, 20))
        self.lbl_sifreAd.setObjectName("lbl_sifreAd")

        Form.setStyleSheet(open("still.qss", "r").read())


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RSA Şifreleme"))
        self.lbl_mesajAd.setText(_translate("Form", "Mesaj :"))
        self.btn_sifrele.setText(_translate("Form", "Şifrele"))
        self.lbl_pAd.setText(_translate("Form", "p : "))
        self.lbl_qAd.setText(_translate("Form", "q :"))
        self.lbl_nAd.setText(_translate("Form", "n : "))
        self.lbl_eAd.setText(_translate("Form", "e :"))
        self.lbl_fiAd.setText(_translate("Form", "fi :"))
        self.lbl_dAd.setText(_translate("Form", "d :"))
        self.lbl_p.setText(_translate("Form", "00"))
        self.lbl_q.setText(_translate("Form", "00"))
        self.lbl_n.setText(_translate("Form", "00"))
        self.lbl_e.setText(_translate("Form", "00"))
        self.lbl_fi.setText(_translate("Form", "00"))
        self.lbl_d.setText(_translate("Form", "00"))
        self.btn_sifreCoz.setText(_translate("Form", "Şifreyi Çöz"))
        self.lbl_sifre.setText(_translate("Form", "*************************************"))
        self.lbl_sifreAd.setText(_translate("Form", "Şifre :"))

