from PIL import Image
import pytesseract
import argparse
import cv2
import subprocess
import os

ids = [4377, 4780, 5927, 5933, 2590, 4130, 5930, 5939, 4094, 6621, 2601, 5987,
4371, 4381, 5984, 4379, 5944, 5935, 5989, 5920, 5921, 2606, 7720, 4784, 6341, 
4091, 4336, 5925, 4072, 6344, 4328, 4372, 2592, 4329, 6620, 4330, 4380, 6346, 4369, 5936, 4333, 4089, 5976, 4073, 4335, 6347, 2586, 2609, 5983, 4782, 4781, 5931, 2608, 5985, 5923, 4783, 4093, 2591, 2720, 4373, 4374, 4375, 4376, 6340, 5926, 5932, 4074, 5934, 4131, 4088, 5986, 6147, 4327, 6301, 5937, 5922, 5928, 2614, 5929, 4331, 4332, 4378, 5938, 4785, 4283, 4368, 5945, 2741, 4334]

done = [4377, 4780, 5927, 5933, 2590, 4130, 5930, 5939, 4094, 6621, 2601, 5987,
4371, 4381, 5984, 4379, 5944, 5935, 5989, 5920, 5921, 2606, 7720, 4784, 6341, 
4091, 4336, 5925, 4072, 6344, 4328, 4372, 2592, 4329, 6620, 4330, 4380, 6346,
4369, 5936, 4333, 4089, 5976, 4073, 4335, 6347, 2586, 2609, 5983, 4782, 4781,
5931, 2608, 4783, 4093, 2591, 2720, 4373, 4374, 4375, 4376, 6340, 5932, 4074,
5934, 4131, 5986, 6147, 4327, 5937, 2614, 4331, 4332, 4378, 4785, 5945, 2741,
4334, 5985, 5923, 5926, 4088]

all_images = os.listdir("/home/lucas/git/urban-discontents/quicktools/images/")

def ocr_image(path_to_image):
    image = cv2.imread(path_to_image)
    gray = cv2. cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    return text

for doc_id in ids:
    if doc_id in done:
        print('Skipping job {}...'.format(doc_id))
        continue
    print('Starting document {}...'.format(doc_id))
    pages = sorted(filter(lambda x: "{}_".format(doc_id) in x, all_images))
    with open("output/{}.txt".format(doc_id), "a+") as out_fp:
        for page in pages:
            print('OCRing doc {} page {}...'.format(doc_id, page))
            try:
                out = ocr_image("/home/lucas/git/urban-discontents/quicktools/images/{}".format(page))
            except cv2.error:
                print('Error processing image. Skipping...')
                continue
            #out = out.decode("utf-8")
            out_fp.write("".join(out.split("-\n")))
            out_fp.write('\n\n')
    print('\n')
