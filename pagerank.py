import csv
def calcular_pagerank(grafo, d=0.85, max_iter=100, tol=1e-6):
    """Calcula el PageRank a partir de un grafo, amortiguación, iteraciones y tolerancia."""
    n = len(grafo._vertices)
    pagerank = {v.id: 1/n for v in grafo._vertices.values()} # Inicialización del PageRank.
    new_pagerank = pagerank.copy() # Se copia el PageRank para actualizarlo posteriormente.

    salidas = {v.id: 0 for v in grafo._vertices.values()} # Inicialización de las salidas.
    for arista in grafo._aristas: 
        salidas[arista.origen.id] += 1 # Se cuentan las salidas de cada nodo.

    for i in range(max_iter): 
        perdida = sum(pagerank[v] for v in salidas if salidas[v] == 0) / n # Suma de PageRank de nodos sin salidas.
        for v in grafo._vertices.values():
            nuevo_valor = (1 - d) / n + d * perdida 
            for u in v.entrantes:
                if salidas[u.id] > 0:
                    nuevo_valor += d * pagerank[u.id] / salidas[u.id] # Suma de PageRank de nodos con salidas.
            new_pagerank[v.id] = nuevo_valor

        diff = sum(abs(new_pagerank[v] - pagerank[v]) for v in pagerank) # Diferencia entre el PageRank actual y la copia.
        if diff < tol: # Si la diferencia es menor a la tolerancia, se termina el cálculo.
            break 
        pagerank = new_pagerank.copy() # Se actualiza el PageRank.

    return pagerank

def guardar_pagerank_csv(grafo, archivo_csv='pagerank_resultados.csv'):
    """Guarda los resultados del PageRank en un archivo CSV."""
    pagerank = calcular_pagerank(grafo) # Se calcula el PageRank a partir del grafo.
    with open(archivo_csv, mode='w', newline='', encoding='utf-8') as f: # Se abre el archivo CSV pasado al método en modo escritura.
        writer = csv.writer(f)
        writer.writerow(['URL', 'PageRank'])
        for url, pr in pagerank.items(): 
            writer.writerow([url, pr])
    # Se imprime por pantalla un mensaje de éxito una vez que se guardaron los resultados.        
    print(f"Resultados de PageRank guardados en {archivo_csv}") 
