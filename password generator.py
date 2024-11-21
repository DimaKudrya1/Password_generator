from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.resize(400, 600)
window.setWindowTitle('Password generator')

v_line = QVBoxLayout()#шаблон розсташування вертикального


text = QLabel('Password generator',  alignment=Qt.AlignCenter)
v_line.addWidget(text)




def click_btn():
    password.setText('пароль')

btn = QPushButton('Згенерувати пароль')
btn.clicked.connect(click_btn)

v_line.addWidget(btn, alignment=Qt.AlignCenter)

password = QLabel('', alignment=Qt.AlignCenter)

v_line.addWidget(password)

window.setLayout(v_line)

window.show()
app.exec_()