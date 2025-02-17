from graphviz import Digraph
from grafo_web import caracteres_especiales
from edd.grafo import DiGrafo, Vertice, Arista
import csv


def dfs(u: Vertice, visitado: dict[Vertice, int], contador: int):
    visitado[u] = contador
    for w in u.adyacentes:
        if visitado[w] == -1:
            dfs(w, visitado, contador)

def obtener_scc_kosaraju(grafo):
    visitado = {v: -1 for v in grafo.vertices}  
    pila = []
    contador = 0  

    for v in grafo.vertices:
        if visitado[v] == -1:
            dfs(v, visitado, contador)
            pila.append(v)  

    grafo_transpuesto = grafo.transponer()

    visitado = {v: -1 for v in grafo_transpuesto.vertices} 
    scc_resultados = []
    contador_scc = 0

    while pila:
        v = pila.pop()
        if visitado[v] == -1:
            componente_actual = []
            dfs_transpuesto(grafo_transpuesto, v, visitado, componente_actual, contador_scc)
            scc_resultados.append(componente_actual)
            contador_scc += 1

    return scc_resultados

def dfs_transpuesto(grafo, v, visitado, componente, contador_scc):
    visitado[v] = contador_scc
    componente.append(v)
    for w in v.adyacentes:
        if visitado[w] == -1:
            dfs_transpuesto(grafo, w, visitado, componente, contador_scc)

def exportar_scc_csv(scc_resultados, archivo_csv="scc_resultados.csv"):
    with open(archivo_csv, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Componente", "URLs"])
        for idx, componente in enumerate(scc_resultados):
            urls = ', '.join([v.id for v in componente])
            writer.writerow([f"SCC {idx+1}", urls])

def graficar_scc(grafo, scc_resultados):
    dot = Digraph(comment="Componentes Fuertemente Conexas")
    colores = ["red","blue","yellow","green","purple"]
    for i, componente in enumerate(scc_resultados):
        color = colores[i % len(colores)]
        for vertice in componente:
            dot.node(caracteres_especiales(vertice.id), color=color, style="filled")
    for arista in grafo._aristas:
        dot.edge(caracteres_especiales(arista.origen.id), caracteres_especiales(arista.destino.id))
    dot.save("grafoweb_scc.dot")
    dot.render("grafoweb_scc", format="png", engine="sfdp", view=True)
