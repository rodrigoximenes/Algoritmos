# algoritmos/algoritmo2.py

def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1  # Retorna -1 se o elemento não for encontrado

# Teste do algoritmo
def executa_busca_binaria():
    lista = [10, 22, 35, 40, 55, 68, 72, 81, 94]
    elemento = 55
    posicao = busca_binaria(lista, elemento)
    if posicao != -1:
        return f"Elemento {elemento} encontrado na posição {posicao}."
    else:
        return f"Elemento {elemento} não encontrado na lista."
