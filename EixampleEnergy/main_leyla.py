import geopandas

import matplotlib;

from EixampleEnergy.drawer import Drawer

matplotlib.use("TkAgg")


def load():
    return geopandas.read_file('../data/Income/BCN_City_Income.shp')

from sklearn.preprocessing import MinMaxScaler

def clean_data(df, frames):
    df["Avg_in_hou_num"] = df['Avg_in_hou'].apply(lambda str_avg: float(str_avg.replace(',', '.')))
    min = df["Avg_in_hou_num"].min()
    max = df["Avg_in_hou_num"].max()
    MinMaxScaler().fit(df["Avg_in_hou_num"])

    return df


def main():
    df = load()
    df = clean_data(df, 100)

    drawer = Drawer(df, data_x="Avg_in_hou_num", data_y="Avg_in_hou", data_time='CDIS',
                    x_label="Build year", y_label="Energy (kWh/m2/year)",
                    map_xlim=(2.05, 2.23), map_ylim=(41.313, 41.47),
                    has_chart=False,
                    dpi=300
                    )

    #drawer.download_map_bg()

    drawer.draw_anime('../out/animation.gif')
    drawer.draw_static('../out/static.png')


if __name__ == '__main__':
    main()
