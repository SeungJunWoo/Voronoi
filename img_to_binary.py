import cv2
import numpy as np
import sys

class Thresh:
    def thresh_show(self):
        self.key=0
        self.i=0 
        print '\nStep 1. Changing original image to binary image\n'
        print 'press [u] or [d] to increase or decrease the threshhold value'
        print 'press [s] to save the image'   
        while(self.key!=ord('s')):
            img=self.thresh_control()
            cv2.imshow('binary image',img)
            self.key=cv2.waitKey(0)
        strthr=`self.thresh`
        cv2.imwrite('binary_'+strthr+'_'+sys.argv[1], img)
        print 'image saved\n'
        return img
            

    def thresh_control(self):
        img_name=sys.argv[1]
        image = cv2.imread('map/'+img_name,0)
        if self.key==ord('u'):
            self.i=self.i+1
        elif self.key==ord('d'):
            self.i=self.i-1
        
        self.thresh=180+self.i
        print 'threshhold value: ' ,self.thresh
        ret,thresh_img = cv2.threshold(image,180+self.i,255,cv2.THRESH_BINARY)

        return thresh_img

if __name__=='__main__':
    t=Thresh()
    t.thresh_show()

