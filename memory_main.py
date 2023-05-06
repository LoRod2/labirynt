from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QHBoxLayout, QVBoxLayout, QBoxLayout, QLabel , QRadioButton, QGroupBox

app = QApplication([])
main_win = QWidget()
main_win.setWindowText = ("Memory Card")
main_win.resize(600,500)

radiogroupbox = QGroupBox("Варіанти відповідей")
radiogroup = QButtonGroup()

rbtn1 = QRadioButton("1")
rbtn2 = QRadioButton("2")
rbtn3 = QRadioButton("3")
rbtn4 = QRadioButton("4")

radiogroup.addButton(rbtn1)
radiogroup.addButton(rbtn2)
radiogroup.addButton(rbtn3)
radiogroup.addButton(rbtn4)

main_layout = QHBoxLayout()
layoutV1 = QVBoxLayout()
layoutV2 = QVBoxLayout()
layoutV3 = QVBoxLayout()
layoutV4 = QVBoxLayout()


layoutV1.addWidget(rbtn1)#, alignment = Qt.AlignCenter)
layoutV1.addWidget(rbtn3)#, alignment = Qt.AlignCenter)
layoutV2.addWidget(rbtn2)#, alignment = Qt.AlignCenter)
layoutV2.addWidget(rbtn4)#, alignment = Qt.AlignCenter)
#
main_layout.addLayout(layoutV1)
main_layout.addLayout(layoutV2)
radiogroupbox.setLayout(main_layout)


main_win.setLayout(main_layout)
main_win.show()
app.exec_()