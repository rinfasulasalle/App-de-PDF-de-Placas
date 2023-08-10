import os
# ----------------------------------------------------------
def get_matriculas(nombre_archivo):
    # Lista para almacenar los códigos
    codigos = []
    # Abro el archivo CSV en modo lectura
    with open(nombre_archivo, 'r') as archivo_csv:
        # Leo todas las líneas del archivo
        lineas = archivo_csv.readlines()
        # Itero sobre las líneas y elimina los espacios en blanco
        codigos = [linea.strip() for linea in lineas]
    return codigos
# ----------------------------------------------------------
def get_archivos_pdf(directorio):
    archivos_pdf = []  # Creo una lista para almacenar los nombres de archivos PDF encontrados
    # Itero a través de los directorios y archivos utilizando os.walk
    for _, _, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.lower().endswith(".pdf"):  # Compruebo si el archivo tiene extensión .pdf
                archivos_pdf.append(archivo)  # Agrego el nombre del archivo a la lista
    return archivos_pdf
#--
def get_archivos_pdf_recursivo(directorio):
    # Verifica si el directorio es válido
    if not os.path.isdir(directorio):
        return []

    # Usando list comprehension para obtener rutas completas de archivos PDF en el directorio actual
    archivos_pdf = [os.path.join(directorio, archivo) for archivo in os.listdir(directorio) if archivo.lower().endswith(".pdf")]

    # Obtiene una lista de rutas completas de subdirectorios en el directorio actual
    subdirectorios = [os.path.join(directorio, subdirectorio) for subdirectorio in os.listdir(directorio) if os.path.isdir(os.path.join(directorio, subdirectorio))]

    # Recursivamente obtiene archivos PDF de subdirectorios y concatena las listas resultantes
    subarchivos_pdf = [archivo for subdirectorio in subdirectorios for archivo in get_archivos_pdf_recursivo(subdirectorio)]

    # Combina las listas de archivos PDF en el directorio actual y sus subdirectorios
    return archivos_pdf + subarchivos_pdf
# ----------------------------------------------------------
# DATOS DE LA EMPRESA
LICENCIAS = get_matriculas('pdf/DATA LICENCIAS DE CONDUCIR DUMMIE.csv')
PDFS = (get_archivos_pdf('pdf'))
LOGO = 'https://store-images.s-microsoft.com/image/apps.31887.13527552335205219.79bdc359-aeae-43cd-ac4a-a9b8c2321785.972ea833-efd0-4edd-b0dc-20ea591f449f'
NOMBREAPP = 'My App'