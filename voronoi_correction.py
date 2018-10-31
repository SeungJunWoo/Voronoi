import cv2
import numpy as np
import sys


def redwall_del(img):
    print 'Step 4. removing redwall\n'
    copy_img = np.zeros((len(img),len(img[3])-1,3),np.float64)

    for y in range(1,len(img)-1):
        for x in range(1,len(img[y])-1):
            count=0
            count_w=0
            if img[y,x+1][0]==0 and img[y,x+1][1]==0 and img[y,x+1][2]==0:
                count=count+1
            if img[y+1,x+1][0]==0 and img[y+1,x+1][1]==0 and img[y+1,x+1][2]==0:
                count=count+1
            if img[y+1,x][0]==0 and img[y+1,x][1]==0 and img[y+1,x][2]==0:
                count=count+1
            if img[y+1,x-1][0]==0 and img[y+1,x-1][1]==0 and img[y+1,x-1][2]==0:
                count=count+1
            if img[y,x-1][0]==0 and img[y,x-1][1]==0 and img[y,x-1][2]==0:
                count=count+1
            if img[y-1,x-1][0]==0 and img[y-1,x-1][1]==0 and img[y-1,x-1][2]==0:
                count=count+1
            if img[y-1,x][0]==0 and img[y-1,x][1]==0 and img[y-1,x][2]==0:
                count=count+1
            if img[y-1,x+1][0]==0 and img[y-1,x+1][1]==0 and img[y-1,x+1][2]==0:
                count=count+1

            if img[y,x+1][0]==255 and img[y,x+1][1]==255:
                count_w=count_w+1
            if img[y+1,x+1][0]==255 and img[y+1,x+1][1]==255:
                count_w=count_w+1
            if img[y+1,x][0]==255 and img[y+1,x][1]==255:
                count_w=count_w+1
            if img[y+1,x-1][0]==255 and img[y+1,x-1][1]==255:
                count_w=count_w+1
            if img[y,x-1][0]==255 and img[y,x-1][1]==255:
                count_w=count_w+1
            if img[y-1,x-1][0]==255 and img[y-1,x-1][1]==255:
                count_w=count_w+1
            if img[y-1,x][0]==255 and img[y-1,x][1]==255:
                count_w=count_w+1
            if img[y-1,x+1][0]==255 and img[y-1,x+1][1]==255:
                count_w=count_w+1
        

            if count_w<=0 and img[y,x][0]==0 and img[y,x][2]==255:
                copy_img[y,x]=(0,0,0)
            elif count>=1 and count_w<=3 and img[y,x][0]==0 and img[y,x][2]==255:
                copy_img[y,x]=(0,0,0)
            elif img[y,x][0]==0 and img[y,x][1]==0 and img[y,x][2]==0:
                copy_img[y,x]=(0,0,0)
            elif img[y,x][0]==0 and img[y,x][1]==0 and img[y,x][2]==255:
                copy_img[y,x]=(0,0,255)
            else:
                copy_img[y,x]=(255,255,255)

    cv2.imshow('voronoi_redwall removed',copy_img)
    cv2.waitKey(0)
    cv2.imwrite('voronoi_redwallremoved_'+sys.argv[1], copy_img)
    print 'image saved\n'
    return copy_img

def unlinked_edge_find(img):
    print 'Step 5. finding unlinked edges\n'
    copy_img = img

    arrow=[]

    for y in range(2,len(img)-1):
        for x in range(2,len(img[y])-1):
            #red
            if img[y,x][0]==0 and img[y,x][1]==0 and img[y,x][2]==255:
                #no black
                if not ((img[y-1,x-1][0]==0 and img[y-1,x-1][2]==0) or
                        (img[y-1,x][0]==0 and img[y-1,x][2]==0) or
                        (img[y-1,x+1][0]==0 and img[y-1,x+1][2]==0) or
                        (img[y,x-1][0]==0 and img[y,x-1][2]==0) or
                        (img[y,x+1][0]==0 and img[y,x+1][2]==0) or
                        (img[y+1,x-1][0]==0 and img[y+1,x-1][2]==0) or
                        (img[y+1,x][0]==0 and img[y+1,x][2]==0) or
                        (img[y+1,x+1][0]==0 and img[y+1,x+1][2]==0)):

                    # _______
                    # |1|2|3|
                    # |8| |4|
                    # |7|6|5| 

                    #1
                    if not (((img[y-1,x-1][0]==0 and img[y-1,x-1][2]==255) and 
                    ((img[y,x+1][0]==0 and img[y,x+1][2]==255) or 
                    (img[y+1,x+1][0]==0 and img[y+1,x+1][2]==255) or 
                    (img[y+1,x][0]==0 and img[y+1,x][2]==255)))

                    #2
                    or ((img[y-1,x][0]==0 and img[y-1,x][2]==255) and 
                    ((img[y+1,x+1][0]==0 and img[y+1,x+1][2]==255) or 
                    (img[y+1,x][0]==0 and img[y+1,x][2]==255) or 
                    (img[y+1,x-1][0]==0 and img[y+1,x-1][2]==255)))

                    #3
                    or ((img[y-1,x+1][0]==0 and img[y-1,x+1][2]==255) and 
                    ((img[y+1,x][0]==0 and img[y+1,x][2]==255) or 
                    (img[y+1,x-1][0]==0 and img[y+1,x-1][2]==255) or 
                    (img[y,x-1][0]==0 and img[y,x-1][2]==255)))

                    #4
                    or ((img[y,x+1][0]==0 and img[y,x+1][2]==255) and 
                    ((img[y+1,x-1][0]==0 and img[y+1,x-1][2]==255) or 
                    (img[y,x-1][0]==0 and img[y,x-1][2]==255) or 
                    (img[y-1,x-1][0]==0 and img[y-1,x-1][2]==255)))

                    #5
                    or ((img[y+1,x+1][0]==0 and img[y+1,x+1][2]==255) and 
                    ((img[y,x-1][0]==0 and img[y,x-1][2]==255) or 
                    (img[y-1,x-1][0]==0 and img[y-1,x-1][2]==255) or 
                    (img[y-1,x][0]==0 and img[y-1,x][2]==255)))

                    #6
                    or ((img[y+1,x][0]==0 and img[y+1,x][2]==255) and 
                    ((img[y-1,x-1][0]==0 and img[y-1,x-1][2]==255) or 
                    (img[y-1,x][0]==0 and img[y-1,x][2]==255) or 
                    (img[y-1,x+1][0]==0 and img[y-1,x+1][2]==255)))

                    #7
                    or ((img[y+1,x-1][0]==0 and img[y+1,x-1][2]==255) and 
                    ((img[y-1,x][0]==0 and img[y-1,x][2]==255) or 
                    (img[y-1,x+1][0]==0 and img[y-1,x+1][2]==255) or 
                    (img[y,x+1][0]==0 and img[y,x+1][2]==255)))

                    #8
                    or ((img[y,x-1][0]==0 and img[y,x-1][2]==255) and 
                    ((img[y-1,x+1][0]==0 and img[y-1,x+1][2]==255) or 
                    (img[y,x+1][0]==0 and img[y,x+1][2]==255) or 
                    (img[y+1,x+1][0]==0 and img[y+1,x+1][2]==255)))):

                        #copy_img[y,x]=(255,0,0)
                        arrow.append([y,x])
    print 'unlinked edges detected\n'
    return copy_img,arrow

def unlinked_edge_draw(img,arrow):
    print 'Step 6. drawing unlinked nodes\n'
    copy_img=img
    for a in arrow:
        if ((img[a[0]-1,a[1]-1][0]==0 and img[a[0]-1,a[1]-1][2]==255)
        and (img[a[0]-1,a[1]+1][0]==0 and img[a[0]-1,a[1]+1][2]==255)):
        
            i=1
            copy_img[a[0],a[1]]=(255,0,0)
            while (img[a[0]+i,a[1]][0]==255 and img[a[0]+i,a[1]][2]==255):
                copy_img[a[0]+i,a[1]]=[255,0,0]
                i=i+1

        elif ((img[a[0]+1,a[1]+1][0]==0 and img[a[0]+1,a[1]+1][2]==255)
        and (img[a[0]-1,a[1]+1][0]==0 and img[a[0]-1,a[1]+1][2]==255)):

            i=1
            copy_img[a[0],a[1]]=(255,0,0)
            while (img[a[0],a[1]-i][0]==255 and img[a[0],a[1]-i][2]==255):
                copy_img[a[0],a[1]-i]=[255,0,0]
                i=i+1

        elif ((img[a[0]+1,a[1]+1][0]==0 and img[a[0]+1,a[1]+1][2]==255)
        and (img[a[0]+1,a[1]-1][0]==0 and img[a[0]+1,a[1]-1][2]==255)):

            i=1
            copy_img[a[0],a[1]]=(255,0,0)
            while (img[a[0]-i,a[1]][0]==255 and img[a[0]-i,a[1]][2]==255):
                copy_img[a[0]-i,a[1]]=[255,0,0]
                i=i+1

        elif ((img[a[0]+1,a[1]-1][0]==0 and img[a[0]+1,a[1]-1][2]==255)
        and (img[a[0]-1,a[1]-1][0]==0 and img[a[0]-1,a[1]-1][2]==255)):

            i=1
            copy_img[a[0],a[1]]=(255,0,0)
            while (img[a[0],a[1]+i][0]==255 and img[a[0],a[1]+i][2]==255):
                copy_img[a[0],a[1]+i]=[255,0,0]
                i=i+1

    cv2.imshow('voronoi_correction',copy_img)
    cv2.waitKey(0)
    cv2.imwrite('voronoi_final_'+sys.argv[1], copy_img)
    print 'image saved'