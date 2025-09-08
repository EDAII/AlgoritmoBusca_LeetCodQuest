from collections import deque
class Solution:
    def minDays(self, laranjas: int) -> int:
        memoria = {}  
        return self.dfs(laranjas, memoria)  # Chama a busca principal
    def dfs(self, qtd: int, memoria: dict) -> int:
        if qtd in memoria: return memoria[qtd]  
        if qtd < 2: return qtd  # Caso base
        dividir2 = (qtd % 2) + self.dfs(qtd // 2, memoria)  # Tenta dividir por 2
        dividir3 = (qtd % 3) + self.dfs(qtd // 3, memoria)  # tenta dividir por 3
        memoria[qtd] = 1 + min(dividir2, dividir3)  # Guarda o melhor
        return memoria[qtd]
    def bfs(self, laranjas: int) -> int:
        fila = deque([laranjas])  # Fila de estados
        vistos = {laranjas}  
        passos = 0  # Dias acumulados
        for _ in iter(int, 1):  
            tamanho = len(fila)  # Nível atual
            if tamanho == 0: break  
            contador = 0  # Indice dentro do nível
            while contador < tamanho:  # percorre nível
                atual = fila.popleft()  # Retira estado
                if atual == 0: return passos  # Chegou no fim
                proximos = self.transicoes(atual)  # Gera próximos
                idx = 0  # Índice da lista
                while idx < len(proximos):  # Percorre próximos
                    prox = proximos[idx]
                    if prox not in vistos:  
                        vistos.add(prox)
                        fila.append(prox)
                    idx += 1
                contador += 1
            passos += 1  # Aumenta contador
        return passos
    def transicoes(self, qtd: int) -> list:
        lista = [qtd - 1]  
        if qtd % 2 == 0: lista.append(qtd // 2)  
        if qtd % 3 == 0: lista.append(qtd // 3)  
        return lista
