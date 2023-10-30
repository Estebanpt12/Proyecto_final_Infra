import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import urllib.request
import time
from utilities.encription import decrypt_text
 
#cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
 
url='http://192.168.1.2/'
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
 
prev=""
pres=""
action=False
message=True
while True:
    img_resp=urllib.request.urlopen(url+'cam-hi.jpg')
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgnp,-1)
    #_, frame = cap.read()
    if not message and action:
        message=True
        time.sleep(2)

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        pres=obj.data
        if prev == pres:
            pass
        else:
            print("Type:",obj.type)
            print("Data: ",str(obj.data.decode('utf-8')))
            prev=pres
            action=False
        cv2.putText(frame, str(obj.data.decode('utf-8')), (50, 50), font, 2,
                    (255, 0, 0), 3)
 
    cv2.imshow("live transmission", frame)
 
    key = cv2.waitKey(1)
    if key == 13 and not action:
        ##Calldb
        cv2.putText(frame, decrypt_text(str(obj.data.decode('utf-8'))), (50, 50), font, 2,
                    (0, 0, 255), 3)
        cv2.imshow("live transmission", frame)
        print("Enter pressed")
        message = False
        action = True
    
    key = cv2.waitKey(1)
    if key == 27:
        break
 
cv2.destroyAllWindows()