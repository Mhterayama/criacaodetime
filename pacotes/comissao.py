from pacotes.tecnico import Tecnico
from pacotes.auxiliar_tecnico import AuxiliarTecnico
from pacotes.preparador_fisico import PreparadorFisico
class ComissaoTecinca:
    def __init__(self, tecnico: Tecnico, auxiliar_tecnico: AuxiliarTecnico, preparador_fisico: PreparadorFisico) -> None:
        self.tecnico = tecnico
        self.auxiliar_tecnico = auxiliar_tecnico
        self.preparador_fisico = preparador_fisico
        
    
    
    def apresentacao_comissao (self)-> None:
       return print(f"Nome Tecinico: {self.nome_tecnico}\n\nNome auxiliar:{self.nome_auxiliar}\n\nNome Preparador Fisico{self.nome_preparador_fisico}")



    def dar_coletiva (self)-> None:
        """
        Verifica a escolha do usuario, qual a parte da comissao tecnica esta em coletiva de imprensa.
        """
        
        escolha = " "
        if escolha == "Preparador Fisico":
            print("O preparador físico está dando uma coletiva de imprensa.")
        elif escolha == "Auxiliar Tecnico":
            print("O Auxiliar Técnico está dando uma coletiva de imprensa.")
        elif escolha == "Tecnico":
            print("O Técnico está dando uma coletiva de imprensa.")
        else:
            print("Esta Pessoa nao faz parte da Comissão Técnica....")