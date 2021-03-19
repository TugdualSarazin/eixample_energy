import geopandas

class Config:
    df = None

    # Shapefile config
    shape_file_path = None

    # Time config
    time_col = None

    # Drawer data config
    chart_xcol = None
    chart_ycol = None
    x_label = None
    y_label = None
    chart_dot_size = 1
    chart_line_size = 1

    # Chart config
    map_xlim = None
    map_ylim = None
    map_color_col = None
    map_cmap = 'YlGnBu'
    background_img_path = None

    # Fig config
    dpi = 72
    save_dir_path = None

    def __init__(self):
        # Load data
        self.df = self.load_shapefile()
        # Clean data
        self.clean_data()

        if self.map_xlim is None:
            self.map_xlim = ([self.df.total_bounds[0], self.df.total_bounds[2]])

        if self.map_ylim is None:
            self.map_ylim = ([self.df.total_bounds[1], self.df.total_bounds[3]])


    def load_shapefile(self):
        return geopandas.read_file(self.shape_file_path)

    def clean_data(self):
        pass