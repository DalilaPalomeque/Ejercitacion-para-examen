#1) Realice un programa que muestre el mensaje “Hola Aula X (Indicar el número de aula a la que pertenecen),
#¿Qué tal?” en tres veces intercambiados entre ellos otros mensajes a su elección.

def mensajes_aula(mensaje):
    print(mensaje)
    respuesta = input("Ingresa tu respuesta: ")
    return respuesta

#Mensaje inicial
numero_aula = input("Ingresa el número de aula: ")
mensaje_inicial = f"Hola Aula {numero_aula}, ¿Qué tal?"
respuesta_inicial = mensajes_aula(mensaje_inicial)
print("Respuesta al mensaje inicial:", respuesta_inicial)

#Segundo Mensaje
mensaje_segundo = "¿Están listos para el nuevo ciclo lectivo?"
respuesta_segundo = mensajes_aula(mensaje_segundo)
print("Respuesta al segundo mensaje:", respuesta_segundo)

#Tercer mensaje
mensaje_tercero = "¡Bienvenidos!"
respuesta_tercero = mensajes_aula(mensaje_tercero)
print("Respuesta al tercer mensaje:", respuesta_tercero)

mensajes_aula()

#2) A partir del siguiente ejemplo “Hola Ana, ¿Qué tal?” realizar el programa la ejecución del mismo con al menos otros
#dos nombres más, es decir, tres mensajes con tres nombres distintos. Recuerda: en estos ejercicios trabajamos argumentos.

def saludo(nombre):
    mensaje = f"Hola {nombre}, ¿Qué tal?"
    print(mensaje)

nombres = ["Ana", "Liliana", "Delia"]

for nombre in nombres:
    saludo(nombre)

#3)Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma. Mostrar el resultado dos veces.

def sumar( a, b , c):
    resultado = a + b + c
    return resultado
resulado_sumar = sumar(1, 2, 3)
print(resulado_sumar)
resulado_sumar = sumar(4, 5, 6)
print(resulado_sumar)

# 4)Realice un programa que lea dos números (dos parámetros), compare si son IGUALES, en ese caso, mostrar un mensaje que muestre TRUE.

def comparacion():
   a = input('Ingrese el primer número:')
   b = input('Ingrese el segundo número:')
   if a==b :
      print('TRUE')
   else:
      print('FALSE')
comparacion()

# 5)Realice un programa que contenga una función que se llame “sumayresta”, que la misma contenga dos variables locales
# nombradas suma y resta, respectivamente. Recuerda: en estos ejercicios trabajamos argumentos para este ejercicio sería dos.

def sumayresta(a,b):
    suma = a + b
    print(suma)
    resta = a - b
    print(resta)
sumayresta(18,23)