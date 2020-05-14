from PIL import Image, ImageDraw
inp=input().split()
try:
    image_inp=inp[0]
except:
    image_inp="1.jpg"
try:
    image_out=inp[1]
except:
    image_out="out.jpg"
try:
    image=Image.open(image_inp)
except:
    print ("Net Faila")
else:
    draw=ImageDraw.Draw(image)
    pix=image.load()
    for i in range (image.size[0]):
        for j in range (image.size[1]):
            a=pix[i,j][0]
            b=pix[i,j][1]
            c=pix[i,j][2]
            draw.point((i,j),((a+b+c)//3,(a+b+c)//3,(a+b+c)//3))
    image.save(image_out,"jpeg")

    image.show()
