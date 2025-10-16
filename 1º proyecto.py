
### variables con input

nombre_competo = input('Introduce tu nombre completo: ')
numero_cliente = int(input('introduce el numero del cliente: '))
saldo_de_la_cuenta = float(input('saldo de la cuenta: '))
codigo_postal = input('codigo postal: ')
numero_de_telefono =input('numero de telefono: ')
edad = int(input('edad: '))
total_de_compras_anteriores = int(input('total de compras anteriores:'))
valor_de_compras_anteriores = float(input('valor de compras anteriores: '))

### Establecemos mayusculas y luego formateamos la cadena con la funcion title(la primera letra de todas las palabras en mayuscula)

Mayusculas_todo = nombre_competo.upper()
formatear_correctamente = nombre_competo.title()

### calculamos el promedio y redondeamos a 2 y 3 decimales y luego agrupamos edad,numero de clientes y saldo de la cuenta en un f_string 

compra = 225.50 
rembolso = 50

saldo_final = saldo_de_la_cuenta - compra + rembolso
redondeo_a_tres_decimales = round(saldo_final,3) 

formateado = f'{formatear_correctamente},Edad: {edad},Nº de cliente: {numero_cliente},saldo de la cuenta: {saldo_de_la_cuenta}'

valor_promedio =(total_de_compras_anteriores + 1) 
total_gastado = (valor_de_compras_anteriores + compra )
valorpromedio1 = total_gastado / valor_promedio
redondeo1 = round(valorpromedio1,2)

print(f'{valorpromedio1}')

### Remplazamos los guiones del numero de telefono por los espacios

cambiar_guiones = numero_de_telefono.replace('-',' ')

### Imprimimos para mostrar la informacion 

print(f'Identificador unico: {Mayusculas_todo}')
print(f'Nombre formateado: {formateado}')
print(f'Saldo actual: {saldo_de_la_cuenta}')
print(f'Nuevo saldo despues de la compra y rembolso: {redondeo_a_tres_decimales}')
print(f'valor promedio de compras anteriores: {redondeo1}')
print(f'Nuevo total de compras: {valor_promedio} Total gastado: {total_gastado}')
print(f'Codigo postal: {codigo_postal}')
print(f'Telefono: {cambiar_guiones}')