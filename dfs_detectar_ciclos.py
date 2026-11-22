vertices = ["1", "2", "3", "4", "5"]
arestas = [
    ["1", "2"],
    ["1", "3"],
    ["2", "4"],
    ["3", "4"],
    ["4", "5"],
    ["5", "1"],
]

def dfs_detectar_ciclos(vertices, arestas, vertice_inicial):
    pilha = [(vertice_inicial, None)]
    visitados = set()

    while pilha:
        vertice_atual, pai = pilha.pop()

        if vertice_atual in visitados:
            continue

        visitados.add(vertice_atual)

        vizinhos = [aresta[1] for aresta in arestas if aresta[0] == vertice_atual]

        for vizinho in vizinhos:
            if vizinho not in visitados:
                pilha.append((vizinho, vertice_atual))
            elif vizinho != pai:
                return True

    return False

dfs_detectar_ciclos(vertices, arestas, "1")