import subprocess
import os

ids = [4377, 4780, 5927, 5933, 2590, 4130, 5930, 5939, 4094, 6621, 2601, 5987, 
4371, 4381, 5984, 4379, 5944, 5935, 5989, 5920, 5921, 2606, 7720, 4784, 6341, 
4091, 4336, 5925, 4072, 6344, 4328, 4372, 2592, 4329, 6620, 4330, 4380, 6346]

done = []

all_images = os.listdir("/home/lucas/git/urban-discontents/quicktools/images/")

for doc_id in ids:
    if doc_id in done:
        print('Skipping job {}...'.format(doc_id))
        continue
    print('Starting document {}...'.format(doc_id))
    pages = sorted(filter(lambda x: "{}_".format(doc_id) in x, all_images))
    with open("output/{}.txt".format(doc_id), "a+") as out_fp:
        for page in pages:
            print('OCRing doc {} page {}...'.format(doc_id, page))
            ocr_program = subprocess.Popen("python3 ocr.py --image \
            /home/lucas/git/urban-discontents/quicktools/images/{} \
            --preprocess blur".format(page).split(), stdout=subprocess.PIPE)
            out, err = ocr_program.communicate()
            out = out.decode("utf-8")
            out_fp.write("".join(out.split("-\n")))
            out_fp.write('\n\n')
    print('\n')
