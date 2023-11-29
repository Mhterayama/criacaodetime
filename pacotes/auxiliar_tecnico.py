class AuxiliarTecnico:
    def __init__(self, nome_do_auxiliar: str, esquema_tatico: str) -> None:
        """
        Recebe o nome da pessoa, o nome do time, e qual esquema tatico de sua escolha.
        """
        
        self.nome_do_auxiliar = nome_do_auxiliar
        self.esquema_tatico = esquema_tatico


    def mostra_nome(self)-> str:
        return self.nome_do_auxiliar