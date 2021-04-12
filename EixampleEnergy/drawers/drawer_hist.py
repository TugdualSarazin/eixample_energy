
import matplotlib.pyplot as plt
import scipy.stats as stats

from EixampleEnergy.drawers.drawer_elem import DrawerElem


class DrawerHist(DrawerElem):
    def __init__(self, full_df,
                 xcol,
                 nb_bins=50,
                 xlabel=None, ylabel=None,
                 cmap=plt.cm.RdYlGn.reversed()):
        # Init attributes
        self.full_df = full_df
        self.xcol = xcol
        self.nb_bins = nb_bins
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.cmap = cmap


    def draw(self, df):
        self.ax.clear()
        self.ax.patch.set_alpha(0)

        # Plot full_df line
        # TODO: remove ax.hist the only used is the plot
        _, bins, _ = self.ax.hist(self.full_df[self.xcol], self.nb_bins, density=True, alpha=0.)
        density = stats.gaussian_kde(self.full_df[self.xcol])
        self.ax.plot(bins, density(bins), color='white', linewidth=2)

        # Df histogram
        _, _, patches = self.ax.hist(df[self.xcol], bins=bins, density=True)

        # TODO: Specific colors for the use case. Need to be move to cmap param.
        for bin, patch in zip(bins, patches):
            if bin <= 5063:
                color = '#2E81B8'
            elif bin <= 5885:
                color = '#65AAAF'
            elif bin <= 6353:
                color = '#A0D2A4'
            elif bin <= 6721:
                color = '#C8E7AD'
            elif bin <= 7141:
                color = '#EEF6B9'
            elif bin <= 7586:
                color = '#FFEDAB'
            elif bin <= 8230:
                color = '#FFC882'
            elif bin <= 9210:
                color = '#F79F55'
            elif bin <= 11020:
                color = '#ED593F'
            else:
                color = '#D71919'
            plt.setp(patch, 'facecolor', color)

        # self.ax.legend((sc, line), ('Mean', 'Building'), bbox_to_anchor=(1, 1), borderaxespad=0, frameon=False)
        # self.ax.legend([sc, line[0]], ['Buildings', 'Eixample\nmean'], bbox_to_anchor=(1, 1))

        self.ax.tick_params(colors='white')
        self.ax.set_yticks([])
        if self.xlabel:
            plt.xlabel(self.xlabel, color='white')
        if self.ylabel:
            plt.ylabel(self.ylabel, color='white')

        # Linewidth
        # TODO: move to params
        #self.ax.rcParams['axes.linewidth'] = 0.1
        [i.set_linewidth(0.2) for i in self.ax.spines.values()]
        # self.ax.set_position([0.75, 0.12, 0.20, 0.15])
