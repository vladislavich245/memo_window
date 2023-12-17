from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QTableWidget,QListWidget,QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout,QVBoxLayout,
        QGroupBox,QButtonGroup,QRadioButton,
        QPushButton,QLabel,QSpinBox)


app = QApplication()


btn_Menu = QPushButton('Меню')
btn_Sleep = QPushButton('Відпочити')
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
btn_OK  = QPushButton('Відповісти')
lb_Question = QLabel('')


RadioGroupBox = QGroupBox('Варіанти відповідей')
RadioGroup = QButtonGroup()


rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)