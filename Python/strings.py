my_string = "Hola Mundo!\n"
print(my_string)

my_string = 'Hola "Mundo"!\n'
print(my_string)

my_string = "Hola 'Mundo'!\n"
print(my_string)

my_string = ''' Hola Mundo!\n ''' # Este string contiene saltos de linea al princio
print(my_string)

my_string = "Hola \nMundo!\n"    # Este string contiene saltos de linea en medio
print(my_string)



course = "Python3"
name = "Matias"

final_message = "Nuevo curso de "+ course+ " por "+ name            # Primera forma de unir strings
print(final_message)

final_message = "Nuevo curso de %s por %s" %(course, name)          # Segunda forma de unir strings
print(final_message)

final_message = "Nuevo curso de {} por {}" .format(course, name)    # Tercera forma de unir strings
print(final_message)