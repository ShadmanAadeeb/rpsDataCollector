import cv2
import keyboard
import os

#Making the dynamic rectangle parameters
x1=0
y1=0
x2=250
y2=250

width=650
height=650

cap = cv2.VideoCapture(0)

#0 for rock
#1 for paper
#2 for scissors
gesture=0

record=False
typeOfGesture=0

rockCounter=len(os.listdir('./rock'))
paperCounter=len(os.listdir('./paper'))
scissorCounter=len(os.listdir('./scissors'))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame=cv2.resize(frame,(width,height))
    frame = cv2.flip(frame,1)
    
    ##########################BOX MOVEMENT CODE STARTS###############################
    #moving the box left
    if keyboard.is_pressed('a'):
        x1=x1-5
        x2=x2-5
        if x1<0:
            x1=0
            x2=250
    #moving the box right
    if keyboard.is_pressed('d'):
        x1=x1+5
        x2=x2+5
        if x2>width:
            x1=width-250
            x2=width
    #moving the box up
    if keyboard.is_pressed('w'):
        y1=y1-5
        y2=y2-5
        if y1<0:
            y1=0
            y2=250
    #moving the box down
    if keyboard.is_pressed('s'):
        y1=y1+5
        y2=y2+5
        if y2>height:
            y1=height-250
            y2=height        
    ##########################BOX MOVEMENT CODE ENDS###############################
    
    ########################## GESTURE SELECTION CODE STARTS ###############################
    if keyboard.is_pressed('0'):
        typeOfGesture=0
        
    elif keyboard.is_pressed('1'):
        typeOfGesture=1 
        
    elif keyboard.is_pressed('2'):
        typeOfGesture=2
        
    elif keyboard.is_pressed('3'):
        typeOfGesture=3
        
    
    
    
    if typeOfGesture==0:
        #typeOfGesture=0
        frame=cv2.putText(frame,'Gesture : None',(width-250,30),cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255),2)
    elif typeOfGesture==1:
        #typeOfGesture=1 
        frame=cv2.putText(frame,'Gesture : Rock',(width-250,30),cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255),2)
    elif typeOfGesture==2:
        #typeOfGesture=2
        frame=cv2.putText(frame,'Gesture : Paper',(width-250,30),cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255),2)
    elif typeOfGesture==3:
        #typeOfGesture=3
        frame=cv2.putText(frame,'Gesture : Scissors',(width-250,30),cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255),2)


    ########################## GESTURE SELECTION CODE ENDS ###############################

    #start recording
    if keyboard.is_pressed('r'):
        record=True
        
    #stop recording
    if keyboard.is_pressed('p'):
        record=False

    
    frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 1) 

    if record==False:
        frame=cv2.putText(frame,'Not Recording',(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255),2)
    else:
        frame=cv2.putText(frame,'Recording',(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255),2)
        if typeOfGesture==0:
            pass
        elif typeOfGesture==1:            
            rockImage=frame[y1:y2,x1:x2]            
            cv2.imwrite('./rock/'+str(rockCounter)+'.jpg',rockImage)
            rockCounter=rockCounter+1
            frame=cv2.putText(frame,str(rockCounter),(width-250,50),cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255),2)
        elif typeOfGesture==2:
            paperImage=frame[y1:y2,x1:x2]
            cv2.imwrite('./paper/'+str(paperCounter)+'.jpg',paperImage)
            paperCounter=paperCounter+1
            frame=cv2.putText(frame,str(paperCounter),(width-250,50),cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255),2)
        elif typeOfGesture==3:
            scissorsImage=frame[y1:y2,x1:x2]
            cv2.imwrite('./scissors/'+str(scissorCounter)+'.jpg',scissorsImage)
            scissorCounter=scissorCounter+1
            frame=cv2.putText(frame,str(scissorCounter),(width-250,50),cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255),2)
    # Our operations on the frame come here
    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()