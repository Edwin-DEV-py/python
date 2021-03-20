#ejercicio 1
print('ejercicio#1')
print(list(range(10)))

#ejercicio 2
print("ejercicio#2")
print(list(range(101,199)))

#ejercicio 3
print("ejercicio#3")
print(list(range(6,20,3)))

#ejercicio 4
print("ejercicio#4")
N=int(input('Ingrese un numero:'))
for i in range(N,N*2):
    print(i)

#ejercicio 5
print("ejercicio#5")
c=int(input("Cantidad de números: ")) 
total=0 
for variable in range(c): 
   numero=int(input("Número: ")) 
   total+=numero 
print("Total de la suma:", total) 

#ejercicio 6
def obtenet_vocales(frase):
    vocales='aeiouAEIOU'
    return[c for c in frase if c in vocales]
texto =str(input("escriba: "))
print(obtenet_vocales(texto))

#ejercicio 7
print("ejercico#7")
c=100
x=0
for i in range(c):
    x+=i
print(x)

#ejercicio 8
print("ejercicio#8")
yearinicio=int(input("año inicial:"))
yearfinal=int(input("año final:"))
for year in range(yearinicio,yearfinal):
    if year%10==0:
        continue
    if not year%4==0:
        continue
    if year%100 !=0 or year%400==0:
        print(year)

#ejercicio 9
print("ejercicio#9")
f=1
p=int(input("ingrese el numero:"))
if p!=0:
    for i in range(1,p+1):
        f=f*i
print("factorial: ",f)

#ejercicio 10
print("ejercicio#10")
def fib(n):
    a=0
    b=1
    for k in range(n):
        c=a+b
        a=b
        b=c
    return b
for x in range(10):
    print(fib(x))

