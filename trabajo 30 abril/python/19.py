#ejercicio 19
segundos = int(input("segundos="))
minutos = int(segundos/1800)
horas = int(segundos*(1/60)*(1/60))
segundo = int(segundos%60)
print("horario=",horas,":",minutos,":",segundo)
