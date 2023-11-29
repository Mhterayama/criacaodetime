class PreparadorFisico:
    def __init__(self, nome_do_preparador:str, parte_elenco:str):
        """
        Recebe nome da pessoa, qual time ele pertence, e qual parte do elenco ele trabalha(Goleiro ou linha).
        """
        
        self.nome_do_preparador = nome_do_preparador
        self.parte_elenco = parte_elenco

    def mostra_nome(self)-> str:
        return self.nome_do_preparador