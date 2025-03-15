import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtWidgets import QMessageBox

from su_kien import Ui_Form


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.btnThayDoi.clicked.connect(self.xu_ly_thoat)

    def xu_ly_thoat(self):
        reply = QMessageBox.question(
            self,
            "Xác nhận thoát chương trình",
            "Bạn có chắc chắn muốn thoát hay không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            QApplication.quit()
        else:
            QMessageBox.information(self, "Thông báo", "Bạn đã không đóng ứng dụng")


# chuong trinh chinh
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
