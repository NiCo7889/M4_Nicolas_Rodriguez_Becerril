import pandas as pd 

def main():
    titulos_de_peliculas = pd.read_csv('imdb_titulos.csv')
    print(titulos_de_peliculas.head(5))

    elenco = pd.read_csv('imdb_elenco.csv')
    print(elenco.head(5))




if __name__ == '__main__':
    main()