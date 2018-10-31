import cv2
import numpy as np
import sys

def raw_voronoi(img):
    print 'Step 3. drawing voronoi graph\n'
    print 'drawing voronoi graph ...'
    copy_img = np.zeros((len(img),len(img[3])-1,3),np.float64)
    for y in range(1,len(img)-1):
        for x in range(1,len(img[y])-1):
            count=0
            if img[y,x]>=img[y,x+1]:
                count=count+1
            if img[y,x]>=img[y+1,x+1]:
                count=count+1
            if img[y,x]>=img[y+1,x]:
                count=count+1
            if img[y,x]>=img[y+1,x-1]:
                count=count+1
            if img[y,x]>=img[y,x-1]:
                count=count+1
            if img[y,x]>=img[y-1,x-1]:
                count=count+1
            if img[y,x]>=img[y-1,x]:
                count=count+1
            if img[y,x]>=img[y-1,x+1]:
                count=count+1
        
        
            if count>=7:
                copy_img[y,x]=(0,0,255)
            elif img[y,x]==0:
                copy_img[y,x]=(0,0,0)
            else:
                copy_img[y,x]=(255,255,255)
    print '\ndone'

    cv2.imshow('voronoi',copy_img)
    cv2.waitKey(0)
    cv2.imwrite('voronoi_'+sys.argv[1], copy_img)
    print 'image saved\n'
    return copy_img