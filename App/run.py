from dotenv import load_dotenv
from PyQt5.QtWidgets import QApplication
from App.view.loginUI import LoginUI
from App.view.homeUI import HomeUI
from App.controller.loginController import isLogged, logout, validateLogin

load_dotenv(override=True)

app = QApplication([])
login = LoginUI()

def login():
    print('-'*20, "Login")
    user = input('Email:')
    senha = input('Senha:')
    result = validateLogin(user, senha)
    return result




while not isLogged():
    if login():
        print('abrir sistema')
    else:
        print("login incorreto")
        # break
    # res = login.exec_()
    # if res:
    #     tela = HomeUI()
    #     app.exec_()
    #     logout()
    # else:
    #     break

print('programa encerrado')