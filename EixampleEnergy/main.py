import geopandas
import pandas as pd
import matplotlib.pyplot as plt

from EixampleEnergy.draw_chart import draw_chart
from EixampleEnergy.draw_map import draw_map


def load():
    return geopandas.read_file('../data/EIX_Buildings_energy_consumption.shp')


def draw(df):
    fig, axs = plt.subplots(2)
    fig.suptitle(str("Hey"))

    draw_map(axs[0], df)
    draw_chart(axs[1], df)
    plt.show()


def main():
    df = load()
    # df = df.head(100)
    draw(df)


if __name__ == '__main__':
    main()
