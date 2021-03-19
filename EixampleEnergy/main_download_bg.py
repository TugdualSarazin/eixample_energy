
import contextily as cx
import matplotlib.pyplot as plt
import rasterio
from rasterio import rio

from EixampleEnergy.main_buildingAge import BuildingAge


def download_map_bg(self):
    if self.config.background_img_path is None:
        raise Exception("Variable Drawer.background_img_path is not defined")

    print(f"Downloading map's background image to {self.config.background_img_path}")
    img, ext = cx.bounds2raster(
        self.config.map_xlim[0], self.config.map_ylim[0], self.config.map_xlim[1], self.config.map_ylim[1],
        self.config.background_img_path,
        ll=True,
        # source=cx.providers.CartoDB.Positron,
        # source='https://a.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png'
        source='http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}'
    )

    def rgb2gray(rgb):
        r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray

    plt.close()
    plt.imshow(rgb2gray(img), extent=ext, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
    plt.show()
    exit()


def main():
    map = BuildingAge()

if __name__ == '__main__':
    main()