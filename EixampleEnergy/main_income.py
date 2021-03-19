import pandas as pd

from EixampleEnergy.drawers.drawer import Drawer
from EixampleEnergy.config import Config


class IncomeAge(Config):
    shape_file_path = '../data/Income/BCN_City_Income.shp'

    # Overwrite clean_data
    def clean_data(self):
        frames = 20
        self.df["Avg_in_hou"] = self.df['Avg_in_hou'].apply(lambda str_avg: float(str_avg.replace(',', '.')))
        self.df["Avg_age"] = self.df['Avg_age'].apply(lambda str_avg: float(str_avg.replace(',', '.')))
        self.df['quantile_time'] = pd.qcut(self.df['Avg_in_hou'], frames, labels=False)

    # Drawer overwrite config
    chart_xcol = "Avg_in_hou"
    chart_ycol = "Avg_age"
    map_color_col = "Avg_in_hou"
    time_col = 'quantile_time'
    x_label = "Avg_in_hou"  # "Energy (kWh/year)"
    y_label = "Building age"
    map_xlim = (2.02, 2.26)
    map_ylim = (41.313, 41.47)
    chart_dot_size = 1
    chart_line_size = 0
    # dpi = 600
    dpi = 72
    save_dir_path = '../out/income/'


def main():
    drawer = Drawer(IncomeAge(), show=True, has_map=True, has_chart=True)
    # drawer.draw_anime(save_anim_imgs=True)
    drawer.draw_static()


if __name__ == '__main__':
    main()
