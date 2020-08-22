import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        sg.theme('Black') # Escolhendo o tema, https://www.geeksforgeeks.org/themes-in-pysimplegui/ 
        
        # Criando os elementos da pagina
        layout = [
            [sg.Text('Site/Software', size=(10,1)), 
            sg.Input(key='site', size=(20,1))],
            [sg.Text('Email/Usuario', size=(10,1)), 
            sg.Input(key='usuario', size=(20,1))],
            [sg.Text('Quantidade de Caracteres'), sg.Combo(values=list(range(30)), key='total_chars',
            default_value=1, size=(3,1) )],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]

        # Exibidando a tela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read() # Lendo as informacoes da aplicacao
            
            if evento == sg.WINDOW_CLOSED: # Para fechar o programa
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
    
    def gerar_senha(self, valores):
        char_list = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789!#%$&*@'
        chars = random.choices(char_list, k=int(valores['total_chars'])) # Gerar uma quantidade de caracteres, sendo o total deles passado por k=int()
        # valores['total_chars'] esta passando o total de caracteres escolhidos na aplicacao
        new_pass = ''.join(chars) # Esta concatendando a string, ou seja tirando os espacos em branco
        return new_pass

    def salvar_senha(self):
        pass

gen = PassGen()
gen.Iniciar()