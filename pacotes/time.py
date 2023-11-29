from pacotes.jogador import Jogador
from pacotes.comissao import ComissaoTecinca
from pacotes.tecnico import Tecnico
from pacotes.auxiliar_tecnico import AuxiliarTecnico
from pacotes.preparador_fisico import PreparadorFisico
class Time :
    def __init__(self,nome_do_time: str, cidade_mandante: str, nome_do_mascote: str,  ) -> None:
        self.nome_do_time = nome_do_time
        self.cidade_mandante = cidade_mandante
        self.nome_do_mascote = nome_do_mascote
        self.jogadores = []
        self.comissao_tecnica = []
               
    
    def adiciona_jogador (self,jogador: Jogador):
        self.jogadores.append(jogador)

    def adiciona_comissao_tecnica (self, tecnico: Tecnico, auxiliar_tecnico: AuxiliarTecnico, preparador_fisico: PreparadorFisico):
        self.comissao_tecnica.append(tecnico)
        self.comissao_tecnica.append(auxiliar_tecnico)
        self.comissao_tecnica.append(preparador_fisico)
    
    def mostra_time (self):
        print(f'Nome do Time: {self.nome_do_time}')
        for jogador in self.jogadores:
            print(f'Jogador: {jogador.mostra_nome()}')
        for comissao in self.comissao_tecnica:
            if isinstance(comissao, Tecnico):
                print(f"Técnico: {comissao.mostra_nome()}")
            elif isinstance(comissao, AuxiliarTecnico):
                print(f"Auxiliar Técnico: {comissao.mostra_nome()}")
            elif isinstance(comissao, PreparadorFisico):
                print(f"Preparador Físico: {comissao.mostra_nome()}")
    
    def dar_coletiva(self):
        for comissao in self.comissao_tecnica:
            if isinstance(comissao, Tecnico):
                print(f"Técnico: {comissao.mostra_nome()}Esta dando Coletiva de Impressa !!")
            elif isinstance(comissao, AuxiliarTecnico):
                print(f"Auxiliar Técnico: {comissao.mostra_nome()} Esta dando Coletiva de Impressa !!")
            elif isinstance(comissao, PreparadorFisico):
                print(f"Preparador Físico: {comissao.mostra_nome()}Esta dando Coletiva de Impressa !!")