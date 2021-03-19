import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pathlib import Path

from EixampleEnergy.config import Config
from EixampleEnergy.drawers.drawer_chart import DrawerChart
from EixampleEnergy.drawers.drawer_map import DrawerMap


class Drawer:
    def __init__(self, config: Config, show=True, has_map=True, has_chart=True):
        self.config = config
        self.is_show = show

        self.time_ids = self.config.df[[self.config.time_col]].squeeze().unique()
        self.time_ids.sort()

        # Has map / has map
        self.has_map = has_map
        self.has_chart = has_chart

        # Config fig
        if self.has_chart and self.has_map:
            self.fig, (ax_map, ax_chart) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [4, 1]},
                                                        dpi=self.config.dpi)
            self.drawer_map = DrawerMap(self.config, ax_map)
            self.drawer_chart = DrawerChart(self.config, ax_chart)

        elif self.has_map:
            self.fig, (ax_map) = plt.subplots(1, 1, dpi=self.config.dpi)
            self.drawer_map = DrawerMap(self.config, ax_map)

        elif self.has_chart:
            self.fig, (ax_chart) = plt.subplots(1, 1, dpi=self.config.dpi)
            self.drawer_chart = DrawerChart(self.config, ax_chart)

        # Create output folder
        if config.save_dir_path:
            Drawer.create_dir(config.save_dir_path)

    @staticmethod
    def create_dir(path):
        Path(path).mkdir(parents=True, exist_ok=True)

    # TODO: unit test
    def filter_df(self, num=None):
        if num is None:
            df = self.config.df
        else:
            df = self.config.df[self.config.df[self.config.time_col].isin(self.time_ids[:num])]
            print(f"{num}/{len(self.time_ids)}")
        return df

    def draw(self, num, save_base_path=None):
        df = self.filter_df(num)

        if self.has_map:
            self.drawer_map.draw_map(df)
        if self.has_chart:
            self.drawer_chart.draw(df)

        if save_base_path is not None:
            if num is None:
                path = f'{save_base_path}.png'
            else:
                path = f'{save_base_path}-{num}.png'
            plt.savefig(path, transparent=True)

    def show(self):
        if self.is_show:
            plt.show()

    def draw_anime(self, save_anim_imgs=False):
        #
        # Config save paths
        save_anim_path = None
        save_anim_imgs_base_path = None
        if self.config.save_dir_path:
            save_anim_path = self.config.save_dir_path + '/anim.gif'
            if save_anim_imgs:
                save_anim_imgs_base_path = self.config.save_dir_path + '/anim'

        # Do animation
        ani = FuncAnimation(self.fig, self.draw, frames=len(self.time_ids) + 1, interval=400, repeat=False,
                            fargs=[save_anim_imgs_base_path])
        if save_anim_path:
            ani.save(save_anim_path, writer='imagemagick')

        self.show()

    def draw_static(self):
        save_base_path = None
        if self.config.save_dir_path:
            save_base_path = self.config.save_dir_path + '/static'
        self.draw(num=None, save_base_path=save_base_path)

        self.show()
