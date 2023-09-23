from pacotes.jogador import Jogador
from pacotes.comissao import ComissaoTecinca
from pacotes.time import Time
from pacotes.tecnico import Tecnico
from pacotes.auxiliar_tecnico import AuxiliarTecnico
from pacotes.preparador_fisico import PreparadorFisico


class MenuCadastro:
    def __init__(self) -> None:
        self.lista_times = []

    def cadastrar_jogador(self):
        jogadores = []
        nome = input("Nome do jogador: ")
        time = input("Nome do time do jogador: ")
        numero_camisa = input("Número da camisa do jogador: ")
        jogador = Jogador(nome, time, numero_camisa)
        jogadores.append(jogador)
        print("Jogador cadastrado com sucesso!")
        return jogadores
    
    def cadastrar_time(self):
        nome = input("Nome do time: ")
        cidade = input("Cidade do time: ")
        mascote = input("Mascote do time: ")
        time = Time(nome, cidade, mascote)
        self.lista_times.append(time)
        print("Time cadastrado com sucesso!")
        
    
    def cadastrar_comissao_tecnica(self,):
        comissao_tecnica = []
        nome_do_tecnico = input("Digite o nome do Tecnico: ")
        nome_do_time = input("Digite o nome do Time: ")
        esquema_tecnico = input("Qual o esquema tatico de sua preferencia: ")
        tecnico = Tecnico(nome_do_tecnico,nome_do_time,esquema_tecnico)
        comissao_tecnica.append(tecnico)
        
        nome_auxiliar = input("Digite o nome do Auxiliar Técnico: ")
        esquema_tatico_auxiliar = input("Qual o esquema Tatico de sua preferencia: ")
        auxiliar = AuxiliarTecnico(nome_auxiliar,nome_do_time,esquema_tatico_auxiliar)
        comissao_tecnica.append(auxiliar)
        
        nome_prepador = input("Digite o Nome do Preparador Físico: ")
        parte_do_elenco = input("Digite com qual parte tecnica vai trabalhar(Goleiro ou Linha): ")
        preparador = PreparadorFisico(nome_prepador,nome_do_time,parte_do_elenco)
        comissao_tecnica.append(preparador)
        
    def mostrar_times (self,):
        for time in self.lista_times:
            time.mostra_time()
           

        
    def teste_sistema_menu(self,):
        time = Time('America','Belo Horizonte','Coelho',)
        self.lista_times.append(time)
        self.mostrar_times()
        
    def sistema_menu (self,):
    
        while True:
            print("\nMenu:")
            print("1. Cadastrar Time")
            print("2. Mostrar Times")
            print("3. Cadastrar Comissão Técnica")
            print("4. Sair")
        
            self.escolha = input("Digite a sua opeção: ")
            
            if self.escolha == "1":
               self.cadastrar_time()
            elif self.escolha == "2":
                self.mostrar_times()
            # elif self.escolha == "2":
            #     cadastrar_jogador()
            # elif self.escolha == "3":
            #     cadastrar_comissao_tecnica()
            elif self.escolha == "4":
                break
            else:
                print("Opção inválida. Tente novamente.")
    