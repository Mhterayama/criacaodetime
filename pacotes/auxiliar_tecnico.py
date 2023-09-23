class AuxiliarTecnico:
    def __init__(self, nome_do_tecnico: str, nome_time: str, esquema_tatico: str) -> None:
        """
        Recebe o nome da pessoa, o nome do time, e qual esquema tatico de sua escolha.
        """
        
        self.nome_do_tecnico = nome_do_tecnico
        self.nome_time = nome_time
        self.esquema_tatico = esquema_tatico