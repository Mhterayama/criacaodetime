from pacotes.jogador import Jogador as jg 
from pacotes.time import Time
from pacotes.comissao import ComissaoTecinca as CT
from pacotes.preparador_fisico import PreparadorFisico as PreF
from pacotes.auxiliar_tecnico import AuxiliarTecnico as AuxT
from pacotes.tecnico import Tecnico as Tec

jogador1 = jg('mathes','America', 10)
jogador2 = jg('Marcos', 'America', 9)

lista_jogador = [jogador1,jogador2]

time = Time('America','Belo Horizonte','Coelho', lista_jogador)

time.mostra_time()


