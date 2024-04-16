from lib import *
import pandas as pd
import threading
import time 
import logging
from concurrent.futures import ThreadPoolExecutor

nombre_archivo = input('Nombre del achivo:')
df = pd.read_excel(nombre_archivo,index_col=False)
 

array = df.values.flatten().tolist()
print(len(array))

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

num_hilos = input("¿Cuántos hilos quiere crear? :")




globalArrayNum = [array]
def contadorDos(inicio, fin):
    logging.info(f'Función con rango: {inicio} - {fin}')
    for i in range(inicio, fin+1, 1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return 0
t0 = time.time()

with ThreadPoolExecutor(max_workers= 2) as executor:
    inicio = 1
    hilos =int(num_hilos) 
    fin = 10000
    #subrango = 200//5
    subrango = fin // hilos
    for i in range (inicio, hilos+1,1):
        intento = subrango * i
        executor.submit(contadorDos,inicio,intento)
        inicio = subrango + inicio


tf = time.time() - t0
print(globalArrayNum)
print(f'Tiempo de ejecución: {tf} ')
globalArrayNum.sort()