import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit


class Ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spanzuratoarea")
        self.setFixedSize(360, 640)


def main():
    app = QApplication(sys.argv)
    ui = Ui()
    ui.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

