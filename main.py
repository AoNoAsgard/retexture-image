from PIL import Image
import random

delta= 30

im = Image.open(r"input/image.png")
im.show()

punti = []
rgb_im = im.convert('RGB')

larghezza,altezza  = im.size
print("h:"+str(altezza),"l:"+str(larghezza))
'''
for x in range(larghezza):
    for y in range(altezza):
        punti.append(tuple((x,y)))
'''
outIm = Image.new('RGB',(larghezza, altezza),color="white")

oipixels = outIm.load()
#print(punti)
for x in range(larghezza):
    for y in range(altezza):
        r , g , b = rgb_im.getpixel((x,y))
        #print(r,g,b)
        oipixels[x,y] = (abs( int(random.randint(r-delta,r+delta)) ) , abs( int(random.randint(g-delta,g+delta))) , abs( int(random.randint(b-delta,b+delta))) )


im.show()

outIm.save("output/image.png")




  