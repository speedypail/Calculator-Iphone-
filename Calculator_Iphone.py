import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Calculator")
        self.setFixedSize(320, 420)
        self.setStyleSheet("background-color: #2c2c2c;")  

        
        self.main_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        
        self.display = QLineEdit()
        self.display.setFixedHeight(60)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("background-color: #1e1e1e; color: #fff; font-size: 24px; border: none; padding: 10px;")
        
       
        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), '.': (3, 1), '=': (3, 2), '+': (3, 3),
        }

        
        operator_style = "background-color: #ff9500; color: white; font-size: 18px;"
        number_style = "background-color: #333333; color: white; font-size: 18px;"
        equals_style = "background-color: #ff3b30; color: white; font-size: 18px;"

       
        for button_text, pos in buttons.items():
            button = QPushButton(button_text)
            button.setFixedSize(70, 70)
            if button_text in ['+', '-', '*', '/']:
                button.setStyleSheet(operator_style)
            elif button_text == '=':
                button.setStyleSheet(equals_style)
            else:
                button.setStyleSheet(number_style)
            self.grid_layout.addWidget(button, pos[0], pos[1])
            button.clicked.connect(self.on_button_click)

        
        self.clear_button = QPushButton('C')
        self.clear_button.setFixedSize(70, 70)
        self.clear_button.setStyleSheet("background-color: #ffcc00; color: black; font-size: 18px;")
        self.grid_layout.addWidget(self.clear_button, 4, 0, 1, 4)
        self.clear_button.clicked.connect(self.clear_display)

        
        self.main_layout.addWidget(self.display)
        self.main_layout.addLayout(self.grid_layout)
        self.setLayout(self.main_layout)

    def on_button_click(self):
        button = self.sender()
        button_text = button.text()

        if button_text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + button_text)

    def clear_display(self):
        self.display.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
