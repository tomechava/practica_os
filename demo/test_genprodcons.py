import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import threading
import time
from genprodcons import GenProdCons

def productor(pc: GenProdCons[int]):
    for i in range(5):
        print(f"[Productor] Poniendo: {i}")
        pc.put(i)
        time.sleep(1)

def consumidor(pc: GenProdCons[int]):
    for _ in range(5):
        valor = pc.get()
        print(f"[Consumidor] Recibido: {valor}")
        time.sleep(2)

if __name__ == "__main__":
    pc = GenProdCons(size=2)

    hilo_prod = threading.Thread(target=productor, args=(pc,))
    hilo_cons = threading.Thread(target=consumidor, args=(pc,))

    hilo_prod.start()
    hilo_cons.start()

    hilo_prod.join()
    hilo_cons.join()

    print("[FIN] Productor y Consumidor han terminado.")
