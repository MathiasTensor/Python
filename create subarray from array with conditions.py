from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import re

#Given an array, construct a subarray satisfying number of tolerance conditions for
#set of elements in subarray. Return pos. of subarray in array for further use in image/L
#detection. Still in progress

#Example
a = np.array(range(0,72))
a = np.array(a).reshape(8, 9)
height = 8
width = 9
print(a)


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

def matrix_of_subarrays(array, sz_box_x, sz_box_y):
    ############################################################################
    """This function creates subarrays of initial array with sizes
    sz_box_x times sz_box_y. It takes the function subarray_slice
    and iterates it over the whole array """
    global height
    global width
    # croping the initial array to fit in all subarrays without unused columns/rows
    if array.shape[1] % sz_box_x != 0:
        array = np.delete(array, list(range(0, array.shape[1] % sz_box_x)), axis=1)
    if array.shape[0] % sz_box_y != 0:
        array = np.delete(array, list(range(0, array.shape[0] % sz_box_y)), axis=0)
    height = array.shape[0]
    width = array.shape[1]
    list_new = []
    # append all the subarrays to list_new
    for i in range(0, array.shape[1], sz_box_x):
        for j in range(0, array.shape[0], sz_box_y):
            #(subarray_slice(array, i, j, sz_box_x, sz_box_y))
            list_new.append((subarray_slice(array, i, j, sz_box_x, sz_box_y)))
    np.array(list_new)
    return np.array(list_new)
    #############################################################################

def interval_of_tolerance_diffpixel(x, tol):
    ###############################################################################
    """Here we define the tolerance of choosing
    which pixels to eliminate from the final
    graph"""
    if x <= x + tol:
        return list(range(0, x + tol))
    ###############################################################################

def matrix_value_test(array, list_of_arrays, tolerance, treshold_of_values, sz_box_x, sz_box_y):
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
                if y in tolerance:
                    tally = tally + 1
                    continue
        # if threshold is achieved, return relevant info
        if tally >= treshold_of_values:
            repository.append((tally, m))
            i = m * sz_box_x % array.shape[1]
            j = m * sz_box_y % array.shape[0]
            final_coordinates.append((i, j))
            tally = 0
    # for user checking
    print(f"Number of instances and subarray column: {repository}")
    return  final_coordinates
