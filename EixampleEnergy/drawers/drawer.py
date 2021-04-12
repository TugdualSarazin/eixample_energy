import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pathlib import Path


class Drawer:
    def __init__(self,
                 full_df,
                 drawers,
                 time_col,
                 is_time_cumulative=True,
                 dpi=72,
                 save_dir_path=None):
        # Init attributes
        self.full_df = full_df
        self.drawers = drawers
        self.time_col = time_col
        self.is_time_cumulative = is_time_cumulative
        self.dpi = dpi
        self.save_dir_path = save_dir_path

        self.time_ids = self.full_df[[self.time_col]].squeeze().unique()
        self.time_ids.sort()

        # Init fig and drawers' ax
        self.fig, axs = plt.subplots(len(self.drawers), 1, dpi=self.dpi, squeeze=False)
        for drw, ax in zip(self.drawers, axs):
            drw.init_ax(ax[0])

        # Create output folder
        if self.save_dir_path:
            Drawer.create_dir(self.save_dir_path)

    @staticmethod
    def create_dir(path):
        Path(path).mkdir(parents=True, exist_ok=True)

    # TODO: unit test
    def filter_df(self, num=None):
        # Static mode (num=None)
        if num is None:
            df = self.full_df
        # Anime mode (num>=0)
        else:
            if self.is_time_cumulative:
                time_values = self.time_ids[:num]
            else:
                time_values = [self.time_ids[num]]
            df = self.full_df[self.full_df[self.time_col].isin(time_values)]
            print(f"{num}/{len(self.time_ids)}")
        return df

    def draw(self, num, save_base_path=None):
        df = self.filter_df(num)

        # Draw all drawers
        for drawer in self.drawers:
            drawer.draw(df)

        # Save to file
        if save_base_path is not None:
            if num is None:
                path = f'{save_base_path}.png'
            else:
                # TODO: update this to param
                id = self.time_ids[num]
                path = f'{save_base_path}-{id}.png'
                #path = f'{save_base_path}-{num}.png'
            plt.savefig(path, transparent=True)

    def draw_anime(self, save_anim_imgs=False, show=True):
        # Config save paths
        save_anim_path = None
        save_anim_imgs_base_path = None
        if self.save_dir_path:
            save_anim_path = self.save_dir_path + '/anim.gif'
            if save_anim_imgs:
                save_anim_imgs_base_path = self.save_dir_path + '/anim'

        # Do animation / draw
        frames = len(self.time_ids)
        if self.is_time_cumulative:
            frames += 1
        ani = FuncAnimation(self.fig, self.draw, frames=frames, interval=400, repeat=False,
                            fargs=[save_anim_imgs_base_path])
        if save_anim_path:
            ani.save(save_anim_path, writer='imagemagick')

        # Show
        if show:
            plt.show()

    def draw_static(self, show=True):
        # Config save paths
        save_base_path = None
        if self.save_dir_path:
            save_base_path = self.save_dir_path + '/static'
        # Draw
        self.draw(num=None, save_base_path=save_base_path)

        # Show
        if show:
            plt.show()
