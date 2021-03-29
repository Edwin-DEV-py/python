#ejercicio 56
n = int(input("numero="))
contador = 0
for i in range(n,0,-1):
    if n%i==0:
        contador+=1
print(contador)
