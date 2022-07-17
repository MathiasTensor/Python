from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import re

#################################################################################
q1 = input("Do you wish to get coord. of pic? (y/n)  ")
q2 = input("Enter path: (e.g.: D:\Testna_mapa\slika3.jpg)  ")
q3 = int(input("Choose cropping in x direction: (num pixels)  "))
q4 = int(input("Choose cropping in y direction: (num pixels)  "))
q5 = int(input("Choose grid finesse: (num from 1 to 4)  "))
q6 = int(input("Choose your tolerance: "))
##################################################################################
# Auxillary info:
#black bg (after filter) = 0
black = 0
#white bg (after  filter) = 255
white = 255
#black bg (after filter) = 0
black = 0
#white bg (after  filter) = 255
white = 255

def get_data(string, edge_crop_x, edge_crop_y):
    ###############################################################################
    """Image processing part. We first greyscale the picture
    and find the edges via the Laplacian in-built kernel
    Opening path to pic:im = Image.open("D:\*...\*.jpg")
    Conversion: *.convert("L")
    Edge find: *.filter(ImageFilter.FIND_EDGES)"""
    global im
    global width
    global height
    global pixel_value
    im = Image.open(string)
    (width, height) = im.size
    im = im.convert("L")
    im = im.filter(ImageFilter.FIND_EDGES)
    #im.show()
    pixel_value = list(im.getdata())
    if im.mode == "RGB":
        channels = 3
    if im.mode == "L":
        channels = 1
    else:
        print("Unsuitable image mode (not RGB or L)")
    pixel_value = np.array(pixel_value).reshape(width, height)
    # Crop the edges wrt. edge_crop (in any case there is a bit of edge cropping)
    pixel_value = np.delete(pixel_value, list(range(0, edge_crop_x)), axis=1)
    pixel_value = np.delete(pixel_value, list(range(pixel_value.shape[1] - edge_crop_x, pixel_value.shape[1])), axis=1)
    pixel_value = np.delete(pixel_value, list(range(0, edge_crop_y)), axis=0)
    pixel_value = np.delete(pixel_value, list(range(pixel_value.shape[0] - edge_crop_y, pixel_value.shape[0])), axis=0)
    im.show()
    return pixel_value, pixel_value.shape
    ###############################################################################

def width_height_tuple(data):
    """Tuple for interval_of_lenght_with_tolerance_diffpixel
    from get_data function"""
    ###############################################################################
    start = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            start.append((i, j))
    return start
    ###############################################################################

def interval_of_tolerance_diffpixel(x, tol):
    ###############################################################################
    """Here we define the tolerance of choosing
    which pixels to eliminate from the final
    graph"""
    if x - tol <= x <= x + tol:
        return list(range(x - tol, x + tol))
    ###############################################################################
# TO here OK
def coord_in_lenght_and_tolerance(data, length, tol, color):
    # start of helper function definitons:
    ###############################################################################
    """This function generates new coarse grid points for final set
    of coordinates s.t. the graph makes sense"""

    def data_line(data, i, j, length):
        """Helper function that shortens notation of 1D
        subarray in pixel_value"""
        return data[np.ix_([i], [int(k) for k in range(j, j + length)])]

    def data_line_index(data, i, j, length):
        """Helper function that shortens notation of 1D
         subarray (data_line) in pixel_value and returns
        index value"""
        new_list = []
        for l in range(0, length):
            if j + length < pixel_value.shape[1]:
                new_list.append(data[np.ix_([i], [int(k) for k in range(j, j + length)])][0, l])
                continue
        return new_list
    # end of function definitions:
    ###############################################################################
    list = []
    # Creating boundaries for summation in pixel_value
    for (i, j) in width_height_tuple(data):

    # Creating a restriction on possible data[i, j] values
        if data[i, j] in interval_of_tolerance_diffpixel(color, tol):

    # Creating a subarray with the desired length and checking if each
    #element is in tolerance. If it is, append it to list
            tally = 0
            for x in data_line_index(pixel_value, i, j, length):
                if x in interval_of_tolerance_diffpixel(color, tol):
                    tally = tally + 1
                    continue
                else:
                    break
            if tally == length:
                if (i, j) not in list:
                    list.append((i, j))
                else:
                    break
    return(list)
    ###############################################################################
# from here ok
def graphing_function(type, list):
    #############################################################################
    """Graphing the resulting function in a figure of the original size
    type: "ro", "b-", ..."""
    plt.figure(figsize=(10, 6))
    plt.title("Points of picture")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.grid(visible=True)
    plt.legend(["Imported graph"])
    list_x = []
    list_y = []
    for u in list:
        list_x.append(u[0])
    for z in list:
        list_y.append(z[1])
    plt.plot(list_x, list_y, type)
    plt.show()
    ###############################################################################
# ending

def data_line_index(data, i, j, length):
    """Helper function that shortens notation of 1D
    subarray (data_line) in pixel_value and returns
    index value"""
    new_list = []
    for l in range(0, length):
        if j + length < pixel_value.shape[1]:
            new_list.append(data[np.ix_([i], [int(k) for k in range(j, j + length)])][0, l])
            continue
    return new_list

####################################################################################
# Actual program
if q1 == "y":
    get_data(q2, q3, q4)
    print("\nBelow is the L grid: ")
    print(get_data(q2, q3, q4))
    print("\nBelow are the points that satisfy your criteria: ")
    print(print(coord_in_lenght_and_tolerance(pixel_value, q5, q6, 255)))
    graphing_function("ro", coord_in_lenght_and_tolerance(pixel_value, q5, q6, 255))
else:
    print("Close the program.")

#######################################################################################
