from PyQt5.QtWidgets import QApplication
from App.view.loginUI import LoginUI
from App.controller.loginController import isLogged

app = QApplication([])
login = LoginUI()

while not isLogged():
    res = login.exec_()
    if res:
        print('login efetuado - carregar tela HOME')
        # tela = MainUI()
        # app.exec_()
    else:
        break

print('programa encerrado')