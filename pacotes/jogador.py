

class Jogador :
    def __init__(self,nome: str, numero_camisa: int) -> None:
        self.nome = nome
        self.numero_camisa = numero_camisa
    
    def mostra_nome(self)-> str:
        return f'{self.nome}, Camisa : {self.numero_camisa}'
        
        