from PIL import Image
import requests
#import urllib.request
#urllib.request.urlretrieve("https://ami.animecharactersdatabase.com/uploads/chars/thumbs/200/5688-1825642757.jpg", "5688-1825642757.jpg")
"""
img1 = Image.open(r"frame1.jpg")

# Opening the secondary image (overlay image)
img2 = Image.open(r"gfg.jpg")

# Pasting img2 image on top of img1
# starting at coordinates (0, 0)
img1.paste(img2, (0,0))

img1.show()



"""

#Read the two images
image1 = Image.open('gfg.jpg')
image1.show()
image2 = Image.open('frame4.jpg')
image2.show()
#resize, first image
image1 = image1.resize((426, 240))
image1_size = image1.size
image2_size = image2.size
new_image = image1
#new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
new_image.save("images/merged_image.jpg","JPEG")
new_image.show()


"""
# creating a image1 object and convert it to mode 'P'
im1 = Image.open("frame1.jpg").convert('P')

# creating a image2 object and convert it to mode 'P'
im2 = Image.open("gfg.jpg").convert('P')

# alpha is 0.0, a copy of the first image is returned
im3 = Image.blend(im1, im2, 0.0)

# to show specified image
im3.show()


"""
"""
# Function to change the image size
def changeImageSize(maxWidth,
                    maxHeight,
                    image):

    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(1.5*(widthRatio*image.size[0]))
    newHeight   = int(3*(heightRatio*image.size[1]))

    newImage    = image.resize((newWidth, newHeight))
    return newImage

# Take two images for blending them together
image1 = Image.open("frame4.jpg")
#, stream=True)
image2 = Image.open("gfg.jpg")#.raw

# Make the images of uniform size
image3 = changeImageSize(800, 550, image1)
image4 = changeImageSize(800, 550, image2)

# Make sure images got an alpha channel
image5 = image3.convert("RGBA")
image6 = image4.convert("RGBA")

# Display the images
#image5.show()
#image6.show()

# alpha-blend the images with varying values of alpha
#alphaBlended1 = Image.blend(image5, image6, alpha=.2)
alphaBlended2 = Image.blend(image5, image6, alpha=.1)

# Display the alpha-blended images
#alphaBlended1.show()
alphaBlended2.show()
"""
