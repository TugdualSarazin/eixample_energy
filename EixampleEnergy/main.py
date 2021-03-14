import geopandas

import matplotlib;

from EixampleEnergy.drawer import Drawer

matplotlib.use("TkAgg")


def load():
    return geopandas.read_file('../data/EIX_superblock_buildings_energy_consumption_4326.shp')


def clean_data(df):
    df = df[df['build_date'] > 1900]
    df = df[df['E_final'] < 250]
    df = df[df.superblock.notna()]
    return df


def main():
    df = clean_data(load())

    drawer = Drawer(df, data_x="build_date", data_y="E_final", data_time='superblock',
                    x_label="Build year", y_label="Energy (kWh/m2/year)",
                    map_xlim=(2.13, 2.20), map_ylim=(41.373, 41.413),
                    update_background=True,
                    dpi=300
                    )

    #drawer.draw_anime('../out/animation.gif')
    drawer.draw_static('../out/static.png')


if __name__ == '__main__':
    main()
