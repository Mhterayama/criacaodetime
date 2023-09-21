class PreparadorFisico:
    def __init__(self, nome:str, time:str, parte_elenco:str):
        """
        Recebe nome da pessoa, qual time ele pertence, e qual parte do elenco ele trabalha(Goleiro ou linha).
        """
        
        self.nome = nome
        self.time = time
        self.parte_elenco = parte_elenco
