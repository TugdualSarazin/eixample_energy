import geopandas

from matplotlib import cm

from EixampleEnergy.config import Config
from EixampleEnergy.drawers.drawer import Drawer

# calcularion of certificate ranges
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


class BuildingCert(Config):
    shape_file_path = '../data/Buildings_SJ/BCN_Avg_Energy_4326.shp'

    # Overwrite clean_data
    def clean_data(self):
        self.df = self.df[self.df['build_date'] > 1900]
        self.df["gr_by_age"] = self.df['build_date'].apply(build_date_group)
        self.df["en_cert"] = self.df['RES_energy'].apply(energy_certificate)

    # Drawer overwrite config
    chart_xcol = "build_date"
    chart_ycol = "en_cert"
    map_color_col = "en_cert"
    time_col = "en_cert"
    x_label = "Build year"
    y_label = "Energy Certificate"
    map_xlim = (2.05, 2.23)
    map_ylim = (41.313, 41.47)
    chart_dot_size = 0.5
    chart_line_size = 1
    # dpi = 600
    dpi = 72
    save_dir_path = '../out/building_cert/'


def main():
    drawer = Drawer(BuildingCert(), show=True, has_map=True, has_chart=True)
    drawer.draw_anime(save_anim_imgs=True)
    # drawer.draw_static()


if __name__ == '__main__':
    main()
