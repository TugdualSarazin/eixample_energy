import matplotlib.pyplot as plt
from matplotlib import pyplot
pyplot.style.use('dark_background')

from EixampleEnergy.drawers.drawer_hist import DrawerHist
from EixampleEnergy.tool import load_shapefile
from EixampleEnergy.drawers.drawer import Drawer
from EixampleEnergy.drawers.drawer_map import DrawerMap
from EixampleEnergy.drawers.drawer_stacked_bar import DrawerStackedBar


def clean_data(df):
    df = df[df['House_cons'] < 20000]
    df = df[df['House_cons'] > 0]
    df = df[df['BARRI'].notnull()]
    return df


def main():
    df = load_shapefile('../data/BCN_Private_communities_barrios/BCN_Private_communities_4326_SJ_barrios.shp')
    df = clean_data(df)
    drawer_hist = DrawerHist(full_df=df,
                            xcol='House_cons',
                            xlabel="Dwelling energy (kWh/year)",
                            ylabel="Density")

    drawer = Drawer(full_df=df,
                    drawers=[drawer_hist],
                    time_col='BARRI',
                    is_time_cumulative=False,
                    #time_col='build_date_10',
                    dpi=600,
                    #dpi=72,
                    save_dir_path='../out/building_district_consumption/')

    drawer.draw_anime(save_anim_imgs=True, show=False)
    #drawer.draw_static()


if __name__ == '__main__':
    main()
