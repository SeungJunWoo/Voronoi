import cv2
import numpy as np
import sys
import Brushfire
import img_to_binary
import brushfire_to_voronoi
import voronoi_correction

if __name__=='__main__':
    if len(sys.argv)==1:
        print 'Usage: python main.py {file name}'
    else:
        t=img_to_binary.Thresh()
        img=t.thresh_show()
        brush=Brushfire.brushfire(img)
        voronoi=brushfire_to_voronoi.raw_voronoi(brush)
        red=voronoi_correction.redwall_del(voronoi)
        detect,arrow=voronoi_correction.unlinked_edge_find(red)
        voronoi_correction.unlinked_edge_draw(detect,arrow)


    