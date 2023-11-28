from utils.border import crop_black_border

def chunk_width(img1, threshold):

    result = img1.copy()
    img1_width, img1_height, _ = img1.shape

    for width in range(img1_width):
        cnt_zero_count = 0

        for height in range(img1_height):
            if sum(img1[width][height][:]) == 0:
                cnt_zero_count += 1

        if cnt_zero_count < (img1_width*threshold):
            continue

        for height in range(img1_height):
            result[width][height][:] = [0,0,0]

    return crop_black_border(result)

def chunk_height(img1, threshold):

    result = img1.copy()
    img1_width, img1_height, _ = img1.shape

    for height in range(img1_height):
        cnt_zero_count = 0

        for width in range(img1_width):
            if sum(img1[width][height][:]) == 0:
                cnt_zero_count += 1

        if cnt_zero_count < (img1_width*threshold):
            continue

        for width in range(img1_width):
            result[width][height][:] = [0,0,0]

    return crop_black_border(result)

def make_panorama(img1):
    threshold = 0.5
    panorama_img = chunk_width(img1, threshold)
    panorama_img = chunk_height(panorama_img, threshold)

    threshold = 0.2
    panorama_img = chunk_width(panorama_img, threshold)
    panorama_img = chunk_height(panorama_img, threshold)

    threshold = 0.05
    panorama_img = chunk_width(panorama_img, threshold)
    panorama_img = chunk_height(panorama_img, threshold)

    return panorama_img