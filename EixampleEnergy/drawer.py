import os

import contextily as cx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Drawer:
    #background_img = "../out/background_leyla.tif"
    # chart_dot_size = 3
    chart_line_width = 1

    def __init__(self, df,
                 data_x, data_y, data_time,
                 x_label=None, y_label=None,
                 map_xlim=None, map_ylim=None,
                 background_img_path=None,
                 has_chart=True,
                 map_cmap='YlGnBu', chart_dot_size=1,
                 dpi=72):
        self.map_cmap = map_cmap
        self.df = df

        self.x_label = x_label
        self.y_label = y_label

        self.data_x = data_x
        self.data_y = data_y
        self.data_time = data_time

        # Config chart
        self.chart_dot_size = chart_dot_size
        self.has_chart = has_chart
        if self.has_chart:
            self.chart_xlim = (df[self.data_x].min(), df[self.data_x].max())
            self.chart_ylim = (df[self.data_y].min(), df[self.data_y].max())
            self.meany = self.df.groupby(self.data_x)[self.data_y].mean()

        # Config map
        self.background_img_path = background_img_path
        if map_xlim:
            self.map_xlim = map_xlim
        else:
            self.map_xlim = ([df.total_bounds[0], df.total_bounds[2]])

        if map_ylim:
            self.map_ylim = map_ylim
        else:
            self.map_ylim = ([df.total_bounds[1], df.total_bounds[3]])


        # Config fig
        if self.has_chart:
            self.fig, (self.ax_map, self.ax_chart) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [4, 1]}, dpi=dpi)
        else:
            self.fig, (self.ax_map) = plt.subplots(1, 1, dpi=dpi)
        plt.subplots_adjust(right=0.80)

    def draw_chart(self, df):
        self.ax_chart.clear()
        self.ax_chart.set_xlim(self.chart_xlim)
        self.ax_chart.set_ylim(self.chart_ylim)
        sc = self.ax_chart.scatter(x=self.data_x, y=self.data_y, data=df, color='c', s=self.chart_dot_size)
        line = self.ax_chart.plot(self.meany, color='r', linewidth=self.chart_line_width)
        #self.ax_chart.legend((sc, line), ('Mean', 'Building'), bbox_to_anchor=(1, 1), borderaxespad=0, frameon=False)
        self.ax_chart.legend([sc, line[0]], ['Buildings', 'Eixample\nmean'], bbox_to_anchor=(1, 1))
        #self.ax.legend(bbox_to_anchor=(1, 1), borderaxespad=0, frameon=False)

        if self.x_label:
            plt.xlabel(self.x_label)
        if self.y_label:
            plt.ylabel(self.y_label)

    def download_map_bg(self):
        if self.background_img_path is None:
            raise Exception("Variable Drawer.background_img_path is not defined")

        print(f"Downloading map's background image to {self.background_img_path}")
        cx.bounds2raster(
            self.map_xlim[0], self.map_ylim[0], self.map_xlim[1], self.map_ylim[1],
            self.background_img_path,
            ll=True,
            #source=cx.providers.CartoDB.Positron
            #source='https://a.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png'
            source='http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}'
        )

    def draw_map(self, df):
        self.ax_map.clear()

        self.ax_map.set_xlim(self.map_xlim)
        self.ax_map.set_ylim(self.map_ylim)
        #df.plot(ax=self.ax_map, column=self.data_x, legend=True, cmap='YlGnBu')
        # df.plot(ax=self.ax_map, column=self.data_x, cmap='YlGnBu')
        df.plot(ax=self.ax_map, column=self.data_x, cmap=self.map_cmap)
        # TODO
        #cx.add_basemap(self.ax_map, crs=self.df.crs.to_string(), source=self.background_img)
        self.ax_map.set_axis_off()

    def animate(self, num, sb_ids):
        #sb_df = self.df[self.df[self.data_time] == sb_ids[num]]
        sb_df = self.df[self.df[self.data_time].isin(sb_ids[:num])]
        print(f"{num}/{len(sb_ids)}")

        self.draw_map(sb_df)
        if self.has_chart:
            self.draw_chart(sb_df)

    def draw_anime(self, save_file=None):
        sb_ids = self.df[[self.data_time]].squeeze().unique()

        ani = FuncAnimation(self.fig, self.animate, frames=len(sb_ids)+1, interval=400, repeat=True, fargs=[sb_ids])
        if save_file:
            ani.save(save_file, writer='imagemagick')

        plt.show()

    def draw_static(self, save_file=None):
        self.draw_map(self.df)
        if self.has_chart:
            self.draw_chart(self.df)

        if save_file:
            plt.savefig(save_file, transparent=True)

        plt.show()
