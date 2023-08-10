def get_matriculas(nombre_archivo):
    # Lista para almacenar los códigos
    codigos = []

    # Abre el archivo CSV en modo lectura
    with open(nombre_archivo, 'r') as archivo_csv:
        # Lee todas las líneas del archivo
        lineas = archivo_csv.readlines()

        # Itera sobre las líneas y elimina los espacios en blanco
        codigos = [linea.strip() for linea in lineas]

    return codigos
print(get_matriculas('pdf/DATA LICENCIAS DE CONDUCIR DUMMIE.csv'))

# ----------------------------------------------------------
import os

def get_archivos_pdf(directorio):
    archivos_pdf = []

    for ruta_actual, _, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.lower().endswith(".pdf"):
                archivos_pdf.append(os.path.join(archivo))

    return archivos_pdf
print(get_archivos_pdf('pdf'))
