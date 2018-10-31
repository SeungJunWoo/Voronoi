import cv2
import numpy as np
import sys

def brushfire(img):
    print 'Step 2. Brushfire\n'
    print 'brushfire processing... this might take a while'
    for k in range(0,150,3):
        for y in range(1,len(img)-1):
            for x in range(1,len(img[y])-1):
                if img[y,x]==255 and (img[y,x+1]==k or img[y+1,x+1]==k or 
                img[y+1,x]==k or img[y+1,x-1]==k or img[y,x-1]==k or 
                img[y-1,x-1]==k or img[y-1,x]==k or img[y-1,x+1]==k):
                    img[y,x]=k+3
    print "\ndone press any key"
    cv2.imshow('brushfire',img)
    cv2.waitKey(0)
    cv2.imwrite('brushfire_'+sys.argv[1], img)
    print 'image saved\n'

    return img
