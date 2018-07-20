import cv2
brain_cascade = cv2.CascadeClassifier('brain_cascade.xml')
tumor_cascade = cv2.CascadeClassifier('tumor_cascade.xml')

def TakeSnapandSave():
    cap = cv2.VideoCapture(1)   #capture from external webcam 

    num = 0
    while num<1000:
        ret, img = cap.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        brains = brain_cascade.detectMultiScale(gray, 7, 7)
        for(x,y,w,h) in brains:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.rectangle(img,(x,y), (x+w,y+h),(255,255,0),5)
            tumors = tumor_cascade.detectMultiScale(gray, 2, 2)
            for (x,y,w,h) in tumors:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
                cv2.putText(img, 'Tumor',(x,y-50), font, 1.5, (0,255,255),5, cv2.LINE_AA)
                break
            break
        num = num+1
        cv2.imshow('img',img)
        cv2.waitKey(1000)
        cap.release()
        cv2.desrtoyAllWindows()
        
