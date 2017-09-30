from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
#from io import BytesIO
#from urllib.request import urlopen
from os import listdir
from os.path import isfile, join
import textwrap

line_width = 40

quotes = "quotes.txt"
base_dir= "/media/chrx/Storage/quoteBatch/"
font = ImageFont.truetype(base_dir+"fonts/amatic.ttf", 15)
img_dir = base_dir+"img/"
FOREGROUND = (255, 255, 255)


def process(filePath, quote, author):
    img = Image.open(filePath)
    img = img.convert("RGBA")

    # make a blank image for the rectangle, initialized to a completely transparent color
    tmp = Image.new('RGBA', img.size, (0,0,0,0))

    # get a drawing context for it
    draw = ImageDraw.Draw(tmp)

    # draw a semi-transparent rect on the temporary image
    draw.rectangle(((0, 0), img.size), fill=(0,0,0,127))

    margin = offset = 40

    for line in textwrap.wrap(quote, width=line_width):
        draw.text((margin, offset), line, fill=FOREGROUND)
        offset += font.getsize(line)[1]

    # composite the two images together
    img = Image.alpha_composite(img, tmp)
    img = img.convert("RGB")

    img.save(filePath.split("/")[-1])




files = [f for f in listdir(img_dir) if isfile(join(img_dir, f))]
with open(quotes) as f:
    content = f.readlines()

n = 0
for img in files:
    quote, author = content[n].split("~")
    process(img_dir+img, quote, author)
    n = n +1
