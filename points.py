

# importing the module 
import cv2
import math
   
# function to display the coordinates of 
# of the points clicked on the image 
coord=[]
def click_event(event, x, y, flags, params): 
  
    # checking for left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN: 
  
        # displaying the coordinates 
        # on the Shell 
        
        #print(x, ' ', y)
        coord.append([x,y])
  
        # displaying the coordinates 
        # on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font, 
                    1, (0, 0, 255), 2) 
        cv2.imshow('image', img)
  
    # checking for right mouse clicks      
    if event==cv2.EVENT_RBUTTONDOWN: 
        pass
        """
        # displaying the coordinates 
        # on the Shell 
        #print(x, ' ', y) 
  
        # displaying the coordinates 
        # on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        b = img[y, x, 0] 
        g = img[y, x, 1] 
        r = img[y, x, 2] 
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r), 
                    (x,y), font, 1, 
                    (0, 0, 255), 1) 
        cv2.imshow('image', img) """
center_coord = []
def click_event2(event, x, y, flags, params): 
  
    # checking for left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN: 
  
        # displaying the coordinates 
        # on the Shell 
        
        #print(x, ' ', y)
        center_coord.append([x,y])
  
        # displaying the coordinates 
        # on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font, 
                    1, (0, 0, 0), 1) 
        cv2.imshow('image', img)
  
    # checking for right mouse clicks      
    if event==cv2.EVENT_RBUTTONDOWN: 
        pass


# driver function 
if __name__=="__main__": 
  
    # reading the image 
    img = cv2.imread('mititoyosimpla.jpg', 1) 
  
    # displaying the image 
    cv2.imshow('image', img) 
  
    # setting mouse handler for the image 
    # and calling the click_event() function 
    cv2.setMouseCallback('image', click_event) 
  
    # wait for a key to be pressed to exit 
    cv2.waitKey(0) 
  
    # close the window
    cv2.destroyAllWindows()
    print('coordinates: ',coord)
    coord_x=[]
    for c in coord:
        coord_x.append(c[0])
    center_x=coord_x[:-1]
    coord_x.pop()
    print('coord_x: ',coord_x)
    print('average_x: ',math.ceil(sum(coord_x)/(len(coord_x))))
    avg_x=(math.ceil(sum(coord_x)/(len(coord_x))))

    coord_y=[]
    for c in coord:
        coord_y.append(c[1])
    center_y=coord_y[:-1]
    coord_y.pop()
    print('coord_y: ',coord_y)
    print('average_y: ',math.ceil(sum(coord_y)/(len(coord_y))))
    avg_y=(math.ceil(sum(coord_y)/(len(coord_y))))
    
    center = [avg_x,avg_y]
    print('center: ',center)
     
    cv2.destroyAllWindows()

    cv2.drawMarker(img, center, (0,0,255), 2,7,7,1)

    cv2.imshow('image', img)

    cv2.waitKey(0) 
  
    # close the window
    cv2.destroyAllWindows()
    #print(coord)
    #cv2.circle()