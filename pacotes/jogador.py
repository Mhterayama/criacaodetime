

class Jogador :
    def __init__(self,nome: str, nome_time : str, numero_camisa: int) -> None:
        self.nome = nome,
        self.nome_time = nome_time,
        self.numero_camisa = numero_camisa
    
    def mostra_nome(self)-> str:
        return self.nome
        
        