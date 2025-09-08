from collections import deque
from typing import List
class Solution:
    def shortestPath(self, labirinto: List[List[int]], k: int) -> int:
        linhas, colunas = len(labirinto), len(labirinto[0])  # Dimensões
        if k >= linhas + colunas - 2: return linhas + colunas - 2  # Caminho trivial sem obstáculos
        return self.bfs(labirinto, k)  # Chama BFS principal
    def bfs(self, mapa: List[List[int]], k: int) -> int:
        fila = deque([(0, 0, k, 0)])  # Linha, coluna, obstáculos restantes e passos
        visitados = set([(0, 0, k)])  # Estados já visitados
        while fila:
            nivel = len(fila)  # Tamanho do nível
            for _ in range(nivel):  # Percorre nível
                lin, col, resto, passos = fila.popleft()  # Pega elemento
                if lin == len(mapa)-1 and col == len(mapa[0])-1: return passos  # Destino alcançado
                vizinhos = self.gerar_vizinhos(lin, col, len(mapa), len(mapa[0]))  # Gera vizinhos
                idx = 0
                while idx < len(vizinhos):  # Percorre vizinhos
                    nlin, ncol = vizinhos[idx]
                    novos_resto = resto - mapa[nlin][ncol]  # Calcula obstáculos restantes
                    if novos_resto >= 0 and (nlin, ncol, novos_resto) not in visitados:  
                        visitados.add((nlin, ncol, novos_resto))  # Marca visitado
                        fila.append((nlin, ncol, novos_resto, passos + 1))  # Adiciona no final da fila
                    idx += 1
        return -1  
    def gerar_vizinhos(self, lin: int, col: int, linhas: int, colunas: int) -> List[tuple[int, int]]:
        direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Direita, baixo, esquerda e em cima
        resultado = []
        idx = 0
        while idx < len(direcoes):  # Percorre direções
            dl, dc = direcoes[idx]
            nlin, ncol = lin + dl, col + dc
            if 0 <= nlin < linhas and 0 <= ncol < colunas: resultado.append((nlin, ncol))  # Válido
            idx += 1
        return resultado  # Retorna vizinhos
