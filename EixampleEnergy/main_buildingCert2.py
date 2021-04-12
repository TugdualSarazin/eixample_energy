import matplotlib.pyplot as plt

from EixampleEnergy.tool import load_shapefile
from EixampleEnergy.drawers.drawer import Drawer
from EixampleEnergy.drawers.drawer_map import DrawerMap
from EixampleEnergy.drawers.drawer_stacked_bar import DrawerStackedBar


def clean_data(df):
    df = df[df['build_date'] > 1900]
    df['build_date_10'] = df['build_date'].apply(lambda date: date - (date % 10))
    return df


def main():
    df = load_shapefile('../data/BCN_Private_communities/BCN_Private_communities_4326.shp')
    df = clean_data(df)
    cmap = plt.cm.RdYlGn.reversed()
    drawer_map = DrawerMap(full_df=df,
                           color_col="E_certific",
                           xlim=(2.05, 2.23),
                           # ylim=(41.313, 41.47),
                           bg_img='../out/background_greyscale.tif',
                           cmap=cmap)
    drawer_stacked = DrawerStackedBar(full_df=df,
                                      xcol='build_date_10',
                                      group_col='E_certific',
                                      xlabel="Build year",
                                      ylabel="Energy Certificate",
                                      cmap=cmap)

    drawer_map.download_bg('../out/bg.tif')
    exit()

    drawer = Drawer(full_df=df,
                    drawers=[drawer_map],
                    # drawers=[drawer_map, drawer_stacked],
                    time_col='build_date_10',
                    dpi=600,
                    # dpi=72,
                    save_dir_path='../out/building_cert2/map/')

    # drawer.draw_anime(save_anim_imgs=True, show=False)
    drawer.draw_static()


if __name__ == '__main__':
    main()
