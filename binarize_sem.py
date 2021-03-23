import cv2 as cv


# Function that takes input image path and binarizes using Otsu thresholding

img_path1 = 'C:/Users/whcha/Desktop/image.tif'
def binarize_sem(img_path):
    img = cv.imread(img_path, 0)
    _, th_img = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    cv.imshow('binary_img', th_img)
    cv.imwrite('binary_img.tif', th_img)
    cv.waitKey(0)
    return th_img

binarize_sem(img_path1)