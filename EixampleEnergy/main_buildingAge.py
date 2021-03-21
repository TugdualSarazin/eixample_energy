from EixampleEnergy.drawers.drawer import Drawer

from EixampleEnergy.tool import load_shapefile
from EixampleEnergy.drawers.drawer_chart import DrawerChart
from EixampleEnergy.drawers.drawer_map import DrawerMap


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
    df = df[df['build_date'] > 1900]
    df["gr_by_age"] = df['build_date'].apply(build_date_group)
    df = df.sort_values(by=["gr_by_age"])
    return df


def main():
    df = clean_data(load_shapefile('../data/Buildings_SJ/BCN_Avg_Energy_4326.shp'))
    drawer_map = DrawerMap(full_df=df,
                           color_col="RES_energy",
                           xlim=(2.05, 2.23),
                           ylim=(41.313, 41.47))
    drawer_chart = DrawerChart(full_df=df,
                               xcol="build_date",
                               ycol="RES_energy",
                               xlabel="Build year",
                               ylabel="Energy (kWh/year)",
                               dot_size=0.5, line_size=1)

    drawer = Drawer(full_df=df,
                    drawers=[drawer_map, drawer_chart],
                    time_col='gr_by_age',
                    # dpi = 600,
                    dpi=72,
                    save_dir_path='../out/building_age/')
    
    drawer.draw_anime(save_anim_imgs=True, show=False)
    # drawer.draw_static()


if __name__ == '__main__':
    main()
