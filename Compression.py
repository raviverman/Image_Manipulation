import matplotlib.pyplot as plt
import numpy as np

# Load Image
image = plt.imread('galaxy.jpg')

plt.subplot(1,3,1)
# Place original image in 1st subplot
plt.axis('off')
plt.title('Original')
plt.imshow(image)


plt.subplot(1,3,2)
# Place next image in II plot
init = 0
blockSize = 16   # blocks to be merged (mean calculated)
height = blockSize # custom control on block height // To be modified if height & width
width = blockSize  # custom control on block height // are different

image2 = image.copy()  #Make copy of original readonly image ( Image2 on plot)
# image2 's size is equal to original size

smallImage = []  # (Image 3 on plot)  
# small image's size is of TotalHeight/height and width TotalWidht/width but not mean

for pixel in image[0::height]:
    tempData = []
    for i in range(0, len(pixel), width):
        if(i + width < len(pixel) ):
            # Calculating mean of pixels
            redMean = np.mean(image[init:init + height,i:i+width, 0])
            greenMean = np.mean(image[init:init + height,i+width, 1])
            blueMean = np.mean(image[init:init + height,i+width, 2])
            
            #applying mean value
            image2[init:init + height,i:i+width, 0]  = redMean
            image2[init:init + height,i:i+width, 1]  = greenMean
            image2[init:init + height,i:i+width, 2]  = blueMean
            
            #pixel for new smallImage (don't know why it comes inver)
            # pix = [255-redMean,255-greenMean,255-blueMean]
            # tempData = tempData + [pix]

    init = init + height
    # smallImage += [tempData]
    smallImage += [pixel[0::width]]

plt.imshow(image2)
plt.axis('off')
plt.title('Block Size :  ' + str(height) +' x ' + str(width) +' pixels')

plt.subplot(1,3,3)
#plot third image
plt.axis('off')
plt.imshow(smallImage)
plt.tight_layout()
# plt.savefig('fig2.png', format='png')
plt.show()
#END