from EixampleEnergy.drawers.drawer import Drawer

from EixampleEnergy.config import Config


def build_date_group(build_date):
    if build_date < 1979:
        return "group_01"
    elif build_date >= 1979 and build_date < 1986:
        return "group_02"
    elif build_date >= 1986 and build_date < 2005:
        return "group_03"
    else:
        return "group_04"


class BuildingAge(Config):
    shape_file_path = '../data/Buildings_SJ/BCN_Avg_Energy_4326.shp'

    # Overwrite clean_data
    def clean_data(self):
        self.df = self.df[self.df['build_date'] > 1900]
        self.df["gr_by_age"] = self.df['build_date'].apply(build_date_group)
        self.df = self.df.sort_values(by=["gr_by_age"])

    # Drawer overwrite config
    chart_xcol = "build_date"
    chart_ycol = "RES_energy"
    map_color_col = "RES_energy"
    time_col = 'gr_by_age'
    x_label = "Build year"
    y_label = "Energy (kWh/year)"
    map_xlim = (2.05, 2.23)
    map_ylim = (41.313, 41.47)
    chart_dot_size = 0.5
    chart_line_size = 1
    # dpi = 600
    dpi = 72
    save_dir_path = '../out/building_age/'


def main():
    drawer = Drawer(BuildingAge(), show=True, has_map=True, has_chart=True)
    drawer.draw_anime(save_anim_imgs=True)
    # drawer.draw_static()


if __name__ == '__main__':
    main()
