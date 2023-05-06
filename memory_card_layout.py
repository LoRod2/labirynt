from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QHBoxLayout, QVBoxLayout, QBoxLayout, QLabel , QRadioButton, QGroupBox, QPushButton, QTableWidget,QListWidget, QSpinBox, QFormLayout

app = QApplication([])


#Віджети
btn_menu = QPushButton("Меню")
btn_sleep = QPushButton("Відпочити")
box_Minutes = QSpinBox()
box_Minutes.setValue(2)
btn_OK = QPushButton("Відповісти")
lb_question = QLabel("")

#Панель відповіді
RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()
rbtn_1 = QRadioButton("1")
rbtn_2 = QRadioButton("2")
rbtn_3 = QRadioButton("3")
rbtn_4 = QRadioButton("4")

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

#Панель результату
Answ_GroupBox = QGroupBox("Результати тесту")
lb_Result = QLabel("")
lb_Correct = QLabel("")

#Розміщення
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

#Розміщення результату
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignCenter,stretch = 2)
Answ_GroupBox.setLayout(layout_res)
Answ_GroupBox.hide()

#Розміщення всіх віджетів
layout_Line1 = QHBoxLayout()
layout_Line2 = QHBoxLayout()
layout_Line3 = QHBoxLayout()
layout_Line4 = QHBoxLayout()

layout_Line1.addWidget(btn_menu)
layout_Line1.addStretch(1)
layout_Line1.addWidget(btn_sleep)
layout_Line1.addWidget(box_Minutes)
layout_Line1.addWidget(QLabel("Хвилини"))

layout_Line2.addWidget(lb_question,alignment = (Qt.AlignHCenter| Qt.AlignVCenter))

layout_Line3.addWidget(RadioGroupBox)
layout_Line3.addWidget(Answ_GroupBox)

layout_Line4.addStretch(1)
layout_Line4.addWidget(btn_OK)
layout_Line4.addStretch(1)

#Головна лінія
layout_card = QVBoxLayout()

layout_card.addLayout(layout_Line1)
layout_card.addLayout(layout_Line2)
layout_card.addLayout(layout_Line3)
layout_card.addStretch(1)
layout_card.addLayout(layout_Line4)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    Answ_GroupBox.show()
    btn_OK.setText("Наступне питання")
def show_question():
    RadioGroupBox.show()
    Answ_GroupBox.hide()
    btn_OK.setText("Відповісти")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)




