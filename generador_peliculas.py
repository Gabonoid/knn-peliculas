import random
import csv

# Lista de películas y géneros
peliculas = ["Rapidos y Furiosos", "Borat", "Hereditary", "Saw X", "After"]
generos = ["Acción", "Comedia", "Drama", "Terror", "Romance"]

# Crear una lista vacía para almacenar los registros
registros = []

# Generar 500 registros aleatorios
for i in range(500):
    calificacion_persona = []
    for j in range(5):
        calificacion_persona.append(random.randint(1, 10))
    gen_fav = random.choice(generos)

    registros.append([i] + calificacion_persona + [gen_fav])

# Crear un archivo CSV y escribir los registros en él
path = "bd_peliculas.csv"
with open(path, mode="w", newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    header = ["Persona"] + peliculas + ["Genero_Favorito"]
    print(header)
    writer.writerow(header)
    writer.writerows(registros)

print(f"Base de datos generada y guardada en '{path}'")
