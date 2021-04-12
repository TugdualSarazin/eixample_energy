import geopandas


def load_shapefile(shape_file_path, rows=None):
    return geopandas.read_file(shape_file_path, rows=rows)
