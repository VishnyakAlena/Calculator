from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = []
        self.operand_1 = []
        self.operand_2 = []
    def initUI(self):
        self.setGeometry(300, 300, 285, 375)
        self.setWindowTitle("Калькулятор")

        self.label = QLabel(self)
        self.label.setText('0')
        self.label.resize(285, 95)
        self.label.setAlignment(Qt.AlignRight)
        self.label.setContentsMargins(5, 45, 5, 20)
        self.label.setFont(QFont('Arial', 13))

        self.number_7 = QPushButton('7', self)
        self.number_7.resize(50, 50)
        self.number_7.move(5, 100)
        self.number_7.setFont(QFont('Georgia', 14))

        self.number_8 = QPushButton('8', self)
        self.number_8.resize(50, 50)
        self.number_8.move(60, 100)
        self.number_8.setFont(QFont('Georgia', 14))

        self.number_9 = QPushButton('9', self)
        self.number_9.resize(50, 50)
        self.number_9.move(115, 100)
        self.number_9.setFont(QFont('Georgia', 14))

        self.multiplication = QPushButton('*', self)
        self.multiplication.resize(50, 50)
        self.multiplication.move(170, 100)
        self.multiplication.setFont(QFont('Georgia', 14))

        self.percent_sign = QPushButton('%', self)
        self.percent_sign.resize(50, 50)
        self.percent_sign.move(225, 100)
        self.percent_sign.setFont(QFont('Georgia', 14))

        self.number_4 = QPushButton('4', self)
        self.number_4.resize(50, 50)
        self.number_4.move(5, 155)
        self.number_4.setFont(QFont('Georgia', 14))

        self.number_5 = QPushButton('5', self)
        self.number_5.resize(50, 50)
        self.number_5.move(60, 155)
        self.number_5.setFont(QFont('Georgia', 14))

        self.number_6 = QPushButton('6', self)
        self.number_6.resize(50, 50)
        self.number_6.move(115, 155)
        self.number_6.setFont(QFont('Georgia', 14))

        self.division = QPushButton('/', self)
        self.division.resize(50, 50)
        self.division.move(170, 155)
        self.division.setFont(QFont('Georgia', 14))

        self.square_root_sign = QPushButton('√', self)
        self.square_root_sign.resize(50, 50)
        self.square_root_sign.move(225, 155)
        self.square_root_sign.setFont(QFont('Georgia', 14))

        self.number_1 = QPushButton('1', self)
        self.number_1.resize(50, 50)
        self.number_1.move(5, 210)
        self.number_1.setFont(QFont('Georgia', 14))

        self.number_2 = QPushButton('2', self)
        self.number_2.resize(50, 50)
        self.number_2.move(60, 210)
        self.number_2.setFont(QFont('Georgia', 14))

        self.number_3 = QPushButton('3', self)
        self.number_3.resize(50, 50)
        self.number_3.move(115, 210)
        self.number_3.setFont(QFont('Georgia', 14))

        self.plus = QPushButton('+', self)
        self.plus.resize(50, 50)
        self.plus.move(170, 210)
        self.plus.setFont(QFont('Georgia', 14))

        self.root_sign = QPushButton('x√', self)
        self.root_sign.resize(50, 50)
        self.root_sign.move(225, 210)
        self.root_sign.setFont(QFont('Georgia', 12))

        self.number_0 = QPushButton('0', self)
        self.number_0.resize(50, 50)
        self.number_0.move(5, 265)
        self.number_0.setFont(QFont('Georgia', 14))

        self.dot_sign = QPushButton('.', self)
        self.dot_sign.resize(50, 50)
        self.dot_sign.move(60, 265)
        self.dot_sign.setFont(QFont('Georgia', 14))

        self.c = QPushButton('C', self)
        self.c.resize(50, 50)
        self.c.move(115, 265)
        self.c.setFont(QFont('Georgia', 14))

        self.minus = QPushButton('-', self)
        self.minus.resize(50, 50)
        self.minus.move(170, 265)
        self.minus.setFont(QFont('Georgia', 14))

        self.degree = QPushButton('x^y', self)
        self.degree.resize(50, 50)
        self.degree.move(225, 265)
        self.degree.setFont(QFont('Georgia', 10))

        self.ravno = QPushButton('=', self)
        self.ravno.resize(105, 50)
        self.ravno.move(5, 320)
        self.ravno.setFont(QFont('Georgia', 14))

        self.remainder_sign = QPushButton('x%y', self)
        self.remainder_sign.resize(50, 50)
        self.remainder_sign.move(115, 320)
        self.remainder_sign.setFont(QFont('Georgia', 10))

        self.integer_division_sign = QPushButton('x//y', self)
        self.integer_division_sign.resize(50, 50)
        self.integer_division_sign.move(170, 320)
        self.integer_division_sign.setFont(QFont('Georgia', 10))

        self.square_degree = QPushButton('x^2', self)
        self.square_degree.resize(50, 50)
        self.square_degree.move(225, 320)
        self.square_degree.setFont(QFont('Georgia', 10))

        self.number_1.clicked.connect(self.one)
        self.number_2.clicked.connect(self.two)
        self.number_3.clicked.connect(self.three)
        self.number_4.clicked.connect(self.four)
        self.number_5.clicked.connect(self.five)
        self.number_6.clicked.connect(self.six)
        self.number_7.clicked.connect(self.seven)
        self.number_8.clicked.connect(self.eight)
        self.number_9.clicked.connect(self.nine)
        self.number_0.clicked.connect(self.zero)
        self.dot_sign.clicked.connect(self.dot)
        self.plus.clicked.connect(self.sum)
        self.minus.clicked.connect(self.difference)
        self.multiplication.clicked.connect(self.product_of_numbers)
        self.division.clicked.connect(self.quotient_of_numbers)
        self.degree.clicked.connect(self.exponentiation)
        self.root_sign.clicked.connect(self.root_of_a_number)
        self.ravno.clicked.connect(self.result)
        self.c.clicked.connect(self.clean)
        self.remainder_sign.clicked.connect(self.remainder_of_the_division)
        self.integer_division_sign.clicked.connect(self.integer_division)
        self.square_root_sign.clicked.connect(self.square_root)
        self.square_degree.clicked.connect(self.squaring)
        self.percent_sign.clicked.connect(self.percent)
    def enterValue(self):
        if self.label.text() == '0':
            self.label.setText('')
        if len(self.label.text()) < 19:
            self.label.setText(self.label.text() + self.my_input)
    def one(self):
        self.my_input = '1'
        self.enterValue()
    def two(self):
        self.my_input = '2'
        self.enterValue()
    def three(self):
        self.my_input = '3'
        self.enterValue()
    def four(self):
        self.my_input = '4'
        self.enterValue()
    def five(self):
        self.my_input = '5'
        self.enterValue()
    def six(self):
        self.my_input = '6'
        self.enterValue()
    def seven(self):
        self.my_input = '7'
        self.enterValue()
    def eight(self):
        self.my_input = '8'
        self.enterValue()
    def nine(self):
        self.my_input = '9'
        self.enterValue()
    def zero(self):
        self.my_input = '0'
        self.enterValue()
    def dot(self):
        self.my_input = '.'
        self.enterValue()
    def sum(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def difference(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def product_of_numbers(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def quotient_of_numbers(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def exponentiation(self):
        self.operation = 'x^y'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def root_of_a_number(self):
        self.operation = 'x√'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def remainder_of_the_division(self):
        self.operation = 'x%y'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def integer_division(self):
        self.operation = 'x//y'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def square_root(self):
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.rezult = self.operand_1 ** (1 / 2)
        self.label.setText(str(self.rezult))
    def squaring(self):
        self.operation = 'x^2'
        self.operand_1 = float(self.label.text())
        self.rezult = self.operand_1 ** 2
        self.label.setText(str(self.rezult))
    def percent(self):
        self.operation = '%'
        self.operand_1 = float(self.label.text())
        self.rezult = self.operand_1 / 100
        self.label.setText(str(self.rezult))
    def result(self):
        self.operand_2 = float(self.label.text())
        if self.operation == '+':
            self.rezult = self.operand_1 + self.operand_2
        elif self.operation == '+' and self.operation == '%':
            self.rezult = self.operand_1 + (self.operand_2 / 100)
        elif self.operation == '-':
            self.rezult = self.operand_1 - self.operand_2
        elif self.operation == '*':
            self.rezult = self.operand_1 * self.operand_2
        elif self.operation == '/':
            if self.operand_2 == 0:
                self.rezult = 'error'
            else:
                self.rezult = self.operand_1 / self.operand_2
        elif self.operation == 'x^y':
            self.rezult = self.operand_1 ** self.operand_2
        elif self.operation == 'x√':
            self.rezult = self.operand_1 ** (1 / self.operand_2)
        elif self.operation == 'x%y':
            if self.operand_2 == 0:
                self.rezult = 'error'
            else:
                self.rezult = self.operand_1 % self.operand_2
        elif self.operation == 'x//y':
            if self.operand_2 == 0:
                self.rezult = 'error'
            else:
                self.rezult = self.operand_1 // self.operand_2
        self.label.setText(str(self.rezult))
    def clean(self):
        self.label.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())