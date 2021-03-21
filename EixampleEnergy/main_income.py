import pandas as pd

from EixampleEnergy.drawers.drawer import Drawer
from EixampleEnergy.tool import load_shapefile
from EixampleEnergy.drawers.drawer_chart import DrawerChart
from EixampleEnergy.drawers.drawer_map import DrawerMap


def clean_data(df):
    frames = 20
    df["Avg_in_hou"] = df['Avg_in_hou'].apply(lambda str_avg: float(str_avg.replace(',', '.')))
    df["Avg_age"] = df['Avg_age'].apply(lambda str_avg: float(str_avg.replace(',', '.')))
    df['quantile_time'] = pd.qcut(df['Avg_in_hou'], frames, labels=False)
    return df


def main():
    df = clean_data(load_shapefile('../data/Income/BCN_City_Income.shp'))
    drawer_map = DrawerMap(full_df=df,
                           color_col="Avg_in_hou",
                           xlim=(2.02, 2.26),
                           ylim=(41.313, 41.47))
    drawer_chart = DrawerChart(full_df=df,
                               xcol="Avg_in_hou",
                               ycol="Avg_age",
                               xlabel="Avg_in_hou",  # "Energy (kWh/year)"
                               ylabel="Building age",
                               dot_size=1, line_size=0)

    drawer = Drawer(full_df=df,
                    drawers=[drawer_map, drawer_chart],
                    time_col='quantile_time',
                    # dpi = 600,
                    dpi=72,
                    save_dir_path='../out/income/')
    # drawer.draw_anime(save_anim_imgs=True)
    drawer.draw_static()


if __name__ == '__main__':
    main()
