import function,tasarim
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class degisken():
    sifre = ""
    e = 0

def sifrele():
    gelenDegerler = fc.sifrele(ui.line_mesaj.text())
    dg.sifre = gelenDegerler[0]
    dg.e = gelenDegerler[1]

    ui.lbl_sifre.setText(str(dg.sifre))


def desifrele():
    fc.desifrele(dg.sifre, dg.e)

if __name__ == "__main__":


    dg = degisken()
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = tasarim.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    fc = function.func(ui)

    ui.btn_sifrele.clicked.connect(sifrele)
    ui.btn_sifreCoz.clicked.connect(desifrele)


    sys.exit(app.exec_())