import matplotlib.pyplot as plt
import pandas as pd

class Grafico:
    #Constructor
    def __init__(self, archivo):
        self.archivo = archivo
        self.dt = pd.read_csv(self.archivo)

    def grafico_simple(self,tipo_grafico, columna):

        fig, ax = plt.subplots()

        self.dt[columna].sum().plot(kind=tipo_grafico, ax=ax)

        ax.set_title("Grafico {}".format(columna), loc = "center", fontdict = {'fontsize':14, 
        'fontweight':'bold', 'color':'tab:blue'})
        ax.set_ylabel('')
        plt.savefig('img/grafico' + ' - '+ columna + '.png', bbox_inches='tight')
    
    def grafico(self,tipo_grafico,col1,col2):

        fig, ax = plt.subplots()

        self.dt.groupby(col1)[col2].sum().plot(kind=tipo_grafico, ax=ax)

        ax.set_title("Grafico {} {}".format(col1, col2), loc = "center", fontdict = {'fontsize':14, 
        'fontweight':'bold', 'color':'tab:blue'})
        ax.set_ylabel('')
        plt.savefig('img/grafico' + ' - '+ col1 + col2 + '.png', bbox_inches='tight')

grafico1 = Grafico("WineQT.csv")
grafico1.grafico("bar","")