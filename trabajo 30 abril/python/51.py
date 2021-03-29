#ejercicio 51
k=int(input("numeros?="))
lista1=[]
lista2=[]
r=1
while r>0:
    for i in range(k):
        if i%2==0:
            lista1.append(i)
    for i in range(k):
        if i%2!=0:
            lista2.append(i)
    r-=1
print(lista1)
print(lista2)