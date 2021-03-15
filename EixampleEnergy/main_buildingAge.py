import geopandas

import matplotlib;
import pandas as pd

from EixampleEnergy.drawer import Drawer

#matplotlib.use("TkAgg")


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
    df["gr_by_age"] = df['build_date'].apply(build_date_group)
    df = df.sort_values(by=["gr_by_age"])
    return df


def main():
    df = clean_data(load())

    # exit()

    drawer = Drawer(df, data_x="build_date", data_y="RES_energy", data_time='gr_by_age',
                    x_label="Build year", y_label="Energy (kWh/year)",
                    map_xlim=(2.05, 2.23), map_ylim=(41.313, 41.47),
                    #background_img_path='../out/background_greyscale.tif',
                    has_map=True, has_chart=True,
                    chart_dot_size=1, chart_line_size=0,
                    is_save_anim_png=True,
                    dpi=600)

    # drawer.download_map_bg()

    #drawer.draw_anime('../out/animation_inigo.gif')
    drawer.draw_static('../out/static_inigo.png')


if __name__ == '__main__':
    main()
