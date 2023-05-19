def bhaskara(a, b, c):

    delta = (b**2 - 4*a*c)**(1/2)
    
    if delta == 0:
        print("Não existem raízes reais")
    else:

        x1 = (-b + delta)/ (2*a) 
        x2 = (-b - delta)/ (2*a)

        print(f"Os resultados de sua equação do segundo grau são: x1 = {x1} e x2 = {x2}")
        print(delta)
    xv = -b/(2*a)
    yv = -(delta)**2/(4*a)




    print(f"Já o x do vértice é {xv} e o y do vértice é {yv}")

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))


bhaskara(a, b, c)


listay = []
listax = []

x = -10
while x < 10:
    y = a*x**2 + b*x + c
    listay.append(y)
    listax.append(x)
    x += 0.1 
    print(listay)
    print(listax)