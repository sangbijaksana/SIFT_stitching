import cv2
from utils.border import crop_both_black_border, create_border
from utils.homography import find_homography

def combine_image(img1, img2):
    img1, img2 = crop_both_black_border(img1, img2)

    result = img2.copy()
    img_widht, img_height, _ = img1.shape

    for width in range(img_widht):
        for height in range(img_height):

            if sum(img1[width][height][:]) == 0:
                result[width][height][:] = img2[width][height][:]
            if sum(img2[width][height][:]) == 0:
                result[width][height][:] = img1[width][height][:]

    return result

def stitch_image(img1_path, img2_path):
    image1, image2 = create_border(img1_path, img2_path)
    homography = find_homography(image1, image2)

    result = cv2.warpPerspective(image1, homography, (image2.shape[1], image2.shape[0]))
    blended_image = combine_image(result, image2)

    return blended_image