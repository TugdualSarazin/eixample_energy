import matplotlib.pyplot as plt


class DrawerChart:
    def __init__(self, map, ax):
        self.map = map
        self.ax = ax

        # Min/max mean
        self.chart_minx = self.map.df[self.map.chart_xcol].min()
        self.chart_maxx = self.map.df[self.map.chart_xcol].max()
        self.chart_miny = self.map.df[self.map.chart_ycol].min()
        self.chart_maxy = self.map.df[self.map.chart_ycol].max()
        self.meany = self.map.df.groupby(self.map.chart_xcol)[self.map.chart_ycol].mean()

        # Chart lim
        self.chart_xlim = (self.chart_minx, self.chart_maxx)
        self.chart_ylim = (self.chart_miny, self.chart_maxy)

    def draw(self, df):
        self.ax.clear()
        self.ax.patch.set_alpha(1)
        self.ax.set_xlim(self.chart_xlim)
        self.ax.set_ylim(self.chart_ylim)
        sc = self.ax.scatter(x=self.map.chart_xcol, y=self.map.chart_ycol, data=df, color='c',
                             s=self.map.chart_dot_size)
        line = self.ax.plot(self.meany, color='white', linewidth=self.map.chart_line_size)
        # self.ax.legend((sc, line), ('Mean', 'Building'), bbox_to_anchor=(1, 1), borderaxespad=0, frameon=False)
        # self.ax.legend([sc, line[0]], ['Buildings', 'Eixample\nmean'], bbox_to_anchor=(1, 1))

        self.ax.spines["bottom"].set_color('white')
        self.ax.spines["left"].set_color('white')
        self.ax.tick_params(colors='white')
        if self.map.x_label:
            plt.xlabel(self.map.x_label, color='white')
        if self.map.y_label:
            plt.ylabel(self.map.y_label, color='white')

        # self.ax_chart.set_position([0.75, 0.12, 0.20, 0.15])
