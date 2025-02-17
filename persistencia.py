import csv
from edd.grafo import DiGrafo
from scc import obtener_scc_kosaraju

def guardar_grafo(grafo: DiGrafo, archivo_nodos: str = "nodos.csv", archivo_aristas: str = "aristas.csv"):
    """Guarda un grafo en dos archivos CSV, uno para los nodos y otro para las aristas."""
    try:
        # Abre el archivo de nodos en modo escritura, con codificación UTF-8, y crea un objeto escritor para guardar los nodos del grafo en CSV
        with open(archivo_nodos, mode="w", newline="", encoding="utf-8") as f: # newline="" para evitar líneas en blanco
            writer = csv.writer(f)
            writer.writerow(["ID"])
            for vertice in grafo.vertices:
                writer.writerow([vertice.id])
        print(f"Nodos guardados en {archivo_nodos}") # Si no hubo errores, se imprime por pantalla un mensaje de éxito
    except IOError as e: # Captura cualquier error de entrada/salida
        print(f"Error al guardar nodos en {archivo_nodos}: {e}") # Si hubo errores, se imprime un mensaje de error
    
    try:
        # Realiza lo mismo que el bloque anterior, pero con las aristas
        with open(archivo_aristas, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Origen", "Destino"])  # Encabezado
            for arista in grafo.aristas:
                writer.writerow([arista.origen.id, arista.destino.id])
        print(f"Aristas guardadas en {archivo_aristas}")  # Si no hubo errores, se imprime por pantalla un mensaje de éxito
    except IOError as e: # Captura cualquier error de entrada/salida y muestra el mensaje de error apropiado
        print(f"Error al guardar aristas en {archivo_aristas}: {e}")


def cargar_grafo(archivo_nodos: str, archivo_aristas: str) -> DiGrafo:
    """Carga un grafo desde dos archivos CSV, uno para los nodos y otro para las aristas."""
    grafo = DiGrafo() # Crea un grafo vacío para llenarlo con los nodos y aristas del archivo y devolverlo al final
    try:
        # Abre el archivo de nodos en modo lectura, con codificación UTF-8, y crea un objeto lector para leer los nodos del grafo en CSV
        with open(archivo_nodos, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            primera_linea = True
            for row in reader:
                
                if primera_linea: # Ignora la primera línea, que es el encabezado
                    primera_linea = False
                    continue
                
                if row: # Si la fila no está vacía agrega el nodo al grafo
                    grafo.agregar_arista(row[0], row[0])
        print(f"Nodos cargados desde {archivo_nodos}") # Si no hubo errores, se imprime por pantalla un mensaje de éxito
    
    except FileNotFoundError: # Captura el error de que el archivo no existe y muestra el mensaje de error apropiado
        print(f"Archivo de nodos no encontrado: {archivo_nodos}")
    
    except IOError as e: # Captura cualquier otro error de entrada/salida y muestra el mensaje de error apropiado
        print(f"Error al cargar nodos desde {archivo_nodos}: {e}")
    
    try:
        # Realiza lo mismo que el bloque anterior, pero con las aristas
        with open(archivo_aristas, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            primera_linea = True
            for row in reader:
                if primera_linea:
                    primera_linea = False 
                    continue
                if len(row) == 2:
                    grafo.agregar_arista(row[0], row[1])
        print(f"Aristas cargadas desde {archivo_aristas}")
    
    except FileNotFoundError: # Captura el error de que el archivo no existe y muestra el mensaje de error apropiado
        print(f"Archivo de aristas no encontrado: {archivo_aristas}")
    
    except IOError as e: # Captura cualquier otro error de entrada/salida y muestra un mensaje de error
        print(f"Error al cargar aristas desde {archivo_aristas}: {e}")

    return grafo


def guardar_scc(scc_resultados, archivo_csv="scc_resultados.csv"):
    """Guarda las SCC en un archivo CSV."""
    try:
        with open(archivo_csv, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Componente", "URLs"])
            for idx, componente in enumerate(scc_resultados):
                urls = ', '.join([v.id for v in componente])
                writer.writerow([f"SCC {idx + 1}", urls])
        print(f"SCC guardadas en {archivo_csv}")
    
    except IOError as e: # Captura cualquier error de entrada/salida y muestra un mensaje de error
        print(f"Error al guardar SCC en {archivo_csv}: {e}")


def cargar_scc(archivo_csv="scc_resultados.csv"):
    """Carga las SCC desde un archivo CSV."""
    scc_resultados = []
    try:
        # Abre el archivo de nodos en modo lectura y crea un lector para leer los nodos del grafo en CSV-
        with open(archivo_csv, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            primera_linea = True
            for row in reader:
                if primera_linea:
                    primera_linea = False
                    continue
                if row and len(row) == 2:
                    componente, urls = row
                    urls = urls.split(', ')
                    scc_resultados.append(urls)
        print(f"SCC cargadas desde {archivo_csv}") # Si no hubo errores, se imprime por pantalla un mensaje de éxito
    
    except FileNotFoundError: # Captura el error de que el archivo no existe y muestra el mensaje de error apropiado
        print(f"Archivo de SCC no encontrado: {archivo_csv}")
    
    except IOError as e: # Captura cualquier otro error de entrada/salida y muestra un mensaje de error
        print(f"Error al cargar SCC desde {archivo_csv}: {e}")

    return scc_resultados # Finalmente devuelve la lista de SCC cargadas desde el archivo CSV
