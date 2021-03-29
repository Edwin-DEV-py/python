#ejercicio 30
lista=[]
contador=3
i=1
while contador>0:
    numero=int(input("digite su #"+str(i)+":"))
    lista.append(numero)
    contador-=1
    i+=1
mayor=max(lista)
menor=min(lista)
print("mayor=",mayor)
print("menor=",menor)