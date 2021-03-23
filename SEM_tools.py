import cv2 as cv
import numpy as np
import math as m


# Function that takes input image path and binarizes using Otsu thresholding
def binarize(img_path):
    img = cv.imread(img_path, 0)
    _, th_img = cv.threshold(img, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    return th_img


# Crops out information bar at the bottom for HITACHI SU-8100
def crop(img):
    height = np.shape(img)[0]
    width = np.shape(img)[1]
    new_height = round(height*0.93)
    new_img = img[0:new_height+1, 0:width+1]
    return new_img


# Sets scale; takes in magnification and returns pixel size in nm
def set_scale(img_path, mag):
    img = cv.imread(img_path, 0)  # reads img in path stores as img which is a numpy array
    width = np.shape(img)[1]
    if width == 1280:
        pix_size = 99218.76/mag
    if width == 2560:
        pix_size = 51499.385/mag
    return pix_size


# input image path, magnification, NW diameter binarizes and calculates AgNW amd
def amd(img_path, mag, dia):
    ag_density = 10.49*10**(-21)  # g/nm^3

    new_img = binarize(img_path)
    pix_size = set_scale(img_path, mag)  # calculate pixel size in nm
    height_px = np.shape(new_img)[0]
    width_px = np.shape(new_img)[1]
    area_px = height_px * width_px  # total number of pixels in image
    height_nm = pix_size*height_px  # height of image in nm
    width_nm = pix_size*width_px  # width of image in nm

    total_area = height_nm * width_nm  # total area of the image in nm^2
    nw_pix_count = area_px - np.count_nonzero(new_img)  # pixel count of NW region (black = 0)
    nw_volume = nw_pix_count * pix_size**2 * dia * m.pi/4  # volume of NW region assuming area ratio between circle square; in nm^3
    nw_mass = nw_volume * ag_density * 1000  # in micrograms

    amd_ = nw_mass/total_area * 10**18  # in mg/m^2

    #print(f'The areal mass density is {amd_} mg/m^2')
    return amd_
