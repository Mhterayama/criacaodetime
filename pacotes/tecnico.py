class Tecnico:
    def __init__(self, nome_do_tecnico: str,  esquema_tatico: str) -> None:
        """
        Recebe o nome da pessoa, e qual esquema tatico de sua escolha.
        """
        self.nome_do_tecnico = nome_do_tecnico
        self.esquema_tatico = esquema_tatico
        
    
    def mostra_nome(self)-> str:
        return self.nome_do_tecnico