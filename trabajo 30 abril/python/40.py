#ejercicio 40
numero = int(input("dia="))
if numero<0 and numero>7:
    exit()

if numero==1:
    print("lunes")
elif numero==2:print("martes")
elif numero==3:print("miercoles")
elif numero==4:print("jueves")
elif numero==5:print("viernes")
elif numero==6:print("sabado")
elif numero==7:print("domingo")