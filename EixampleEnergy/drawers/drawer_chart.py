from EixampleEnergy.drawers.drawer_elem import DrawerElem


class DrawerChart(DrawerElem):
    def __init__(self, full_df,
                 xcol, ycol,
                 xlabel=None, ylabel=None,
                 dot_size=1, line_size=1):
        # Init attributes
        self.full_df = full_df
        self.xcol = xcol
        self.ycol = ycol
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.dot_size = dot_size
        self.line_size = line_size

        # Min/max mean
        self.minx = self.full_df[self.xcol].min()
        self.maxx = self.full_df[self.xcol].max()
        self.miny = self.full_df[self.ycol].min()
        self.maxy = self.full_df[self.ycol].max()
        self.meany = self.full_df.groupby(self.xcol)[self.ycol].mean()

        # Chart lim
        self.xlim = (self.minx, self.maxx)
        self.ylim = (self.miny, self.maxy)

    def draw(self, df):
        self.ax.clear()
        self.ax.patch.set_alpha(0)
        self.ax.set_xlim(self.xlim)
        self.ax.set_ylim(self.ylim)
        sc = self.ax.scatter(x=self.xcol, y=self.ycol, data=df, color='c',
                             s=self.dot_size)
        line = self.ax.plot(self.meany, color='white', linewidth=self.line_size)
        # self.ax.legend((sc, line), ('Mean', 'Building'), bbox_to_anchor=(1, 1), borderaxespad=0, frameon=False)
        # self.ax.legend([sc, line[0]], ['Buildings', 'Eixample\nmean'], bbox_to_anchor=(1, 1))

        # self.ax.spines["bottom"].set_color('white')
        # self.ax.spines["left"].set_color('white')
        # self.ax.tick_params(colors='white')
        # if self.map.x_label:
        #     plt.xlabel(self.map.x_label, color='white')
        # if self.map.y_label:
        #     plt.ylabel(self.map.y_label, color='white')

        # self.ax_chart.set_position([0.75, 0.12, 0.20, 0.15])
