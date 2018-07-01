# Used to concatenate the pages for the documents in http://sceti.library.upenn.edu/PhilaNeighborhoods/browse.cfm#

from urllib.request import urlopen
import urllib.request
import re
from fpdf import FPDF

url_base = "http://sceti.library.upenn.edu/pages/index.cfm?so_id=4377&pageposition=XXXXX&level=3" 

link_base = "http://images.library.upenn.edu/mrsidsceti/bin/image_jpeg2.pl?coll=printedbooks;subcoll=ht177p5p64_1960;image=ht177p5p64_1960_front9999.sid;level=3;degree=0"

imagelist = []
for i in range(1, 10):
    html = urlopen(url_base.replace("XXXXX", str(i)))
    #print(html.read().decode("utf-8"))
    img_match = re.search(r'(http://images\.library\.upenn\.edu.*?)"', html.read().decode("utf-8"))
    if img_match:
        img_url = img_match.groups(0)[0]
        # http://sceti.library.upenn.edu/pages/zoom.cfm?coll=printedbooks&subcoll=tl726.4p5a4_1946&FileName=tl726.4p5a4_1946_front0009.sid&width=5000&height=5000&level=3&rotated=0&myimage.x=100&myimage.y=100
        img_url = img_url.replace(";level=3;degree=0", "&width=5000&height=5000&level=3&rotated=0&myimage.x=100&myimage.y=100")
        img_url = img_url.replace("mrsidsceti/bin/image_jpeg2.pl?", "pages/zoom.cfm?")
        img_url = img_url.replace("images.library.upenn.edu", "sceti.library.upenn.edu")
        img_url = img_url.replace(";image=", "&FileName=")
        img_url = img_url.replace(";subcoll", "&subcoll")
        print(img_url)
        urllib.request.urlretrieve(img_url, "images/{}.JPEG".format(i))
        imagelist.append("images/{}.JPEG".format(i))
    else:
        break

pdf = FPDF()
for image in imagelist:
    pdf.add_page()
    pdf.image(image, 10, 10, 190)
pdf.output("1.pdf", "F")
