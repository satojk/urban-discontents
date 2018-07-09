# COPIED FROM
# https://nedbatchelder.com/blog/200712/extracting_jpgs_from_pdfs.html
# Adapted to python3

# Extract jpg's from pdf's. Quick and dirty.
import sys

in_file = open(sys.argv[1], "rb")
pdf = in_file.read()
in_file.close()

startmark = b"\xff\xd8"
startfix = 0
endmark = b"\xff\xd9"
endfix = 2
i = 0

njpg = 0
while True:
    istream = pdf.find(b"stream", i)
    if istream < 0:
        break
    istart = pdf.find(startmark, istream, istream+20)
    if istart < 0:
        i = istream+20
        continue
    iend = pdf.find(b"endstream", istart)
    if iend < 0:
        raise Exception("Didn't find end of stream!")
    iend = pdf.find(endmark, iend-20)
    if iend < 0:
        raise Exception("Didn't find end of JPG!")
     
    istart += startfix
    iend += endfix
    print("JPG {} from {} to {}".format(njpg, istart, iend))
    jpg = pdf[istart:iend]
    jpgfile = open("jpg{}.jpg".format(njpg), "wb")
    jpgfile.write(jpg)
    jpgfile.close()
     
    njpg += 1
    i = iend
