import cv2
import numpy as np

def find_Target(img_name):
   ballFound = False

   img = cv2.imread(img_name,1)
   img = cv2.resize(img,(0,0),fx=.25, fy=.25)

   # Split the image into 3 channels: b,g,r to view them individually
   # We then want to search for white spots in a channel,
   # since this will represent more 'pure' colors of the color channel.
   # For example, a white spot on the red color channel is a signifier of there
   # being an object that is very close to pure red.

   b,g,r = cv2.split(img)

   # Threshold the image, keeping frames that are closer to white (a value of 255)
   # Thresholding the individual color channel allows us to cut out anything below
   # a specific value on the grayscale spectrum.
   ret,blue_thresh = cv2.threshold(b,155,255,cv2.THRESH_BINARY_INV)
   ret,red_thresh = cv2.threshold(r,190,255,cv2.THRESH_BINARY)
   ret,green_thresh = cv2.threshold(g,155,255,cv2.THRESH_BINARY)

   masked = red_thresh-green_thresh

   # Apply a Guassian Blur to smooth out the edges of the image
   #blur = cv2.GaussianBlur(red_thresh,(7,7),8,8)
   masked = cv2.bitwise_not(masked)

   circles = cv2.HoughCircles(masked,cv2.HOUGH_GRADIENT,2.0,masked.shape[0]/2,
                               param1=100,param2=10,minRadius=0,maxRadius=30)
   #TODO: either have radius change based on elevation of drone or look for concentric circles instead

   # return empty list if no POI found
   if circles is None:
      print("no Target!")
      return []

   circles = np.uint16(np.around(circles))
   for i in circles[0,:]:
       # draw the outer circle
       cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
       # draw the center of the circle
       cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

   # create a list of locations not including radii:
   return_list = circles.tolist()
   #for loc in return_list:
      #del loc[2]   

   #show images
   cv2.imshow('mask red-green',masked)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

   cv2.imshow('detected circles',img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

   print("Target found:",  return_list)
   return return_list[0]
