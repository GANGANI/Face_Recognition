import numpy as np
import cv2
                              
Face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
Eye = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

count=0                                                                 #initialize variables
arr=[]
arr1=[]
eyeDif=[]
LongH=0
SmallH=0

while count<100:                                                         #start to detect face and eyes      
    count+=1
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = Face.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:                                             #detecting face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = Eye.detectMultiScale(roi_gray)
        count2=0
        eye=[]
        
        for (ex,ey,ew,eh) in eyes:                                      #detecting eyes
            count2=count2+1
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            eye.append(ex+ew)
            
            if count2==2:                                               #check whether the both eyes are recognized
                eyeDif.append(eye[0]-ex)                        
                LongH=(y+h-ey-eh)                                       #detect the position of eye                                 
                SmallH=(y-ey)
                arr.append(LongH)
                arr1.append(SmallH)
                
    cv2.imshow('img',img)
    k = cv2.waitKey(2) & 0xff
    
    if k == 27:
        break
    if count==100:
        break
    
cap.release()
cv2.destroyAllWindows()
    
name = raw_input('Enter your name:')                                #Register user by name

Login= raw_input("Login or Register? :")                            #select login or registration

if (Login == "register" and arr!=[] and arr1!=[] and arr!=eyeDif):  #Login
    fout = open(name+'.txt', 'w+')                                  #registation details-write in a file
    fout.write(str(max(arr))+" ")               
    fout.write(str(max(arr1))+" ")
    fout.write(str(max(eyeDif)))
    fout.close()
    print ("\nSuccessfully registered")

    
if Login == "login":                                             #registration
        f = open(name+'.txt')                                       #registation details-read file   
        marytxt = f.read()             
        f.close()
        t=marytxt.split(" ")
        
        if(t[0]<max(arr)-5 and t[1]<max(arr1)-5 and t[2]<max(eyeDif) and arr!=[] and arr1!=[] and arr!=eyeDif):
        #check whether the gap between two eyes are less than recorded value and detect the position of eye by giving range
            print("Your face is successfully detected")

        else:
            print("Your face recognition is unsuccessful")
                  
