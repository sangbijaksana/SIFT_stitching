import cv2
import numpy as np

def create_border(img1_path, img2_path):
    image1 = cv2.imread(img1_path)
    image2 = cv2.imread(img2_path)

    image1 = cv2.copyMakeBorder(
                    image1, 1500, 1500, 1500, 1500,
                    cv2.BORDER_CONSTANT, value=0)

    image2 = cv2.copyMakeBorder(
                    image2, 1500, 1500, 1500, 1500,
                    cv2.BORDER_CONSTANT, value=0)

    return image1, image2

def crop_both_black_border(img1, img2):
    img1_y_nonzero, img1_x_nonzero, _ = np.nonzero(img1)
    img2_y_nonzero, img2_x_nonzero, _ = np.nonzero(img2)

    min_y_nonzero = min(np.min(img1_y_nonzero), np.min(img2_y_nonzero))
    max_y_nonzero = max(np.max(img1_y_nonzero), np.max(img2_y_nonzero))

    min_x_nonzero = min(np.min(img1_x_nonzero), np.min(img2_x_nonzero))
    max_x_nonzero = max(np.max(img1_x_nonzero), np.max(img2_x_nonzero))

    img1 = img1[min_y_nonzero:max_y_nonzero, min_x_nonzero:max_x_nonzero]
    img2 = img2[min_y_nonzero:max_y_nonzero, min_x_nonzero:max_x_nonzero]

    return img1, img2

def crop_black_border(image):
    y_nonzero, x_nonzero, _ = np.nonzero(image)
    return image[np.min(y_nonzero):np.max(y_nonzero), np.min(x_nonzero):np.max(x_nonzero)]