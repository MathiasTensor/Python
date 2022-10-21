try:
    import os
except ModuleNotFoundError:
    #print(f'Install via pip in cmd: {"\u0332".join("pip install os")} OR pip3 {"\u0332".join("pip3 install os")}')
    quit()

try:
    import subprocess
except ModuleNotFoundError:
    try:
        os.system('cmd /c "pip install subprocess"')
        import subprocess
    except PermissionError:
        print("No permissions")
        quit()

try:
    import cv2
except ModuleNotFoundError:
    try:
        os.system('cmd /c "pip install cv2"')
        import cv2
    except PermissionError:
        print("No permissions")
        quit()

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    try:
        os.system('cmd /c "pip install matplotlib"')
        import matplotlib.pyplot as plt
    except PermissionError:
        print("No permissions")
        quit()

try:
    import pytesseract
except ModuleNotFoundError:
    try:
        os.system('cmd /c "pip install tesseract"')
        os.system('cmd /c "pip install pytesseract"')
        import pytesseract
    except PermissionError:
        print("No permissions")
        quit()

try:
    import psutil
except ModuleNotFoundError:
    try:
        os.system('cmd /c "pip install psutil"')
        import psutil
    except PermissionError:
        print("No permissions")
        quit()

try:
    from datetime import datetime
except ModuleNotFoundError:
    try:
        os.system('cmd /c "pip install datetime"')
        from datetime import datetime
    except PermissionError:
        print("No permissions")
        quit()

try:
    from PIL import Image
except ModuleNotFoundError:
    try:
        os.system('cmd /c "pip install pillow"')
        from PIL import Image
    except PermissionError:
        print("No permissions")
        quit()

try:
    import numpy as np
except ModuleNotFoundError:
    try:
        os.system('cmd /c "pip install numpy"')
        import numpy as np
    except PermissionError:
        print("No permissions")
        quit()

###############################################################  
# initial parameter ONLY CHANGE THIS. It is a filepath to the given image
image_path = r"C:\Users\Asus\Desktop\Receipts\0_2022_6.jpg"
###############################################################

__all__ = ("TextBoxPreparation", "TesseractOCRBoxInformation", "OCRBOXPlotting", "TextBoxContours","TextBoxImages", "FinalResult")

class TextBoxPreparation:
    """Initial class of this file. Loads the given image and converts it to GrayScale, thresholds it via the Gaussian Blur and finally thresholds it with cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU --> Binary thresholding with inversion accompanied with Otsu thresholding.\n
    For more information:\nhttps://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html\n
    For information about histograms for pixel counts:\nhttps://docs.opencv.org/4.x/d1/db7/tutorial_py_histogram_begins.html """
    def __init__(self, image_path=None) -> None:
        
        # for convenience we will draw them all in the subplot grid
        self.fig = plt.figure(figsize=(12, 10))
        self.fig.suptitle("Different char boxes detections")
        self.subfigs = self.fig.subfigures(1, 2)
        # open image with cv2
        self.load = cv2.imread(image_path)
        self.load_grayscale = cv2.imread(image_path, 0)
        # add image to figure via subplots
        self.subplot_left = self.subfigs[0]
        self.subplot_left.suptitle("Thresholding and Tesseract OCR")
        self.subplot_left.set_edgecolor("red")
        self.subplot_left.set_linewidth(2)
        
        # adding subplots to subfiguresć
        self.subplot_left.add_subplot(2, 2, 1)
        plt.imshow(self.load)
        plt.axis("off")
        plt.title("Input image")
        # convert to graypltscale
        self.image_gray = cv2.cvtColor(self.load, cv2.COLOR_BGR2GRAY)
        # Do some Gaissian bluring with kernel size of (9,9) per instruction of site: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
        self.gaussian_threshold_filter = cv2.GaussianBlur(self.image_gray, (15,15), 0)
        # threshold the image (binary + otsu thresholding) --> To distinct out boundaries
        _, self.threshold_image = cv2.threshold(self.image_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        # experimental adaptive thresholding
        #self.threshold_image = cv2.adaptiveThreshold(src=self.gaussian_threshold_filter, maxValue=255, adaptiveMethod=cv2.#ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU, blockSize=11, C=2)
        
        # show intermediate step in subplots
        self.subplot_left.add_subplot(2, 2, 2)
        plt.imshow(self.threshold_image, cmap=plt.cm.Greys)
        plt.axis("off")
        plt.title("Thresholded and GrayScale image")

        # calculate histogram --> could use, we will use matplotlib's own hist method
        self.hist_threshold = cv2.calcHist([self.threshold_image], [0], None, [256], [0, 256])
        self.hist_load_b = cv2.calcHist([self.load], [0], None, [256], [0, 256])
        self.hist_load_g = cv2.calcHist([self.load], [1], None, [256], [0, 256]) 
        self.hist_load_r = cv2.calcHist([self.load], [2], None, [256], [0, 256]) 

        # histogram of pixel intensity pre / post thresholding
        self.subplot_left.add_subplot(2, 2, 3)
        #plt.hist(self.threshold_image, 256, [0,256])
        plt.plot(self.hist_threshold, label="Thresholded image with inversion")
        plt.plot(self.hist_load_r, label="Input Image - RED", c="r")
        plt.plot(self.hist_load_g, label="Input Image - GREEN", c="g")
        plt.plot(self.hist_load_b, label="Input Image - BLUE", c="b")
        plt.legend()
        #plt.axis("off")
        plt.title("Threshold Histogram of Image")
       
        # fit kernel size (15,15)
        self.kernel_size = (15,15)
        # number of iterations
        self.iterations = 10
        # structuring element to check in image --> in out case rectangles (MORPH_RECT). Out structure paramter is kernel size
        self.structure = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=self.kernel_size)
        # dilate the image with the structuring element (Extrude the image morphology)
        self.dilated_image = cv2.morphologyEx(src=self.threshold_image, op=cv2.MORPH_DILATE, kernel=self.kernel_size, dst=None,
                                         anchor=None,
                                         iterations=self.iterations, borderType=cv2.BORDER_REFLECT)


class TesseractOCRBoxInformation(TextBoxPreparation):
    """This class initialises the tesseract module in this file. From this we got in the terminal the image to word string and the bounding boxes of the characters for latter processing / plotting.\n\nAdditional info:\nhttps://nanonets.com/blog/ocr-with-tesseract/\nhttps://pypi.org/project/pytesseract/ """
    def __init__(self, image_path=None) -> None:
        super().__init__(image_path)
        
        # cmd to tesseract
        self.disks = psutil.disk_partitions()
        for parts in self.disks:
            for root, dirs, files in os.walk(parts.device, topdown=True):
                if "tesseract.exe" in files:
                    self.tesseract_path = os.path.join(root, "tesseract.exe")
                    pytesseract.pytesseract.tesseract_cmd = self.tesseract_path
                    print(f"tesseract.exe found at: {os.path.join(root, 'tesseract.exe')}")
                    break

        # boxes made with pytesseract
        self.boxpack = pytesseract.pytesseract.image_to_boxes(image=self.load_grayscale, lang="slv")
        self.text = pytesseract.pytesseract.image_to_string(image=self.load_grayscale, lang="slv")
        
        # splits tring with blank spaces
        self.boxpack_list = self.boxpack.replace("\n", "")
        self.boxpack_list = self.boxpack_list.split(" ")
        # dictionary for consistent rectangle information
        self.dic_rect = dict()
        
        # define function to separate the list in increments of 5
        def list_division(list, n):
            for i in range(0, len(list), n):
                self.dic_rect[f"{i // 5}"] = self.boxpack_list[i:i + 5]
        
        # call instance of function
        list_division(self.boxpack_list, 5)
        # makeparameters information equiped with all rectangle information (pseudo-code)
        # char[key], x_lower[key], y_lower[key], x_upper[key], y_upper[key] = self.dic_rect#[key]
        
        # change all values in  the dictionary to integers, if possible
        for key in self.dic_rect.keys():
            for i in range(len(self.dic_rect[key])):
                try:
                    self.dic_rect[key][i] = int(self.dic_rect[key][i])
                except ValueError:
                    pass
        with open(image_path + "__text__.txt", mode="a") as f:
            f.write(self.text)
            f.write(f"\n\n\n-----------------------------------------------\nText written on: {datetime.now()}")


class OCRBOXPlotting(TesseractOCRBoxInformation):
    """This class plots the character rectangles onto the original image for later comparison. Can be skipped if not needed in final analysis. Is useful because it shows whichs words were recognised because some characters in those that were not recognised do not have a bounding rectangle"""
    def __init__(self, image_path=None) -> None:
        super().__init__(image_path)
        
        # make a copy of the original image to manipulate
        self.OCR_image = self.load.copy()
        # because of tesseract anf cv2 differing views on height (y-axis) definition, we have to substract the height of the picture in the drawing of the rectangles
        self.height = self.load.shape[0]
        # drawing of the rectangles. Some rectangles might have weird keys/values, so we pass them via cv2.error or IndexError
        for key in self.dic_rect.keys():
            try:
                cv2.rectangle(self.OCR_image, pt1=(self.dic_rect[key][1], self.height - self.dic_rect[key][2]), pt2=(self.dic_rect[key][3], self.height - self.dic_rect[key][4]), color=(255, 0, 0), thickness=1)
            except cv2.error:
                pass
            except IndexError:
                pass
        
        # show the final blitted image with rectangles on the subplots
        self.subplot_left.add_subplot(2, 2, 4)
        plt.imshow(self.OCR_image)
        plt.axis("off")
        plt.title("Bltlitted rectangles - Tesseract OCR")
        

class TextBoxContours(TextBoxPreparation):
    """Analogous to OCRBOXPlotting class. Only this time we find the character rectangles not with the tesseract library, but rather with cv2 image thresholding and finding contours / contour hierarchies. This provides a comparison with both methods. The method in cv2.findContours function is cv2.CHAIN_APPROX_NONE, which is a slow method but stores ALL contour points (not just the rect special ones). We will check all possible modes with this method. This class highlight the purpose of this file, and that is rectangle blitting performance in different modes. This should help you choose.\n\nAdditional sources: https://learnopencv.com/contour-detection-using-opencv-python-c/ """
    def __init__(self, image_path=None) -> None:
        super().__init__(image_path)
        
        # 4 copies of images to manipulate them
        self.contours_image_0 = self.load.copy()
        self.contours_image_1 = self.load.copy()
        self.contours_image_2 = self.load.copy()
        self.contours_image_3 = self.load.copy()

        # dictionary of contour images
        self.dic_image_copies = {0: self.contours_image_0, 1: self.contours_image_1, 2: self.contours_image_2, 3: self.contours_image_3}
        
        # finding closed contours in image. Here we will iterate over all the modes of findContours function. For this we will construct a dictionary
        self.dic_modes = {0: cv2.RETR_EXTERNAL, 1: cv2.RETR_TREE, 2: cv2.RETR_LIST, 3: cv2.RETR_CCOMP}
        self.dic_modes_coord_list = dict()
        
        # add subplot instance to the right subfigure
        self.subplot_right = self.subfigs[1]
        self.subplot_right.suptitle("Different modes of rectangle detection")
        self.subplot_right.set_edgecolor("red")
        self.subplot_right.set_linewidth(2)
        
        for k in range(0, 4, 1):
            
            self.contours, self.hierarchy = cv2.findContours(self.dilated_image, mode=self.dic_modes[k], method=cv2.CHAIN_APPROX_NONE)

            # contours have a lot of information in them. We only want the bounding rectangles. Per documentation we enumerate the contours and only the second parameter (c) get analysed / used further.
            # We will also create a list of coordinates (coord_list), whose elements (e.g. coord_list[i]) are (pt1, pt2)'s.
            for j, c in enumerate(self.contours):
                # for paramter (c) we give him a bounding rectangle ()
                bound_rect = cv2.boundingRect(c)
                # giving the bounding rectangle new logical names:
                rect_x = bound_rect[0]
                rect_y = bound_rect[1]
                rect_w = bound_rect[2]
                rect_h = bound_rect[3]

                (pt1, pt2) = (rect_x, rect_y), (rect_x + rect_w, rect_y + rect_h)

                # initializes for key-value pairs the default value type (that is list, so we can append to list)
                self.dic_modes_coord_list.setdefault(k, [])
                self.dic_modes_coord_list[k].append((pt1, pt2))

            cv2.drawContours(self.dic_image_copies[k], self.contours, -1, (255, 0, 0), thickness=1)
            self.subplot_right.add_subplot(2, 2, k + 1)
            plt.imshow(self.dic_image_copies[k])
            plt.axis("off")
            plt.title(f"Blitted rectangels - findContours\nwith cv2.CHAIN_APPROX_NONE and\n{self.dic_modes[k]} mode () integer of mode)")


class TextBoxImages(TextBoxContours, OCRBOXPlotting, TesseractOCRBoxInformation, TextBoxPreparation):
    """This class crops the image with rectangles corresponding with the rectangle of the character found via the image thresholding and finding the contours"""
    def __init__(self, image_path=None) -> None:
        super().__init__(image_path)
        # Transform cv2 Mat object to array (parentheses [:,:] required for all elements)
        self.image_to_array = np.array(self.load[:,:])
        #print(self.image_to_array)
        self.PIL_image = Image.fromarray(self.image_to_array)
        self.dic_copy_images = dict()

        #if not os.path.isdir(f"{os.path.split(image_path)[0]}\{os.path.splitext(os.path.split(image_path)[1])[0]}"):
        #    os.makedirs(f"{os.path.split(image_path)[0]}\{os.path.splitext(os.path.split(image_path)[1])[0]}")
        
        for key in self.dic_modes_coord_list.keys():
            # create a directory for each separate key (if not found)
            # key folder:
            self.key_folder = f"{os.path.split(image_path)[0]}\{os.path.splitext(os.path.split(image_path)[1])[0]}\{key}"
            if not os.path.isdir(self.key_folder):
                os.makedirs(self.key_folder)
            
            for value in self.dic_modes_coord_list[key]:
                #print(f"value00 {value[0][0]}, value11 {value[1][1]} ")
                index = self.dic_modes_coord_list[key].index(value)
                self.dic_copy_images[index] = self.PIL_image.copy()
                try:
                    self.crop = self.dic_copy_images[index].crop((value[0][0], value[0][1], value[1][0], value[1][1]))
                except TypeError:
                    pass

                try:
                    self.crop.save(f"{self.key_folder}\crop{index}.jpg")
                except FileNotFoundError:
                    pass
                except AttributeError:
                    pass


class FinalResult(TextBoxContours, OCRBOXPlotting, TesseractOCRBoxInformation, TextBoxPreparation):
    """Class that executes all** the other classes in this file together. Has no special __init__ attributes or methods on its own apart from plt.show() and plt.tight_layout().\n\n** Does not contain the class TextBoxImages, which crops the image and returns to us sample images of cahracters which will be resized to 28x28 pixels for the neural network input layer"""
    def __init__(self, image_path=None) -> None:
        super().__init__(image_path)
        
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    #FinalResult(image_path=image_path)
    TextBoxImages(image_path=image_path)
