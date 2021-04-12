from EixampleEnergy.drawers.drawer_stacked_bar import DrawerStackedBar
from EixampleEnergy.tool import load_shapefile
from EixampleEnergy.drawers.drawer import Drawer
from EixampleEnergy.drawers.drawer_chart import DrawerChart
from EixampleEnergy.drawers.drawer_map import DrawerMap


def clean_data(df):
    df = df[df['build_date'] > 1900]
    df = df[df['E_final'] < 250]
    df = df[df.superblock.notna()]
    return df


def main():
    df = clean_data(
        load_shapefile('../data/EIX_superblock_buildings_energy/EIX_superblock_buildings_energy_consumption_4326.shp'))
    drawer_map = DrawerMap(full_df=df,
                           color_col="build_date",
                           xlim=(2.13, 2.20),
                           ylim=(41.313, 41.47))
    drawer_chart = DrawerChart(full_df=df,
                                    xcol="build_date",
                                    ycol="E_final",
                                    xlabel="Build year",
                                    ylabel="Energy (kWh/year)",
                                    dot_size=0.5, line_size=1)

    drawer = Drawer(full_df=df,
                    drawers=[drawer_map, drawer_chart],
                    time_col='superblock',
                    # dpi = 600,
                    dpi=72,
                    save_dir_path='../out/buildyear_energy/')

    drawer.draw_anime(save_anim_imgs=True, show=False)
    # drawer.draw_static()


if __name__ == '__main__':
    main()
