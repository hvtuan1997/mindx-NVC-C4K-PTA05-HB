import sys
from PyQt6.QtWidgets import QWidget, QApplication

from su_kien import Ui_Form


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.btnThayDoi.clicked.connect(self.doi_gia_tri)

    def doi_gia_tri(self):
        self.ui.lblKetQua.setText("Toi thich hoc lap trinh Python")

    # su kien khi nhan phim tren ban phim
    def keyPressEvent(self, a0):
        self.ui.lblKetQua.setText("Phim " + str(a0.text()) + " duoc bam")


# chuong trinh chinh
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
