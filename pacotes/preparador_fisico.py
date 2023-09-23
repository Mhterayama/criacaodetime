class PreparadorFisico:
    def __init__(self, nome_do_preparador:str, nome_time:str, parte_elenco:str):
        """
        Recebe nome da pessoa, qual time ele pertence, e qual parte do elenco ele trabalha(Goleiro ou linha).
        """
        
        self.nome_do_preparador = nome_do_preparador
        self.nome_time = nome_time
        self.parte_elenco = parte_elenco
