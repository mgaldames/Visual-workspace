menu = """
Bienvenidos al conversor de monedas 💲

1 - Pesos Chilenos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input("¿Cúantos pesos chilenos tienes?: "))
    valor_dolar = 836
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)   ## el resultado de dolares queda acortado a solo 2 decimales
    dolares = str(dolares)          ## el resultado de dolares lo muestra como texto
    print("Tienes $" + dolares  + " dólares")
elif opcion == 2:
    pesos = float(input("¿Cúantos pesos argentinos tienes?: "))
    valor_dolar = 114
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)   ## el resultado de dolares queda acortado a solo 2 decimales
    dolares = str(dolares)          ## el resultado de dolares lo muestra como texto
    print("Tienes $" + dolares  + " dólares")
elif opcion == 3:
    pesos = float(input("¿Cúantos pesos mexicanos tienes?: "))
    valor_dolar = 20
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)   ## el resultado de dolares queda acortado a solo 2 decimales
    dolares = str(dolares)          ## el resultado de dolares lo muestra como texto
    print("Tienes $" + dolares  + " dólares")
else:
    print("Ingresa una opción correcta por favor")



