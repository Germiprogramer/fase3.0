#otra funcion para crear gráficos

vinos = pd.read_csv("WineQT.csv", header=0)
def grafico_2(dataset, tipo_grafico, titulografico, nombregrafico):
    fig, ax = plt.subplots()
 
    dataset.plot(kind=tipo_grafico, ax = ax, color = "red")
    ax.set_title(str(titulografico), loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:orange'})
    ax.set_ylabel('')

    plt.savefig('{}.png'.format(nombregrafico), bbox_inches='tight')

    plt.show()

grafico(vinos["quality"], "bar", "Calidad del vino", "quality")