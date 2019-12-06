from yolo import YOLO 
import cv2
import numpy as np
from PIL import Image
from timeit import time


####Read a video and perform yolo object detection/recognition

def main(yolo):

    
    video_capture = cv2.VideoCapture("./test.mp4")

    
        
    fps = 0.0
    while True:
        ret, frame = video_capture.read()  # frame shape 640*480*3
        if ret != True:
            break
        t1 = time.time()

       # image = Image.fromarray(frame)
        image = Image.fromarray(frame[...,::-1]) #bgr to rgb
        boxs = yolo.detect_image(image)

        for i in boxs:
        	#print(i)
        	xmin = i[0]
        	ymin = i[1]+i[3]
        	xmax = i[0]+i[2]
        	ymax = i[1]
        	cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)),(255,255,255), 2)
        	cv2.putText(frame, str(i[4]),(int(xmin), int(ymin)),0, 5e-3 * 200, (0,255,0),2)

   
   		
        cv2.imshow('', frame)
        
            
        fps  = ( fps + (1./(time.time()-t1)) ) / 2
        print("fps= %f"%(fps))
        
        # Press Q to stop!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    if writeVideo_flag:
        out.release()
        list_file.close()
    cv2.destroyAllWindows()


if __name__ == '__main__':
	main(YOLO())

cv2.waitKey(0)
cv2.destroyAllWindows()