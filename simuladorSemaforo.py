# Sistemas de Informação - 3o Período Turma A #
# Alunas: Natasha Teixeira - 01653487 / Ariel Cássia - 01649872 #

import threading
import time

def semaforo_controller():

    time.sleep(6)
    print("Semáforo: 🟢")
    time.sleep(3)

    print("Semáforo: 🟡")
    time.sleep(3)

    print("Semáforo: 🔴")
    time.sleep(5)

if __name__ == "__main__":
    numero_iteracoes = 3

    for _ in range(numero_iteracoes):
        controller_thread = threading.Thread(target=semaforo_controller)
        controller_thread.start()

        time.sleep(2)
        print("Mudando para verde...")
        time.sleep(4)
        print("Mudando para amarelo...")
        time.sleep(4)
        print("Mudando para vermelho...")
        time.sleep(3)

        controller_thread.join()

        print("Ciclo completo...")