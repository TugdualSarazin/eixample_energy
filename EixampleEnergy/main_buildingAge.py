import geopandas

import matplotlib;
import pandas as pd

from EixampleEnergy.drawer import Drawer

matplotlib.use("TkAgg")


def load():
    return geopandas.read_file('../data/Buildings_SJ/BCN_Avg_Energy_4326.shp')




def build_date_group(build_date):
    if build_date < 1979:
        return "group_01"
    elif build_date >= 1979 and build_date < 1986:
        return "group_02"
    elif build_date >= 1986 and build_date < 2005:
        return "group_03"
    else:
        return "group_04"

def clean_data(df):
    # df = df[["build_date","RES_energy","geometry"]]
    df = df[df['build_date'] > 1900]
    df["gr_by_age"]= df['build_date'].apply(build_date_group)
    return df


def main():
    df = clean_data(load())

    # exit()

    drawer = Drawer(df, chartx="build_date", charty="RES_energy",
                    x_label="Build year", y_label="Energy (kWh/m2/year)",
                    map_xlim=(2.13, 2.20), map_ylim=(41.373, 41.413),
                    update_background=False,
                    dpi=300
                    )

    #drawer.draw_anime('../out/animation.gif')
    drawer.draw_static('../out/static.png')


if __name__ == '__main__':
    main()
