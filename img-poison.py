import random
import glob
import sys
from PIL import Image

def munge(inpic, outpic, quality=60):
    im = Image.open(inpic)
    boxsize = (im.size[0]//16, im.size[1]//16)
    shift = max(boxsize[0]//8, boxsize[1]//8, 1)
    for i in range(1500):
        x = random.randint(shift, im.size[0]-boxsize[0]-shift)
        y = random.randint(shift, im.size[1]-boxsize[1]-shift)
        im2 = im.crop((x, y, x+boxsize[0], y+boxsize[1]))
        im.paste(im2, (x+shift*random.choice((-1, 1)), y+shift*random.choice((-1, 1))))
    im.save(outpic, quality=quality, exif=im.getexif())

print('image poison: PICs')
for pattern in sys.argv[1:]:
    print('\t{}'.format(pattern))
    for pic in glob.glob(pattern):
        try:
            munge(pic, pic)
        except:
            print('WARNING: error while processing ', pic)
            pass
