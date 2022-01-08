'''
selectiva_simple_2.py
script en Python que genere un numero aleatorio entre 1 y 10 y le pida al usuario que intente adivinarlo.Si adivina el numero que lo felicite por su logro.
'''

#Agreaga el modulo random a mi programa y con ello me permite generar
#numeros aleatorios
import random

secreto = random.randint(1, 10)

print('Acabo de generar un numero aleatorio entre 1 y 10 intenta adivinarlo')

numero =int(input('cual crees que sea el numero?'))

if numero==secreto:
    print('Felicidades eres un mago')


print('Sigue intentando')
