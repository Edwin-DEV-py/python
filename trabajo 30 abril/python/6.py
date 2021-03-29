#ejercicio 6
listaa=[]
i=1
Cantidad=5
while Cantidad>0:
    Num=(float(input('Digite su nota#'+str(i)+(':'))))
    if Num>=5.1:
        print('no se admiten valores mayores a 5')
        break   
    i+=1
    listaa.append(Num)
    Cantidad-=1
Total=(listaa[0]*0.15)+(listaa[1]*0.2)+(listaa[2]*0.15)+(listaa[3]*0.3)+(listaa[4]*0.2)
print('Su definitiva es:',Total)
if Total>=3:
    print('Aprobo')
else:
    print('Reprobo')