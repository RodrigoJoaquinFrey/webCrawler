[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-FxuqLvX)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16397621&assignment_repo_type=AssignmentRepo)
# Trabajo Práctico Grupal de Estructuras de Datos

## Objetivo

El objetivo de este trabajo práctico es aplicar los conceptos aprendidos en clase sobre grafos, recuperación de información de la web y persistencia de datos. Los estudiantes trabajarán en grupos de 4 o 5 integrantes para implementar un _crawler_, construir un grafo de la web y realizar operaciones avanzadas sobre este grafo, incluyendo el cálculo del _PageRank_ y la identificación de componentes fuertemente conexas.

## Enunciado

### Parte 1: Web Crawling

1. **Implementación del _crawler_**
    - Desarrollar un _crawler_ que navegue por el sitio web `untref.edu.ar`, comenzando desde una URL dada.
    - El _crawler_ debe recolectar información sobre los enlaces internos del dominio `untref.edu.ar`.
    - Almacenar los datos recolectados en archivos CSV, incluyendo la URL de origen, la URL de destino y cualquier información adicional relevante (como el texto del enlace).

### Parte 2: Construcción del Grafo

1. **Definición y Construcción del Grafo**
    - Definir una clase `GrafoWeb` para representar un grafo dirigido de las páginas de `untref.edu.ar`.
    - Cada nodo del grafo representará una página web del dominio, y cada arista representará un enlace entre páginas.
    - Implementar métodos para agregar nodos y aristas al grafo utilizando los datos recolectados por el _crawler_.
    - Visualizar el grafo de manera gráfica utilizando bibliotecas como `networkx` y `matplotlib` o `pygraphviz`.

### Parte 3: Cálculo del _PageRank_

1. **Implementación del Algoritmo de _PageRank_**
    - Implementar el algoritmo de _PageRank_ para calcular la importancia de cada página dentro del dominio `untref.edu.ar`.
    - Asegurarse de manejar adecuadamente los enlaces salientes y entrantes, así como las páginas sin enlaces salientes (_dangling nodes_).

2. **Resultados del _PageRank_**
    - Almacenar los resultados del _PageRank_ en un archivo CSV, incluyendo la URL de la página y su valor de _PageRank_.
    - Visualizar los resultados en forma de gráfico, mostrando las páginas con los valores de _PageRank_ más altos.

### Parte 4: Componentes Fuertemente Conexas

1. **Identificación de Componentes Fuertemente Conexas**
    - Implementar un algoritmo para encontrar las componentes fuertemente conexas (SCC) del grafo.
    - Escribir un programa que utilice este algoritmo para identificar y listar todas las SCC del grafo de `untref.edu.ar`.

2. **Visualización de las SCC**
    - Visualizar las componentes fuertemente conexas en el grafo, utilizando colores o etiquetas distintas para cada SCC.
    - Almacenar los resultados en un archivo CSV, incluyendo las URLs de las páginas en cada SCC.

### Parte 5: Persistencia de Datos

1. **Guardado y Carga del Grafo**
    - Guardar el grafo construido y los resultados de las operaciones en archivos CSV.
    - Implementar funciones para leer y escribir datos en estos archivos, asegurando que se manejen posibles excepciones.

## Entregables

1. **Código Fuente:**
    - Todo el código fuente de los programas, organizado en carpetas según la funcionalidad (_crawler_, grafo, _PageRank_, SCC, persistencia de datos).

2. **Documentación:**
    - Documentación del código y las decisiones de diseño.
    - Un informe detallado con la explicación de la solución y los resultados obtenidos.

3. **Datos:**
    - Archivos CSV generados durante la ejecución de los programas.
    - Ejemplos de entradas y salidas utilizadas para las pruebas.

4. **Presentación Oral:**
    - Una presentación oral explicando las soluciones implementadas y respondiendo preguntas sobre el código y los algoritmos utilizados. Las fechas de las presentaciones serán anunciadas posteriormente.

**Fecha Límite de Entrega:**
- Semana del 28 de octubre. Durante esa semana los grupos realizarán la presentación oral de su trabajo en clase.

**Evaluación:**
- La correcta implementación de los algoritmos y estructuras de datos.
- La eficiencia y claridad del código.
- La documentación y presentación del trabajo.
- La colaboración y el trabajo en equipo.

### Instrucciones Adicionales para el Trabajo en Grupo

- **Formación de Grupos:** Cada grupo debe estar conformado por 4 o 5 estudiantes.
- **Distribución de Tareas:** Es importante que cada integrante del grupo tenga una responsabilidad clara. Se recomienda asignar tareas específicas (por ejemplo, uno se encarga del _crawler_, otro del grafo, otro del cálculo del _PageRank_, etc.) para asegurar una distribución equitativa del trabajo.
- **Coordinación y Comunicación:** Utilizar herramientas de gestión de proyectos (como Trello o Asana) y comunicación (Slack o WhatsApp) para coordinar el trabajo y mantener una comunicación fluida.
- **Control de Versiones:** Utilizar Git para colaborar en el desarrollo del código y mantener un historial de cambios

**🚨 TODOS LOS INTEGRANTES DEL EQUIPO DEBERAN HACER COMMITS AL REPOSITORIO PARA DEMOSTRAR SU PARTICIPACIÓN EN EL DESARROLLO 🚨**.
