#ejercicio 47
n = int(input("n="))
m = int(input("m="))

if m>n:
    for i in range(n+1,m):
        print(i)
else:print("m es menor que n")