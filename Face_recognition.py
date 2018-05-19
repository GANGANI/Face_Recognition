import numpy as np
import cv2

name = raw_input('Enter your name:')
if name != "":
    Login= raw_input("Login or Register : ")
    if Login == "1":
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

            eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

            cap = cv2.VideoCapture(0)
            n=0
            arr=[]
            arr1=[]
            eyeDif=[]
            LongH=0
            SmallH=0
            while n<50:
                
                n+=1
                ret, img = cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                for (x,y,w,h) in faces:
                    print x,y,w,h
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = img[y:y+h, x:x+w]
                    
                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    m=0
                    eye=[]
                    for (ex,ey,ew,eh) in eyes:
                        m=m+1
                        print "eye",m,ex,ey,ew,eh
                        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                        eye.append(ex+ew)
                        if m==2:
                            eyeDif.append(eye[0]-ex)
                            LongH=(y+h-ey-eh)
                            SmallH=(y-ey)
                            arr.append(LongH)
                            arr1.append(SmallH)
                            print LongH,SmallH, max(arr),max(arr1),min(eyeDif)       
                cv2.imshow('img',img)
                k = cv2.waitKey(2) & 0xff
                if k == 27:
                    break
                if n==50:
                    break

            print "minmax",max(arr),max(arr1),min(eyeDif)
            fout = open('.txt', 'w+')
            fout.write(str(max(arr))+"\n")               
            fout.write(str(max(arr1))+"\n")
            fout.write(str(max(eyeDif)))
            fout.close()
            cap.release()
            cv2.destroyAllWindows()
    if Login == "2":
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

        cap = cv2.VideoCapture(0)
        n=0
        arr=[]
        arr1=[]
        eyeDif=[]
        LongH=0
        SmallH=0
        while n<50:
            
            n+=1
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:
                print x,y,w,h
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                
                eyes = eye_cascade.detectMultiScale(roi_gray)
                m=0
                eye=[]
                for (ex,ey,ew,eh) in eyes:
                    m=m+1
                    print "eye",m,ex,ey,ew,eh
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    eye.append(ex+ew)
                    if m==2:
                        eyeDif.append(eye[0]-ex)
                        LongH=(y+h-ey-eh)
                        SmallH=(y-ey)
                        arr.append(LongH)
                        arr1.append(SmallH)
                        print LongH,SmallH, max(arr),max(arr1),min(eyeDif)       
            cv2.imshow('img',img)
            k = cv2.waitKey(2) & 0xff
            if k == 27:
                break
            if n==50:
                break

        print "minmax",max(arr),max(arr1),min(eyeDif)
        f = open(name+'.txt')
        marytxt = f.read()             
        f.close()
        t=marytxt.split(" ")
        if(t[0]<max(arr) and t[1]<max(arr1) and t[2]<max(eyeDif) and arr!=[] and arr1!=[] and arr!=eyeDif):
            print("Your face is successfully detected")
        else:
            print("Your face detection is unsuccessful")
        cap.release()
        cv2.destroyAllWindows()

else:
    print("Invalid user")
        
        
