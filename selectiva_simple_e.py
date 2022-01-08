'''

selectiva_simple_e.py
script en Python que le pide al usaurio cual es su calificacion; si su calificacion es menor o es mayor redondear al mas cercano.

'''
calificacion = int(input('Cual es tu calificacion: '))
residuo= calificacion % 10
mensaje='No amerita redondeo'


if residuo >= 6:
    calificacion = calificacion +(10 - residuo)
    mensaje=f'tu calificacion es:{calificacion}'

print(mensaje)
print('Que tengas buen dia')
