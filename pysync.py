import threading
from threading import Thread
from queue import Queue
from typing import Generic, TypeVar, Any

E = TypeVar('E')
T = TypeVar('T')

class GenProdCons(Generic[E]):
    
    def __init__(self, size: int = 10):
        #Revisar que size si sea un int
        if isinstance(size, int):
            self.size = size
        else:
            raise ValueError("El tamaño debe ser un entero")
        
        if size <= 0:
            raise ValueError("El tamaño del buffer debe ser mayor que 0")
        
        
        #Creamos cola FIFO para almacenar los elementos
        self.queue = Queue(maxsize=size)
        
        #Variable para controlar el estado de la cola
        self.disabled = False
        
    def put(self, e: E):
        self.queue.put(e)        
    
    def get(self) -> E:
        return self.queue.get()
    
    def __len__(self):
        return self.queue.qsize()
    
    
class RendezvousDEchange(Generic[E,T]):
    def __init__(self):
        self.mutex = threading.Lock()
        self.condition = threading.Condition(self.mutex)
        self.first_arrived = False
        self.first_value = None
        self.second_value = None

    def echanger(self, value: E) -> T:
        with self.condition:
            if not self.first_arrived:
                self.first_value = value
                self.first_arrived = True
                self.condition.wait()
                result = self.second_value

                self.first_arrived = True
                self.first_value = None
                self.second_value = None

                self.condition.notify()
                return result
            else:
                self.second_value = value
                result = self.first_value
                self.condition.notify()
                self.condition.wait()
                return result
    