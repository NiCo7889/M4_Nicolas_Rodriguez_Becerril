import pandas as pd # Importa pandas y usa un alias para poder utilizar sus recursos

def main():
    # Cargar como dataframe de pandas el csv imdb_titulos.csv y mostrar sus 5 primeros registros
    titulos_de_peliculas = pd.read_csv('imdb_titulos.csv')
    print(titulos_de_peliculas.head(5))

    # Cargar como dataframe de pandas el csv imdb_elenco.csv y mostrar sus 5 primeros registros
    elenco = pd.read_csv('imdb_elenco.csv')
    print(elenco.head())

    # Mostrar el número de registros del dataframe de titulos
    print("Mostrar el número de registros del dataframe de titulos{} ".format(len(titulos_de_peliculas.shape)))

    # Mostrar el número de registros del dataframe de elenco
    print("Mostrar el número de registros del dataframe de elenco{} ".format(len(elenco.shape)))

    # Mostrar las 5 peliculas más antiguas del listado de titulos
    print(titulos_de_peliculas.sort_values(by='año').head(5))

    # Mostrar las peliculas que en el titulo tienen la palabra "Dracula". También mostrar el número total de peliculas que coincidan con este requisito
    print(titulos_de_peliculas[titulos_de_peliculas['titulo'].str.contains('Dracula')])
    print("Mostrar las peliculas que en el titulo tienen la palabra Dracula. También mostrar el número total de peliculas que coincidan con este requisito{} ".format(len(titulos_de_peliculas[titulos_de_peliculas['titulo'].str.contains('Dracula')])))
    print(titulos_peliculas[titulos_peliculas['title'].str.contains('Dracula')])  #str.contains() devuelve la subcadena indicada en el parámetro
    print("Número de peliculas que coincidan con este requisito: {} coincidencias".format(len(titulos_peliculas[titulos_peliculas['title'].str.contains('Dracula')])), "\n")



