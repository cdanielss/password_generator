import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        sg.theme('BlueMono') # Escolhendo o tema, https://www.geeksforgeeks.org/themes-in-pysimplegui/ 
        
        # Criando os elementos da pagina
        layout = [
            [sg.Text('Site/Software:', size=(15,1)), 
            sg.Input(key='site', size=(20,1))],
            [sg.Text('Email/Usuario:', size=(15,1)), 
            sg.Input(key='usuario', size=(20,1))],
            [sg.Text('Quantidade de Caracteres:'), sg.Combo(values=list(range(30)), key='total_chars',
            default_value=7, size=(3,1) )],
            [sg.Text('Caracteres Especiais:'), sg.Combo(values=('sim', 'não'), key='esp_chars',
            default_value='sim', size=(5,1) )],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha'), sg.Button('Salvar')]
        ]

        # Exibidando a tela
        self.janela = sg.Window('Password Generator', layout, grab_anywhere=True, size=(350,250))

    def Iniciar(self):
        # Roda a aplicacao
        while True:
            evento, valores = self.janela.read() # Lendo as informacoes da aplicacao
            if evento == sg.WINDOW_CLOSED: # Para fechar o programa
                break
            if evento == 'Gerar Senha': # Se clicar no botao de gerar senhas
                if valores['esp_chars'] == 'sim':
                    nova_senha = self.gerar_senha(valores)
                    print(nova_senha) 
                if valores['esp_chars'] == 'não':
                    nova_senha = self.gerar_senhaEsp(valores)
                    print(nova_senha) 
            if evento == 'Salvar': # Se clicar no botao de salvar
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, valores):
        char_list = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789!#%$&*@'
        chars = random.choices(char_list, k=int(valores['total_chars'])) # Gerar uma quantidade de caracteres, sendo o total deles passado por k=int()
        # valores['total_chars'] esta passando o total de caracteres escolhidos na aplicacao
        new_pass = ''.join(chars) # Esta concatendando a string, ou seja tirando os espacos em branco
        return new_pass

    def gerar_senhaEsp(self, valores):
        char_list = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
        chars = random.choices(char_list, k=int(valores['total_chars'])) 
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt','a',newline='') as arquivo: 
            arquivo.write(f"site: {valores['site']}, usuario: {valores['usuario']}, senha: {nova_senha} \n")

        print('Arquivo Salvo')

gen = PassGen()
gen.Iniciar()