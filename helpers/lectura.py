import pandas as pd


def leer_archivo(path):
    data = pd.read_csv(path)
    titulos = _obtener_titulos(data)
    return data.values.tolist(), titulos

def _obtener_titulos(data):
    titulos = data.columns
    titulos = titulos.tolist()
    titulos.pop(0)
    titulos.pop(-1)
    return titulos
