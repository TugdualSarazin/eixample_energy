import matplotlib.pyplot as plt

from EixampleEnergy.drawers.drawer_elem import DrawerElem


class DrawerStackedBar(DrawerElem):
    def __init__(self, full_df,
                 xcol, group_col,
                 xlabel=None, ylabel=None,
                 cmap=plt.cm.RdYlGn.reversed()):
        # Init attributes
        self.full_df = full_df
        self.xcol = xcol
        self.group_col = group_col
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.cmap = cmap

        # Min/max
        self.minx = self.full_df[self.xcol].min()
        self.maxx = self.full_df[self.xcol].max()
        self.xlim = (self.minx, self.maxx)
        self.miny = 0
        self.maxy = self.full_df.groupby([self.xcol])[self.xcol].count().max()
        self.ylim = (self.miny, self.maxy)

    def draw(self, df):
        self.ax.clear()
        self.ax.patch.set_alpha(0)
        self.ax.set_xlim(self.xlim)
        self.ax.set_ylim(self.ylim)

        df_group = df.groupby([self.xcol, self.group_col])[self.xcol].count().unstack(self.group_col).fillna(0)
        if df_group.size > 0:
            df_group.plot(ax=self.ax, kind='bar', stacked=True, cmap=self.cmap, legend=None)
