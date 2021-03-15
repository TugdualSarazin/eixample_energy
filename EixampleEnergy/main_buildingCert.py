import geopandas

import matplotlib;
import pandas as pd
from matplotlib import cm

from EixampleEnergy.drawer import Drawer

#matplotlib.use("TkAgg")


def load():
    return geopandas.read_file('../data/Buildings_SJ/BCN_Avg_Energy_4326.shp')

#calcularion of certificate ranges
x1 = 0
x2 = 34.475
x3 = 43.83 + (61.66-43.83)/2
x4 = 61.66 + (88.44-61.66)/2
x5 = 88.44 + (147.94-88.44)/2
x6 = 147.94 + (214.71-147.94)/2
x7 = 214.71 + (297.30-214.71)/2


def build_date_group(build_date):
    if build_date < 1979:
        return "group_01"
    elif build_date >= 1979 and build_date < 1986:
        return "group_02"
    elif build_date >= 1986 and build_date < 2005:
        return "group_03"
    else:
        return "group_04"

def energy_certificate(build_energy):
    if build_energy < x2:
        return 1
    elif build_energy >= x2 and build_energy < x3:
        return 2
    elif build_energy >= x3 and build_energy < x4:
        return 3
    elif build_energy >= x4 and build_energy < x5:
        return 4
    elif build_energy >= x5 and build_energy < x6:
        return 5
    elif build_energy >= x6 and build_energy < x7:
        return 6
    else:
        return 7


def clean_data(df):
    # df = df[["build_date","RES_energy","geometry"]]
    df = df[df['build_date'] > 1900]
    df["gr_by_age"] = df['build_date'].apply(build_date_group)
    df["en_cert"] = df['RES_energy'].apply(energy_certificate)
    df = df.sort_values(by=["en_cert"], ascending=False)
    return df


def main():
    df = clean_data(load())

    # exit()

    drawer = Drawer(df, data_x="build_date", data_y="en_cert", data_time="build_date",
                    x_label="Build year", y_label="Energy Certificate",
                    map_xlim=(2.05, 2.23), map_ylim=(41.313, 41.47),
                    #background_img_path='../out/background_greyscale.tif',
                    has_map=True, has_chart=False,
                    map_cmap=cm.get_cmap('PiYG', 7),
                    chart_dot_size=0.5, chart_line_size=1,
                    is_save_anim_png=True,
                    dpi=600)

    # drawer.download_map_bg()
    # "build_date"
    # "en_cert"


    drawer.draw_anime('../out/animation_e-certification')
    # drawer.draw_static('../out/static_cert.png')


if __name__ == '__main__':
    main()
