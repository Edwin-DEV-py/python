#ejercicio 38
lista=[]
contador=int(input("cuantos numero ingresara?="))
i=1
while contador>0:
    num=int(input("#"+str(i)+":"))
    i+=1
    lista.append(num)
    contador-=1
uno=lista[0]
dos=lista[-1]

if dos>uno:
    print("la secuencia incrementa")
else:print("la secuencia decrementa")