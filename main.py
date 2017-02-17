import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#read the image
image = mpimg.imread('images/test.jpg')
print('This image is: ', type(image),
      ' with dimensions ', image.shape)

#Grab the X and Y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]

"""
#Define color selection criteria
############

color_select = np.copy(image)
red_threshold = 200
green_threshold = 200
blue_threshold = 200
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

thresholds = (image[:,:,0] < rgb_threshold[0])\
        | (image[:,:,1] < rgb_threshold[1])\
        | (image[:,:,2] < rgb_threshold[2])

color_select[thresholds] = [0,0,0]

#dispay the image

plt.subplot(221), plt.title('Original'),  plt.imshow(image)
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.title('Color Corrected'), plt.imshow(color_select)
plt.xticks([]), plt.yticks([])
plt.show()

#Define a TRIANGLE ROI
######

region_select=np.copy(image)

#Keep in mind the origin (X=0, Y=0) is in the upper left
left_bottom = [136,539]
right_bottom = [790,539]
apex = [477,322]

#Fit lines (y=AX+B) to ID the 3 sided region
fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]),(right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

#Find the region inside the lines
XX, YY = np.meshgrid(np.arange(0,xsize),np.arange(0,ysize))
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))

#Color all pizels in the ROI red
region_select[region_thresholds] = [255,0,0]

plt.imshow(region_select)
plt.show()
"""

#Combine color and Region
color_select = np.copy(image)
line_image = np.copy(image)

#Define the Color Criteria

red_threshold = 200
green_threshold = 200
blue_threshold = 200
rgb_threshold = [red_threshold,green_threshold,blue_threshold]

left_bottom = [127,539]
right_bottom = [788,539]
apex = [475,330]

fit_left = np.polyfit((left_bottom[0], apex[0]),(left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

color_thresholds = (image[:,:,0] < rgb_threshold[0]) | \
                    (image[:,:,1] < rgb_threshold[1]) | \
                   (image[:,:,2] < rgb_threshold[2])

#Find the region inside the lines
XX, YY = np.meshgrid(np.arange(0,xsize), np.arange(0,ysize))
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))

#mask color selection
color_select[color_thresholds] = [0,0,0]
line_image[~color_thresholds & region_thresholds] = [255,0,0]

#plt.subplot(1,3,1), plt.title('Original')
#plt.imshow(image)
#plt.subplot(1,3,2), plt.title('Color')
#plt.imshow(color_select)
#plt.subplot(1,3,3), plt.title('Region')
#plt.imshow(line_image)
#plt.show()


plt.imshow(image)
x = [left_bottom[0], right_bottom[0], apex[0], left_bottom[0]]
y = [left_bottom[1], right_bottom[1], apex[1], left_bottom[1]]
plt.plot(x, y, 'b--', lw=2)
plt.imshow(color_select)
plt.xticks([]), plt.yticks([])
plt.imshow(line_image)
plt.show()


