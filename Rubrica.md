### Rúbrica para el Trabajo Práctico de Estructuras de Datos

**Puntaje Total: 10 puntos (8 puntos para el trabajo práctico y 2 puntos para la presentación oral y escrita)**

#### Trabajo Práctico (Hasta 8 puntos)

1. **Implementación del Crawler (2 puntos)**
    - **Funcionalidad Básica (1 punto):** 
        - El crawler navega por el sitio `untref.edu.ar` y recolecta enlaces internos.
    - **Manejo de Excepciones y Robustez (0.5 puntos):**
        - El crawler maneja adecuadamente las excepciones y errores (por ejemplo, enlaces rotos, tiempo de espera, etc.).
    - **Almacenamiento de Datos (0.5 puntos):**
        - Los datos recolectados son guardados correctamente en archivos CSV, con el formato adecuado.

2. **Construcción del Grafo (2 puntos)**
    - **Definición y Construcción del Grafo (1 punto):**
        - El grafo se construye correctamente a partir de los datos recolectados por el crawler, representando adecuadamente los nodos y aristas.
    - **Visualización del Grafo (1 punto):**
        - El grafo se visualiza de manera clara y legible utilizando bibliotecas gráficas apropiadas (networkx, matplotlib).

3. **Cálculo del PageRank (2 puntos)**
    - **Implementación del Algoritmo de PageRank (1 punto):**
        - El algoritmo de PageRank está correctamente implementado y calcula los valores de PageRank para cada página.
    - **Resultados y Visualización (1 punto):**
        - Los resultados del PageRank se almacenan correctamente en archivos CSV y se visualizan adecuadamente, destacando las páginas con mayores valores de PageRank.

4. **Componentes Fuertemente Conexas (2 puntos)**
    - **Implementación del Algoritmo de SCC (1 punto):**
        - El algoritmo para encontrar las componentes fuertemente conexas está correctamente implementado.
    - **Resultados y Visualización (1 punto):**
        - Los resultados de las SCC se almacenan correctamente en archivos CSV y se visualizan adecuadamente, con las SCC claramente identificadas en el grafo.

#### Presentación Oral y Escrita (Hasta 2 puntos)

1. **Presentación Escrita (1 punto)**
    - **Documentación del Código (0.5 puntos):**
        - El código está bien documentado, con comentarios claros y descripciones de las funciones y clases.
    - **Informe del Proyecto (0.5 puntos):**
        - El informe está bien estructurado y explica claramente las decisiones de diseño, la implementación y los resultados obtenidos.

2. **Presentación Oral (1 punto)**
    - **Claridad y Estructura (0.5 puntos):**
        - La presentación es clara y bien organizada, explicando de manera lógica las partes del proyecto.
    - **Respuesta a Preguntas (0.5 puntos):**
        - Los presentadores responden adecuadamente a las preguntas realizadas, demostrando comprensión de los conceptos y del trabajo realizado.

#### Distribución de Puntos

| **Categoría**                         | **Subcategoría**                         | **Puntos** |
|---------------------------------------|------------------------------------------|------------|
| Implementación del Crawler            | Funcionalidad Básica                     | 1          |
|                                       | Manejo de Excepciones y Robustez         | 0.5        |
|                                       | Almacenamiento de Datos                  | 0.5        |
| Construcción del Grafo                | Definición y Construcción del Grafo      | 1          |
|                                       | Visualización del Grafo                  | 1          |
| Cálculo del PageRank                  | Implementación del Algoritmo de PageRank | 1          |
|                                       | Resultados y Visualización               | 1          |
| Componentes Fuertemente Conexas       | Implementación del Algoritmo de SCC      | 1          |
|                                       | Resultados y Visualización               | 1          |
| Presentación Escrita                  | Documentación del Código                 | 0.5        |
|                                       | Informe del Proyecto                     | 0.5        |
| Presentación Oral                     | Claridad y Estructura                    | 0.5        |
|                                       | Respuesta a Preguntas                    | 0.5        |
| **Total**                             |                                          | **10**     |

### Notas Finales

- **Entrega Puntual:** La entrega del trabajo práctico después de la fecha límite puede resultar en una reducción de puntos.
- **Trabajo en Equipo:** Se evaluará la colaboración y el trabajo en equipo; cada integrante debe tener una responsabilidad clara.
- **Originalidad y Creatividad:** Se valorará la originalidad y creatividad en las soluciones propuestas.
