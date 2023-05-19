x = 0.001
ax = 2*x**2 + 4/x
listax = []
listay= []
while x < 20:
    y = 2*x**2 + 4/x
    listay.append(y)
    listax.append(x)
    x += 0.1 
    
def acha_menor(lista):
    menor = lista[0]
    indice_menor = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i 
    return indice_menor

local_menor = acha_menor(listay)
print(listay[local_menor])