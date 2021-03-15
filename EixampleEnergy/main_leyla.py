import geopandas
import pandas as pd

import matplotlib;

from EixampleEnergy.drawer import Drawer

#matplotlib.use("TkAgg")


def load():
    return geopandas.read_file('../data/Income/BCN_City_Income.shp')


def clean_data(df, frames):
    df["Avg_in_hou"] = df['Avg_in_hou'].apply(lambda str_avg: float(str_avg.replace(',', '.')))
    df["Avg_age"] = df['Avg_age'].apply(lambda str_avg: float(str_avg.replace(',', '.')))
    df['quantile_time'] = pd.qcut(df['Avg_in_hou'], frames, labels=False)

    return df


def main():
    df = load()
    df = clean_data(df, 20)

    drawer = Drawer(df, data_x="Avg_in_hou", data_y="Avg_age", data_time='quantile_time',
                    x_label="Avg_in_hou", y_label="Avg_age",
                    map_xlim=(2.02, 2.26), map_ylim=(41.313, 41.47),
                    #background_img_path='../out/background_greyscale.tif',
                    has_map=True, has_chart=True,
                    chart_dot_size=1, chart_line_size=0,
                    is_save_anim_png=True,
                    dpi=300)

    #drawer.download_map_bg()

    drawer.draw_anime('../out/animation_leyla.gif')
    #drawer.draw_static('../out/static_leyla.png')


if __name__ == '__main__':
    main()
