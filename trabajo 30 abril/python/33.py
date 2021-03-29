#ejercicio 33
year = int(input("ingrese el año="))
if year%4!=0:
    print("no es bisiesto")
elif year%4 ==0 and year%100!=0:
    print("es bisiesto")
elif year%4==0 and year%100==0 and year%400!=0:
    print("no es bisisesto")
elif year%4==0 and year%100==0 and year%400==0:
    print("es bisisesto")