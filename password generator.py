from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt
from mine import generate_password

app = QApplication([])
window = QWidget()
window.resize(500, 400)
window.setWindowTitle('Password generator')
window.setStyleSheet('background-color: darckCyan;')
v_line = QVBoxLayout()#шаблон розсташування вертикального
v_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

#text = QLabel('Password generator')
#text.setStyleSheet('font-size: 20px;')
#v_line.addWidget(text)
#v_line.setAlignment(text, Qt.AlignmentFlag.AlignCenter)


def click_btn():
    df_pass = difficult_password.text()
    password.setText(generate_password(int(df_pass)))

text_dificult = QLabel('Введіть складність пароля')
difficult_password = QLineEdit('8')
difficult_password.setStyleSheet('font-size: 20px; color: white;')
text_dificult.setStyleSheet('font-size: 20px; margin: 30px; padding: 40px; color: white;')

v_line.addWidget(text_dificult)
v_line.addWidget(difficult_password)

btn = QPushButton('Згенерувати пароль')
btn.setStyleSheet('font-size: 20px; padding: 10px; margin: 40px; background-color: lightblue;')
btn.clicked.connect(click_btn)

v_line.addWidget(btn)

password = QLineEdit('')
password.setStyleSheet('font-size: 20px; color: white;')

v_line.addWidget(password)

window.setLayout(v_line)

window.show()
app.exec()