def leer_archivo(nombre_archivo):
    # Lista para almacenar los códigos
    codigos = []

    # Abre el archivo CSV en modo lectura
    with open(nombre_archivo, 'r') as archivo_csv:
        # Lee todas las líneas del archivo
        lineas = archivo_csv.readlines()

        # Itera sobre las líneas y elimina los espacios en blanco
        codigos = [linea.strip() for linea in lineas]

    return codigos
print(leer_archivo('licencias.csv'))