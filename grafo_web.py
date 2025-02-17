import csv
from edd.grafo import DiGrafo, Vertice, Arista
from graphviz import Digraph

def caracteres_especiales(texto):
    return ''.join(c for c in texto if c.isalnum() or c in ['_', '-'])

class GrafoWeb(DiGrafo):
    def AgregarAristas(self, archivo_csv: str, limite: int = None):
        """Agrega aristas al grafo a partir de un archivo CSV."""
        with open(archivo_csv, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            for d in reader:
                origen, destino = d['URL Origen'], d['URL Destino']
                self.agregar_arista(origen, destino)
                count += 1
                if limite and count >= limite:
                    break

    def graficar(self):
        """Genera un dot y lo renderiza en un .png para visualizar el grafo."""
        dot = Digraph(comment="Grafo Web")
        for vertice in self._vertices.values():
            dot.node(caracteres_especiales(vertice.id))
        for arista in self._aristas:
            dot.edge(caracteres_especiales(arista.origen.id), caracteres_especiales(arista.destino.id))
        dot.save("grafoweb.dot")
        dot.render("grafoweb", engine="sfdp", format="png", view=True)

    def transponer(self):
        """
        Crea una nueva instancia de GrafoWeb con las aristas invertidas.
        """
        grafo_transpuesto = GrafoWeb()  # Crear un nuevo grafo vacío

        # Invertir cada arista y agregarla al grafo transpuesto
        for arista in self._aristas:
            origen = arista.origen.id
            destino = arista.destino.id
            grafo_transpuesto.agregar_arista(destino, origen, arista.peso)  # Invertir dirección de la arista

        return grafo_transpuesto
