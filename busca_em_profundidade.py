vertices = ["1", "2", "3", "4", "5"]
arestas = [
    ["1", "2"],
    ["1", "3"],
    ["2", "4"],
    ["3", "4"],
    ["4", "5"],
    ["5", "1"],
]

def busca_em_profundidade(vertices, arestas, vertice_inicial):
    pilha = [vertice_inicial]
    visitados = []

    while pilha:
        vertice_atual = pilha.pop()

        visitados.append(vertice_atual)

        vizinhos = [aresta[1] for aresta in arestas if aresta[0] == vertice_atual]

        for vizinho in vizinhos:
            if vizinho not in pilha and vizinho not in visitados:
                pilha.append(vizinho)

    return visitados

busca_em_profundidade(vertices,arestas,"1")