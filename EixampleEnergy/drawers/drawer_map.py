import contextily as cx
import matplotlib.pyplot as plt

class DrawerMap:
    def __init__(self, config, ax):
        self.config = config
        self.ax = ax

        # Min / max
        self.map_vmin = self.config.df[self.config.map_color_col].min()
        self.map_vmax = self.config.df[self.config.map_color_col].max()

    def draw_map(self, df):
        self.ax.clear()
        self.ax.set_xlim(self.config.map_xlim)
        self.ax.set_ylim(self.config.map_ylim)
        df.plot(ax=self.ax, column=self.config.map_color_col, cmap=self.config.map_cmap,
                vmin=self.map_vmin, vmax=self.map_vmax)
        if self.config.background_img_path:
            cx.add_basemap(self.ax, crs=self.config.df.crs.to_string(), source=self.config.background_img_path,
                           cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
        self.ax.set_axis_off()
        self.ax.set_position([0., 0., 1., 1.])