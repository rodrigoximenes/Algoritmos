
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Teste do algoritmo
def executa_bubble_sort():
    numeros = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", numeros)
    ordenada = bubble_sort(numeros)
    return f"Lista ordenada: {ordenada}"
