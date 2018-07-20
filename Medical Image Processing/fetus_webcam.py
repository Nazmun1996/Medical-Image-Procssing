import cv2
fetus_cascade = cv2.CascadeClassifier('fetus_cascade.xml')

def TakeSnapandSave():
    cap = cv2.VideoCapture(1)   #capture from external webcam 

    num = 0
    while num<1000:
        ret, img = cap.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        fet = fetus_cascade.detectMultiScale(gray, 7, 7)
        for(x,y,w,h) in fet:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.rectangle(img,(x,y), (x+w,y+h),(255,255,0),5)
            break
        num = num+1
        cv2.imshow('img',img)
        cv2.waitKey(1000)
        cap.release()
        cv2.desrtoyAllWindows()
        
