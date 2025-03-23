import time
import random
import threading


# Função que simula uma tarefa que leva tempo para ser executada
def tarefa_simulada(tarefa_id):
    print(f"Iniciando tarefa {tarefa_id}")
    tempo_execucao = random.uniform(1, 5)  # Simula um tempo de execução entre 1 e 5 segundos
    time.sleep(tempo_execucao)
    print(f"Tarefa {tarefa_id} concluída em {tempo_execucao:.2f} segundos")


# Teste de desempenho: executa várias tarefas sequencialmente
def teste_desempenho(num_tarefas):
    print("Iniciando teste de desempenho...")
    inicio = time.time()

    for i in range(num_tarefas):
        tarefa_simulada(i + 1)

    fim = time.time()
    print(f"Teste de desempenho concluído em {fim - inicio:.2f} segundos")


# Teste de carga: executa várias tarefas simultaneamente (usando threads)
def teste_carga(num_tarefas):
    print("Iniciando teste de carga...")
    inicio = time.time()

    threads = []
    for i in range(num_tarefas):
        thread = threading.Thread(target=tarefa_simulada, args=(i + 1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    fim = time.time()
    print(f"Teste de carga concluído em {fim - inicio:.2f} segundos")


# Teste de estresse: executa um número muito alto de tarefas simultaneamente
def teste_estresse(num_tarefas):
    print("Iniciando teste de estresse...")
    inicio = time.time()

    threads = []
    for i in range(num_tarefas):
        thread = threading.Thread(target=tarefa_simulada, args=(i + 1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    fim = time.time()
    print(f"Teste de estresse concluído em {fim - inicio:.2f} segundos")


# Menu para escolher o tipo de teste
def menu():
    print("Escolha o tipo de teste não funcional:")
    print("1 - Teste de Desempenho")
    print("2 - Teste de Carga")
    print("3 - Teste de Estresse")
    escolha = input("Digite o número da opção desejada: ")

    num_tarefas = int(input("Digite o número de tarefas a serem executadas: "))

    if escolha == "1":
        teste_desempenho(num_tarefas)
    elif escolha == "2":
        teste_carga(num_tarefas)
    elif escolha == "3":
        teste_estresse(num_tarefas)
    else:
        print("Opção inválida!")


# Executa o menu
menu()
