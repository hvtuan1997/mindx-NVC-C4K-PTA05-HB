# khai báo thư viện
from PyQt6.QtWidgets import QApplication, QWidget
import sys

# tạo ứng dụng
app = QApplication(sys.argv)

# tạo cửa sổ chính
window = QWidget(windowTitle="Hello World")
window.show()

# khởi động vòng lặp sự kiện
app.exec()
