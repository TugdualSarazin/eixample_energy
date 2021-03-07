import os

import contextily as cx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class Drawer:
    background_img = "../out/background.tif"
    chart_dot_size = 3
    chart_line_width = 1

    def __init__(self, df,
                 chartx, charty,
                 x_label=None, y_label=None,
                 map_xlim=None, map_ylim=None,
                 update_background=False,
                 dpi=72):
        self.df = df

        self.x_label = x_label
        self.y_label = y_label

        self.chartx = chartx
        self.charty = charty

        # Config chart
        self.chart_xlim = (df[self.chartx].min(), df[self.chartx].max())
        self.chart_ylim = (df[self.charty].min(), df[self.charty].max())
        self.meany = self.df.groupby(self.chartx)[self.charty].mean()

        # Config map
        self.update_background = update_background
        if map_xlim:
            self.map_xlim = map_xlim
        else:
            self.map_xlim = ([df.total_bounds[0], df.total_bounds[2]])

        if map_ylim:
            self.map_ylim = map_ylim
        else:
            self.map_ylim = ([df.total_bounds[1], df.total_bounds[3]])
        self.download_map_bg()

        # Config fig
        self.fig, (self.ax_map, self.ax_chart) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, dpi=dpi)
        plt.subplots_adjust(right=0.80)

    def draw_chart(self, df):
        self.ax_chart.clear()
        self.ax_chart.set_xlim(self.chart_xlim)
        self.ax_chart.set_ylim(self.chart_ylim)
        sc = self.ax_chart.scatter(x=self.chartx, y=self.charty, data=df, s=self.chart_dot_size)
        line = self.ax_chart.plot(self.meany, color='r', linewidth=self.chart_line_width)
        #self.ax_chart.legend((sc, line), ('Mean', 'Building'), bbox_to_anchor=(1, 1), borderaxespad=0, frameon=False)
        self.ax_chart.legend([sc, line[0]], ['Buildings', 'Eixample\nmean'], bbox_to_anchor=(1, 1))
        #self.ax.legend(bbox_to_anchor=(1, 1), borderaxespad=0, frameon=False)

        if self.x_label:
            plt.xlabel(self.x_label)
        if self.y_label:
            plt.ylabel(self.y_label)

    def download_map_bg(self):
        if not os.path.isfile(self.background_img) or self.update_background:
            print(f"Background image file ({self.background_img}) doesn't exists download it")
            cx.bounds2raster(
                self.map_xlim[0], self.map_ylim[0], self.map_xlim[1], self.map_ylim[1],
                self.background_img,
                ll=True,
                # source=cx.providers.Wikimedia
                #source=cx.providers.CartoDB.Positron
                #source=cx.providers.Stamen.TerrainBackground
                #source='https://a.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png'
                source='http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}'
            )
        else:
            print(f"Background image file ({self.background_img}) already exists")

    def draw_map(self, df):
        self.ax_map.clear()

        self.ax_map.set_xlim(self.map_xlim)
        self.ax_map.set_ylim(self.map_ylim)
        # df.plot(ax=self.ax_map, column=self.chartx)
        df.plot(ax=self.ax_map)
        cx.add_basemap(self.ax_map, crs=self.df.crs.to_string(), source=self.background_img)
        self.ax_map.set_axis_off()

    def animate(self, num, sb_ids):
        id = sb_ids[num]
        sb_df = self.df[self.df['superblock'] == id]
        print(f"{num}/{len(sb_ids)}")

        self.draw_map(sb_df)
        self.draw_chart(sb_df)

    def draw_anime(self, save_file=None):
        sb_ids = self.df[['superblock']].squeeze().unique()

        ani = FuncAnimation(self.fig, self.animate, frames=len(sb_ids), interval=400, repeat=True,
                            fargs=[sb_ids])
        if save_file:
            ani.save(save_file, writer='imagemagick')

        #plt.show()

    def draw_static(self, save_file=None):
        self.draw_map(self.df)
        self.draw_chart(self.df)

        if save_file:
            plt.savefig(save_file)

        plt.show()
