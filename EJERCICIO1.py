import pandas as pd # Importa pandas y usa un alias para poder utilizar sus recursos

def main():
    # Cargar como dataframe de pandas el csv imdb_titulos.csv y mostrar sus 5 primeros registros
    titulos_de_peliculas = pd.read_csv('imdb_titulos.csv')
    print(titulos_de_peliculas.head(5))

    # Cargar como dataframe de pandas el csv imdb_elenco.csv y mostrar sus 5 primeros registros
    elenco = pd.read_csv('imdb_elenco.csv')
    print(elenco.head(5))

    # Mostrar el número de registros del dataframe de titulos

    # Mostrar el número de registros del dataframe de elenco

    # Mostrar las 5 peliculas más antiguas del listado de titulos





