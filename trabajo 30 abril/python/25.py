#ejercicio 25
def precio(iva,valor,valor_iva):
    valor_iva = iva*valor
    total = valor_iva+valor
    return total

iva = 0.19
valor = int(input("valor del producto="))
valor_iva=0

valor_pagar = precio(iva,valor,valor_iva)
print(f'total a pagar es: {valor_pagar}.')

if valor>=150000:
    descuento=valor*0.05
    total_descuento=valor_pagar-descuento
    print("el valor con descuento por compras mayore a 150.000 es de:",total_descuento)
