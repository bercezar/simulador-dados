#Simulador de dado
#Simula o dado, o uso consiste em gerar valores de 1 a 6

import random

class SimuladorDados:
    def __init__ (self):
        self.max = 6
        self.min = 1
        self.msg = "Você deseja lançar o dado?\nR.:"
    
    def iniciar(self):
        resposta = input(self.msg)
        try:
            if resposta.upper() in ['SIM', 'S']:
                return self.gerarvalor()
            elif resposta.upper() not in ['SIM', 'S']:
                print("OBRIGADO POR JOGAR!")
            else:
                print("Por favor, responda com 'sim' ou 'não'")
        except:
            print("ERROR....")
    
    def gerarvalor(self):
        print(random.randint(self.min, self.max))

simula = SimuladorDados()
simula.iniciar()
