# Used to concatenate the pages for the documents in http://sceti.library.upenn.edu/PhilaNeighborhoods/browse.cfm#

from urllib.request import urlopen
import urllib.request
import re
from fpdf import FPDF
import copy

# http://images.library.upenn.edu/mrsidsceti/bin/image_jpeg2.pl?coll=printedbooks&subcoll=tl726.4p5a4_1946&image=tl726.4p5a4_1946_front0002.sid&level=0&rotated=0&x=1832&y=2312&width=3700&height=4600
def zoomed_url(oldurl):
    new_url = copy.copy(oldurl)
    new_url = new_url.replace("level=3;degree=0",
      "level=0&rotated=0&x=1832&y=2312&width=3700&height=4600")
    new_url = "&".join(new_url.split(";"))
    return new_url

def make_pdf_from_images(imagelist, doc_id):
    pdf = FPDF()
    for image in imagelist:
        try:
            pdf.add_page()
            pdf.image(image, 10, 10, 190)
        except RuntimeError:
            print("ERROR: bad image {}. Skipping...".format(image))
    pdf.output("pdfs/{}.pdf".format(doc_id), "F")

ids = [4377, 4780, 5927, 5933, 2590, 4130, 5930, 5939, 4094, 6621, 2601, 5987, 
4371, 4381, 5984, 4379, 5944, 5935, 5989, 5920, 5921, 2606, 7720, 4784, 6341, 
4091, 4336, 5925, 4072, 6344, 4328, 4372, 2592, 4329, 6620, 4330, 4380, 6346,
4369, 5936, 4333, 4089, 5976, 4073, 4335, 6347, 2586, 2609, 5983, 4782, 4781, 5931, 2608, 5985, 5923, 4783, 4093, 2591, 2720, 4373, 4374, 4375, 4376, 6340, 5926, 5932, 4074, 5934, 4131, 4088, 5986, 6147, 4327, 6301, 5937, 5922, 5928, 2614, 5929, 4331, 4332, 4378, 5938, 4785, 4283, 4368, 5945, 2741, 4334]

done = [4377, 4780, 5927, 5933, 2590, 4130, 5930, 5939, 4094, 6621, 2601, 5987,
4371, 4381, 5984, 4379, 5944, 5935, 5989, 5920, 5921, 2606, 7720, 4784, 6341, 
4091, 4336, 5925, 4072, 6344, 4328, 4372, 2592, 4329, 6620, 4330, 4380, 6346, 
4369, 5936, 4333, 4089, 5976, 4073, 4335, 6347, 2586, 2609, 5983, 4782]

url_base = "http://sceti.library.upenn.edu/pages/index.cfm?so_id=XXXXX&pageposition=YYYYY&level=3" 

for ix, doc_id in enumerate(ids):
    if doc_id in done:
        print("Skipping job {} (already done)".format(doc_id))
        continue
    print("\n\nSTARTING JOB {}: DOC ID = {}".format(ix+1, doc_id))
    url_doc_base = url_base.replace("XXXXX", str(doc_id))
    imagelist = []
    for i in range(1, 9999):
        url_page = url_doc_base.replace("YYYYY", str(i))
        html = urlopen(url_page)
        img_match = re.search(r'(http://images\.library\.upenn\.edu.*?)"',
                              html.read().decode("utf-8"))
        if img_match:
            img_url = img_match.groups(0)[0]
            img_url = zoomed_url(img_url)
            print(img_url)
            urllib.request.urlretrieve(img_url, 
              "images/{}_{:04d}.jpg".format(doc_id, i))
            imagelist.append("images/{}_{:04d}.jpg".format(doc_id, i))
        else:
            print('No url found. Breaking...')
            break
    print("Generating pdf...")
    make_pdf_from_images(imagelist, doc_id)

