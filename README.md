# Class code
* Code: NVC-C4K-PTA05-HB
* Khối K12 - Năm 3: App Producer - Học phần: Advanced
# Teacher
* Họ tên: Hoàng Văn Tuân
# Installation
```bash
pip install PyQt6
```
# Convert from file_giao_dien.ui to file_chay.py
* Bước 1: Chuyển từ file_giao_dien.ui thành file_giao_dien.py
```bash
pyuic6 -o file_giao_dien.py file_giao_dien.ui
```
* Bước 2: Tạo file_chay.py từ file_giao_dien.py
```bash
import sys
from PyQt6.QtWidgets import QWidget, QApplication

from file_giao_dien import Ui_Form


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


# chuong trinh chinh
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

```
* Bước 3: Chạy file_chay.py
```bash
python file_chay.py
```
