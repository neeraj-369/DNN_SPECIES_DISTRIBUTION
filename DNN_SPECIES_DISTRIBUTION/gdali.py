import tifffile

def Open(tif_file):
    # Read the GeoTIFF file using tifffile
    print("testing")
    print(tif_file)
    print("asdfadsf")
    with tifffile.TiffFile(tif_file) as tif:
        # Extract the geotransform information
        print(tif_file)
        geotransform = tif.pages[0].geotiff_tags.get('ModelTransformationTag')
        if geotransform is None:
            return(0, 0, 0, 0, 0, 0)
        # Extract the pixel size and rotation information
        x_size = geotransform[0]
        x_rotation = geotransform[1]
        y_rotation = geotransform[2]
        y_size = geotransform[5]
        # Extract the upper-left coordinates
        upper_left_x = geotransform[3]
        upper_left_y = geotransform[4]
    # Return the geotransform information as a tuple
    return (upper_left_x, x_size, x_rotation, upper_left_y, y_rotation, y_size)