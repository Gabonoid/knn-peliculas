from helpers import lectura as rd
import algoritmos as al


db, peliculas  = rd.leer_archivo("data/bd_peliculas.csv")

propuestos = []

print("Del 1 al 10 ¿Qué calificacion le das a la pelicula...")
for pelicula in peliculas:
    calificacion = int(input(f'"{pelicula}"? '))
    calificacion = max(1, min(10, calificacion))
    propuestos.append(calificacion)

distancias = al.distancia_euclidiana(propuestos, db)

valor_k = int(input("¿Cuantas 'K' quieres? "))

recomendaciones = al.vecinos(peliculas, distancias, valor_k)

al.recomendar_pelicula(recomendaciones.keys())