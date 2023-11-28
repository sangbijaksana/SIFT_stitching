import cv2
from utils.combine import stitch_image 
from utils.panorama import make_panorama

image_pair_list = [
    ['./images/original/pairs_01_01.jpg', './images/original/pairs_01_02.jpg'],
    ['./images/original/pairs_02_01.png', './images/original/pairs_02_02.png'],
    ['./images/original/pairs_03_01.jpg', './images/original/pairs_03_02.jpg'],
    ['./images/original/pairs_04_01.jpg', './images/original/pairs_04_02.jpg'],
]

idx = 0
for image_pair in image_pair_list:
    idx += 1
    img1_path = image_pair[0]
    img2_path = image_pair[1]

    stitch_image_result = stitch_image(img1_path, img2_path)
    stich_image_name = "./images/combined/pairs_{}.jpg".format(idx)

    cv2.imwrite(stich_image_name, stitch_image_result)
    print("Created stich image:" + stich_image_name)

    panorama_image_result = make_panorama(stitch_image_result)
    panorama_image_name = "./images/panorama/pairs_{}.jpg".format(idx)
    
    cv2.imwrite(panorama_image_name, panorama_image_result)
    print("Created panorama image:" + panorama_image_name)
