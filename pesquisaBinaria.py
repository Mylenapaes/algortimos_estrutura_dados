"""
                         Pesquisa Binária:
A pesquisa binária é um problema de busca de um elemento em uma lista (vetor) ordenada. Se o elemento bsucado estiver na lista, a pesquisa binária retorna a posição do elemento na lista. Caso contrário, a pesquisa binária retorna o seu indice, senão retorna None.
Vale ressaltar que com a pesquisa binária, você elimina metade dos items da lista a cada iteração, entretanto, a lista deve estar ordenada.

"""

def pesquisa_binaria(lista, valorBuscado):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        indiceMeio = (esquerda + direita) // 2
        valorMeio = lista[indiceMeio]
        if valorMeio == valorBuscado:
            return indiceMeio
        if valorMeio > valorBuscado:
            direita = indiceMeio -1
        else:
            esquerda = indiceMeio + 1
    return None

def recebe_itens(numlista):
    lista = []
    for i in range(numlista):
        i = int(input("Digite o item que quer adicionar na lista: "))
        lista.append(i)
    return lista

tamanho = int(input("Digite o tamanho da lista: "))
lista = recebe_itens(tamanho)
busca = int(input("Digite o item que deseja pesquisar: "))
print (pesquisa_binaria(lista, busca))
