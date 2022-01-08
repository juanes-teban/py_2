'''

selectiva_simple_3.py
script en python que le solicite al usuario sus calificaciones y su
numero de asistencia a un curso.Si la calificacion es mayor o igual que 60 y ña cantidad de asistencias es mayor que 20 entonces que indique que ha aprobado el curso

'''

calificacion =int(input('Cual es tu calificacion?'))

asistencia = int(input('cuantas asistencias tuviste'))

if calificacion >= 60 and asistencia >= 20:
    print('felicidades aprobaste el curso')

print('Adios')     
