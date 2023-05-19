def acha_maior(lista):
    maior = lista[0]
    indice_maior = 0 
    for i in range(len(lista)):
        if lista[i]>maior:
            maior = lista[i]
            indice_maior = i 
    return indice_maior 

def acha_menor(lista):
    menor = lista[0]
    indice_menor = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i 
    return indice_menor

listaf = []
listax = []
x = -10
# nao eh asolução usar o for pq nao poderiamos conseguir chegar em numeros quebrados
# existem diversas dificuldades nisso

while x < 20:
    f = x**2 - 23*x + 132
    listaf.append(f)
    listax.append(x)
    x += 0.1 
    print(listaf)
    print(listax)

local_menor = acha_menor(listaf)
print(listaf[local_menor])
print(listax[local_menor])


