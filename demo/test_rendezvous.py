import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import threading
import time
import random
from rendezvousdechange import RendezvousDEchange

def trabajador(rendezvous: RendezvousDEchange[str, str], nombre: str):
    tiempo_espera = random.uniform(0.1, 1.5)
    time.sleep(tiempo_espera)  # Para que lleguen en tiempos aleatorios
    print(f"[{nombre}] Listo para intercambiar después de {tiempo_espera:.2f}s")
    recibido = rendezvous.echanger(nombre)
    print(f"[{nombre}] Recibió: {recibido}")

if __name__ == "__main__":
    rendezvous = RendezvousDEchange()

    nombres = ["Hilo-1", "Hilo-2", "Hilo-3", "Hilo-4", "Hilo-5", "Hilo-6"]
    hilos = []

    for nombre in nombres:
        t = threading.Thread(target=trabajador, args=(rendezvous, nombre))
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()

    print("[FIN] Todos los hilos intercambiaron datos.")
