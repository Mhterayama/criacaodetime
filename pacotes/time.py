from pacotes.jogador import Jogador
from pacotes.comissao import ComissaoTecinca

class Time :
    def __init__(self,nome_do_time: str, cidade_mandante: str, nome_do_mascote: str, lista_jogador: list, ) -> None:
        self.nome_do_time = nome_do_time
        self.cidade_mandante = cidade_mandante
        self.nome_do_time = nome_do_mascote
        self.jogadores = lista_jogador
        #self.comissao_tecnica = comissao_tecnica
               
    
        
    def mostra_time (self):
        print(f'Nome do Time: {self.nome_do_time}')
        for jogador in self.jogadores:
            print(f'Jogador: {jogador.mostra_nome()}')