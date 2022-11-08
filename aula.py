# pip install PySimpleGUI // para instalar a biblioteca
# pip install db-sqlite3 // para instalar a biblioteca

import sqlite3
from PySimpleGUI import PySimpleGUI as sg

# designe da tela
#
sg.theme('Dark Grey 13')
layout = [
    [sg.Text('Email:   '), sg.Input(size=(30, 0), key='email')],
    [sg.Text('senha:   '), sg.Input(size=(30, 0), key='senha')],
    [sg.Button('entrar')]
]

# iniciação da tela
janela = sg.Window('login').layout(layout)
button, values = janela.read()

# recolhimeno de dados da interface
email = values['email']
senha = values['senha']

# BANCO DE DADOS

db = sqlite3.connect('DataBase.db')

cursor = db.cursor()

# cursor.execute("CREATE TABLE Login (idUser integer primary key autoincrement, Email text, senha text)")
cursor.execute(f"INSERT INTO Login (Email, senha) VALUES('{email}', '{senha}')")

db.commit()
