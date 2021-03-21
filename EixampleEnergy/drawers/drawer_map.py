import contextily as cx
import matplotlib.pyplot as plt

from EixampleEnergy.drawers.drawer_elem import DrawerElem


class DrawerMap(DrawerElem):
    def __init__(self, full_df,
                 color_col,
                 cmap='YlGnBu',
                 xlim=None, ylim=None, bg_img=None):
        # Init attributes
        self.full_df = full_df
        self.color_col = color_col
        self.cmap = cmap
        self.bg_img = bg_img

        if xlim is None:
            self.xlim = ([self.full_df.total_bounds[0], self.full_df.total_bounds[2]])
        else:
            self.xlim = xlim

        if ylim is None:
            self.ylim = ([self.full_df.total_bounds[1], self.full_df.total_bounds[3]])
        else:
            self.ylim = ylim

        # Min / max
        self.vmin = self.full_df[self.color_col].min()
        self.vmax = self.full_df[self.color_col].max()

    def draw(self, df):
        self.ax.clear()
        self.ax.set_xlim(self.xlim)
        self.ax.set_ylim(self.ylim)
        df.plot(ax=self.ax, column=self.color_col, cmap=self.cmap,
                vmin=self.vmin, vmax=self.vmax)
        if self.bg_img:
            cx.add_basemap(self.ax, crs=self.full_df.crs.to_string(), source=self.bg_img,
                           cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
        self.ax.set_axis_off()
        self.ax.set_position([0., 0., 1., 1.])