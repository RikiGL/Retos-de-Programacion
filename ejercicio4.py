'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''
def esPrimo(numero):
    if numero < 2:
        return False
    
    # Solo verificamos hasta la raíz cuadrada del número
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


# Imprime los numeros primos entre 1 y 100
for num in range(1, 101):
    if esPrimo(num):
        print(num)


# Comprueba si un numero ingresado es primo
ingreso = int(input("Ingrese un valor: "))

if esPrimo(ingreso):
    print(f'{ingreso} es primo')
else:
    print(f'{ingreso} no es primo')
