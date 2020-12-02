import sys, random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QGridLayout, QPushButton


class Ui(QMainWindow):
    def create_keyboard(self):
        buttonsLayout = QGridLayout()
        self.buttons = {
            'Q': (0, 0),
            'W': (0, 1),
            'E': (0, 2),
            'R': (0, 3),
            'T': (0, 4),
            'Y': (0, 5),
            'I': (0, 6),
            'O': (0, 7),
            'P': (0, 8),
            'A': (1, 0),
            'S': (1, 1),
            'D': (1, 2),
            'F': (1, 3),
            'G': (1, 4),
            'H': (1, 5),
            'J': (1, 6),
            'K': (1, 7),
            'L': (1, 8),
            'Z': (2, 2),
            'X': (2, 3),
            'C': (2, 4),
            'V': (2, 5),
            'B': (2, 6),
            'N': (2, 7),
            'M': (2, 8),
        }
        for btnText, pos in self.buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        self.generalLayout.addLayout(buttonsLayout)

    def create_word(self):
        words = ["Lamaie", "mancare", "pepsi", "sexy", "placere"]
        choice = random.randint(0, len(words))
        word = words[choice]
        l1 = QLabel



    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spanzuratoarea")
        self.setFixedSize(360, 640)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget()
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self.create_keyboard()

def main():
    app = QApplication(sys.argv)
    ui = Ui()
    ui.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

