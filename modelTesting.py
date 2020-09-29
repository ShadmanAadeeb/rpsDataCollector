import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import keyboard
import numpy as np


from tensorflow.keras.models import load_model
 
print(tf.__version__) 
# load model
model = tf.keras.models.load_model('rpsmodel.h5')
# summarize model.
model.summary()


cap = cv2.VideoCapture(0)
x1=0
y1=0
x2=224
y2=224

width=650
height=650

predict=False
while(True):
    
    ret, frame = cap.read()
    frame=cv2.resize(frame,(650,650))
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
            x1=width-224
            x2=width
    #moving the box up
    if keyboard.is_pressed('w'):
        y1=y1-5
        y2=y2-5
        if y1<0:
            y1=0
            y2=224
    #moving the box down
    if keyboard.is_pressed('s'):
        y1=y1+5
        y2=y2+5
        if y2>height:
            y1=height-224
            y2=height        
    frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 1) 
    ##########################BOX MOVEMENT CODE ENDS###############################
    

    ###################################PREDICTION CODE STARTS############################
    if keyboard.is_pressed('p'):
        if predict==True:
            predict=False
        else:
            predict=True
        

    if predict==True:
        frame=cv2.putText(frame,'Prediction mode',(width-250,30),cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255),2)
        img=frame[y1:y2,x1:x2]
        img=img.reshape(1,224,224,3)
        img=img/255
        y=model.predict(img)
        if(np.argmax(y)==0):
            frame=cv2.putText(frame,'Paper',(width-250,60),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0 ),5)
        elif(np.argmax(y)==1):
            frame=cv2.putText(frame,'Rock',(width-250,60),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0 ),5)
        elif(np.argmax(y)==2):
            frame=cv2.putText(frame,'Scissors',(width-250,60),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0 ),5)
    ###################################PREDICTION CODE ENDS############################
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

