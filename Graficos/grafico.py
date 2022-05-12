import matplotlib.pyplot as plt
import pandas as pd

class Grafico:
    #Constructor
    def __init__(self, archivo):
        self.archivo = archivo
        self.dt = pd.read_csv(self.archivo)
    
    def grafico(self,tipo_grafico,col1,col2):

        fig, ax = plt.subplots()

        self.dt.groupby(col1)[col2].sum().plot(kind=tipo_grafico, ax=ax)

        ax.set_title("Grafico {} {}".format(col1, col2), loc = "center", fontdict = {'fontsize':14, 
        'fontweight':'bold', 'color':'tab:blue'})
        ax.set_ylabel('')
        plt.savefig('Graficos/grafico' + ' - '+ col1 + col2 + '.png', bbox_inches='tight')


#Una segunda forma de crear graficos

def grafico_2(dataset, tipo_grafico, titulografico, nombregrafico):
    fig, ax = plt.subplots()
 
    dataset.plot(kind=tipo_grafico, ax = ax, color = "red")
    ax.set_title(str(titulografico), loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:orange'})
    ax.set_ylabel('')

    plt.savefig('{}.png'.format(nombregrafico), bbox_inches='tight')

    plt.show()

grafico_2(calidad, "hist", "CALIDAD VINO", "grafico")