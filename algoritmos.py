import math


def distancia_euclidiana(propuesto, datos):
    distancias = []
    for fila in datos:
        indice_persona = fila.pop(0)
        gen_favorito = fila.pop(-1)

        distancia = math.sqrt(
            sum((dato-var_propuesto)**2 for dato, var_propuesto in zip(fila, propuesto))
        )

        distancias.append([indice_persona] + [distancia] +
                          fila + [gen_favorito])
    distancias = sorted(distancias, key=lambda x: x[1])
    return distancias


def vecinos(peliculas, distancias, k):
    recomendaciones = {}
    for i in range(k):
        distancia = distancias[i]
        id = distancia.pop(0)
        val_distancia = round(distancia.pop(0), 4)
        genero = distancia.pop(-1)
        
        print(f'Persona {id}'.center(50, '-'))
        print(
            f'La persona {id} tuvo una distancia de {val_distancia} con el genero favorito "{genero}". Sus calificaciones fueron:')
        for i, calificacion in enumerate(distancia):
            print(f'    "{peliculas[i]}": {calificacion}')
        
        if genero not in recomendaciones:
            pelicula_fav = peliculas[distancia.index(max(distancia))]
            recomendaciones[genero] = pelicula_fav
    return recomendaciones

def recomendar_pelicula(generos):
    peliculas = {
        "Acción": "Resident Evil",
        "Comedia": "Deadpool",
        "Drama": "Los Juegos del Hambre",
        "Terror": "The Fly",
        "Romance": "La La Land",
    }
    for genero in generos:
        print(f'Pelicula recomendada para el genero "{genero}": {peliculas[genero]}')
    