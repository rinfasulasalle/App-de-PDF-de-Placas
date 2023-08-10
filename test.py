import time
from load_data import get_archivos_pdf, get_archivos_pdf_recursivo

def medir_tiempo(funcion, *args, repeticiones=10000):
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.time()
        funcion(*args)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        tiempos.append(tiempo_transcurrido)
    
    tiempo_promedio = sum(tiempos) / repeticiones
    print("Tiempo promedio de ejecución:", tiempo_promedio, "segundos")

# Llama a la función medir_tiempo con las dos funciones que deseas medir
medir_tiempo(get_archivos_pdf, 'pdf')
medir_tiempo(get_archivos_pdf_recursivo, 'pdf')
