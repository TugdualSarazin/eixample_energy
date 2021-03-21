from EixampleEnergy.tool import load_shapefile
from EixampleEnergy.drawers.drawer import Drawer

from EixampleEnergy.drawers.drawer_chart import DrawerChart
from EixampleEnergy.drawers.drawer_map import DrawerMap

x1 = 0
x2 = 34.475
x3 = 43.83 + (61.66 - 43.83) / 2
x4 = 61.66 + (88.44 - 61.66) / 2
x5 = 88.44 + (147.94 - 88.44) / 2
x6 = 147.94 + (214.71 - 147.94) / 2
x7 = 214.71 + (297.30 - 214.71) / 2


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
    df = df[df['build_date'] > 1900]
    df["gr_by_age"] = df['build_date'].apply(build_date_group)
    df["en_cert"] = df['RES_energy'].apply(energy_certificate)
    return df


def main():
    df = clean_data(load_shapefile('../data/Buildings_SJ/BCN_Avg_Energy_4326.shp'))
    drawer_map = DrawerMap(full_df=df,
                           color_col="en_cert",
                           xlim=(2.05, 2.23),
                           ylim=(41.313, 41.47),
                           bg_img='../out/background_greyscale.tif')
    drawer_chart = DrawerChart(full_df=df,
                               xcol="build_date",
                               ycol="en_cert",
                               xlabel="Build year",
                               ylabel="Energy Certificate",
                               dot_size=0.5, line_size=1)

    drawer = Drawer(full_df=df,
                    drawers=[drawer_map, drawer_chart],
                    time_col='en_cert',
                    # dpi = 600,
                    dpi=72,
                    save_dir_path='../out/building_age/')

    drawer.draw_anime(save_anim_imgs=True, show=False)
    # drawer.draw_static()


if __name__ == '__main__':
    main()
