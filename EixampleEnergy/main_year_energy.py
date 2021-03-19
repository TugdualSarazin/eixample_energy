from EixampleEnergy.config import Config
from EixampleEnergy.drawers.drawer import Drawer


class BuildYearEnergy(Config):
    shape_file_path = '../data/EIX_superblock_buildings_energy/EIX_superblock_buildings_energy_consumption_4326.shp'

    # Overwrite clean_data
    def clean_data(self):
        self.df = self.df[self.df['build_date'] > 1900]
        self.df = self.df[self.df['E_final'] < 250]
        self.df = self.df[self.df.superblock.notna()]

    # Drawer overwrite config
    chart_xcol = "build_date"
    chart_ycol = "E_final"
    map_color_col = "build_date"
    time_col = 'superblock'
    x_label = "Build year"
    y_label = "Energy (kWh/m2/year)"
    map_xlim = (2.13, 2.20)
    map_ylim = (41.373, 41.413)
    chart_dot_size = 1
    chart_line_size = 0
    # dpi = 600
    dpi = 72
    save_dir_path = '../out/buildyear_energy/'


def main():
    drawer = Drawer(BuildYearEnergy(), show=True, has_map=True, has_chart=True)
    #drawer.draw_anime(save_anim_imgs=True)
    drawer.draw_static()


if __name__ == '__main__':
    main()
