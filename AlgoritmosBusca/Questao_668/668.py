class Solution:
    def findKthNumber(self, linhas: int, colunas: int, posicao: int) -> int:
        linhas, colunas = self.ajustar_dimensoes(linhas, colunas)  # Garante que linhas <= colunas
        if linhas == 1: return posicao  
        return self.executar_busca(linhas, colunas, posicao)  # Busca binária
    def ajustar_dimensoes(self, linhas: int, colunas: int) -> tuple[int, int]:
        if linhas > colunas: linhas, colunas = colunas, linhas  # Troca se necessário
        return linhas, colunas  # Retorna ajustado
    def contar_elementos(self, limite: int, linhas: int, colunas: int) -> int:
        acumulado = 0  
        for indice in range(1, linhas + 1):  # Percorre linhas
            acumulado += min(limite // indice, colunas)  # Conta valores
        return acumulado  # Retorna contagem
    def executar_busca(self, linhas: int, colunas: int, posicao: int) -> int:
        inicio, fim = 1, linhas * colunas  
        resultado = -1  
        for _ in range((linhas * colunas).bit_length()):  
            if inicio > fim: break  # Sai se intervalo esgotar
            candidato = (inicio + fim) // 2  # Calcula meio
            quantidade = self.contar_elementos(candidato, linhas, colunas)  # Conta <= candidato
            if quantidade >= posicao: resultado, fim = candidato, candidato - 1  # Se estiver válido, atualiza e reduz
            else: inicio = candidato + 1  # Caso contrário, aumenta
        return resultado  
