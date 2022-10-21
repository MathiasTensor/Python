from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import re

#Given an array, construct a subarray satisfying number of tolerance conditions for
#set of elements in subarray. Return pos. of subarray in array for further use in image/L
#detection. Works only well with infividuals pixels and very small images

# Auxillary info:
#black bg (after filter) = 0
black = 0
#white bg (after  filter) = 255
white = 255
#black bg (after filter) = 0
black = 0
#white bg (after  filter) = 255
white = 255
##################################################################################

def get_data(string, edge_crop_x, edge_crop_y):
    ###############################################################################
    """Image processing part. We first greyscale the picture
    and find the edges via the Laplacian in-built kernel
    Opening path to pic:im = Image.open("D:\*...\*.jpg")
    Conversion: *.convert("L")
    Edge find: *.filter(ImageFilter.FIND_EDGES)"""
    global im
    global pixel_value
    im = Image.open(string)
    (width, height) = im.size
    im = im.convert("L")
    #im = im.filter(ImageFilter.FIND_EDGES)
    #im.show()
    array = list(im.getdata())
    if im.mode == "RGB":
        channels = 3
    if im.mode == "L":
        channels = 1
    else:
        print("Unsuitable image mode (not RGB or L)")
    array = np.array(array).reshape(width, height)
    #print(array.shape)
    # Crop the edges wrt. edge_crop (in any case there is a bit of edge cropping)
    array = np.delete(array, list(range(0, edge_crop_x)), axis=1)
    array = np.delete(array, list(range(array.shape[1] - edge_crop_x, array.shape[1])), axis=1)
    array = np.delete(array, list(range(0, edge_crop_y)), axis=0)
    array = np.delete(array, list(range(array.shape[0] - edge_crop_y, array.shape[0])), axis=0)
    #im.show()
    # rotate image over the y axis centered over the middle of the array
    array = array[::-1]
    return array


def subarray_slice(array, i, j, sz_box_x, sz_box_y):
    ##############################################################################
    """Creating subarrays of initial grid
    i, j = starting indices of subarray
    comment: i,j should be kept in bounds s.t.
    lenght of initial array should not be
    exceeded.
    sz_box_x = size of matrix in x direc.
    sz_box_y = size of matrix in y direc."""
    array = np.delete(array, list(range(0, i)), axis=1)
    array = np.delete(array, list(range(sz_box_x, array.shape[1])), axis=1)
    array = np.delete(array, list(range(0, j)), axis=0)
    array = np.delete(array, list(range(sz_box_y, array.shape[0])), axis=0)
    return array

def matrix_of_subarrays(array, sz_box_x, sz_box_y, a = True, b = False):
    ############################################################################
    """This function creates subarrays of initial array with sizes
    sz_box_x times sz_box_y. It takes the function subarray_slice
    and iterates it over the whole array
    a = True, b = False returns list of arrays
    a = False, b = True returns coordinates of arrays
    both are in sequence t.i. array number 0 has index
    (0,0), array 1 has index (sz_box_y,0) ..."""
    global height
    global width
    # croping the initial array to fit in all subarrays without unused columns/rows
    if array.shape[1] % sz_box_x != 0:
        array = np.delete(array, list(range(0, array.shape[1] % sz_box_x)), axis=1)
    if array.shape[0] % sz_box_y != 0:
        array = np.delete(array, list(range(0, array.shape[0] % sz_box_y)), axis=0)
    # append all the subarrays to list_new
    list_new = []
    list_new_coord = []
    for i in range(0, array.shape[1], sz_box_x):
        for j in range(0, array.shape[0], sz_box_y):
            #(subarray_slice(array, i, j, sz_box_x, sz_box_y))
            list_new.append((subarray_slice(array, i, j, sz_box_x, sz_box_y)))
            list_new_coord.append((i, j))
    #np.array(list_new)
    if a:
        return np.array(list_new)
    if b:
        return np.array(list_new_coord)
    #############################################################################

def interval_of_tolerance_diffpixel(x, tol):
    ###############################################################################
    """Here we define the tolerance of choosing
    which pixels to eliminate from the final
    graph"""
    if x <= x + tol:
        return list(range(0, x + tol))
    ###############################################################################

def matrix_value_test(list_of_arrays, list_new_coord, pixel, tol, treshold_of_values):
    ############################################################################
    """This function passes or fails certain subarrays whether they contain enough
    values in tolerance. If they do, it returns to us coordinates of the subarray
    for later plotting"""
    # here we define tally for keeping score on number of values, repository for keeping
    #track of which subarrays are contributing and final_coordinates for the cooridnates
    #we will want to graph
    tally = 0
    repository = []
    final_coordinates = []
    # loop over all rows in a all subarrays and compare row values with tolerance
    for m in range(0, len(list_of_arrays)):
        for x in list_of_arrays[m]:
            for y in x:
                if y in interval_of_tolerance_diffpixel(pixel, tol):
                    tally = tally + 1
                    continue
        # if threshold is achieved, return relevant info
        if tally >= treshold_of_values:
            repository.append((tally, m))
            final_coordinates.append(list_new_coord[m])
            tally = 0
    final_coordinates = np.array(final_coordinates)
    print(f"Number of instances and subarray column: {repository}")
    print(f"Relevant coordinates for plotting: {final_coordinates}")
    return  final_coordinates

def graphing_function(type, final_coordinates):
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
    for u in final_coordinates:
        list_x.append(u[0])
    for z in final_coordinates:
        list_y.append(z[1])
    plt.plot(list_x, list_y, type)
    plt.show()
    ###############################################################################

####################################################################################
# Actual program
def start():
    q1 = input("Do you wish to get coord. of pic? (y/n)  ")
    if q1 == "y":
        questions()
    if q1 == "n":
        exit()
    else:
        print("Only y/n values are allowed")

def questions():
    q2 = input("Enter path: (e.g.: D:\Testna_mapa\slika3.jpg)  ")
    q3 = int(input("Choose cropping in x direction: (num pixels)  "))
    q4 = int(input("Choose cropping in y direction: (num pixels)  "))
    q5 = int(input("Choose subarray dim in x direc: (num)  "))
    q6 = int(input("Choose subarray dim in y direc: (num)  "))
    q7 = int(input("Choose number of relevant pixels in subbaray: (num)  "))
    q8 = int(input("Choose pixel deviation from black: (num)  "))
    print("\nBelow is the L grid: \n")
    print(get_data(q2, q3, q4))
    print("\nBelow are the subarray's: \n")
    print(matrix_of_subarrays(get_data(q2, q3, q4), q5, q6, a=True, b=False))
    print("\nBelow are the subarray's coordinates (potential points to plot): \n")
    print(matrix_of_subarrays(get_data(q2, q3, q4), q5, q6, a=False, b=True))
    print("\nBelow are the subarray's coordinates (final points to plot): \n")
    print(matrix_value_test(matrix_of_subarrays(get_data(q2, q3, q4), q5, q6, a=True, b=False),
                            matrix_of_subarrays(get_data(q2, q3, q4), q5, q6, a=False, b=True), 0, q8, q7))
    print("Graph is on the screen \n")
    graphing_function("or", matrix_value_test(matrix_of_subarrays(get_data(q2, q3, q4), q5, q6, a=True, b=False),
                            matrix_of_subarrays(get_data(q2, q3, q4), q5, q6, a=False, b=True), 0, q8, q7))

start()
##############################################################################################################
