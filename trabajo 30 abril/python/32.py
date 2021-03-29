#ejercicio 32
def valor_pagar(km,dias):
    total=km*5000
    return total


km=int(input("km a recorrer="))
dias=int(input("dias que se quedara="))

if km<20:
    print("son muy pocos km")
    exit()

valor_a_pagar = valor_pagar(km,dias)
print(f'Su total a pagar es:{valor_a_pagar}')

if km>=1000 and dias>=7:
    descuento=valor_a_pagar*0.15
    print("se gano un descuento de=",descuento)



