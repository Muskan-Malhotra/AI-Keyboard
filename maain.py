

import cv2
from time import sleep
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0) 

cap.set(3,1280) 

cap.set(4,720)   

# //detection confidence by default is 0.5 but we want the keys to be acurate
detector = HandDetector(detectionCon=0.8, maxHands=2)


keys = [["Q","W","E","R","T","Y","U","I","O","P"],
["A","S","D","F","G","H","J","K","L",";"],
["Z","X","C","V","B","N","M",",",".","/"]
]

# creating a class for all the buttons and their position on the keboard
def drawAll(img,buttonList):

  for button in buttonList:

    x,y = button.pos
    w,h = button.size
    cv2.rectangle(img,button.pos,(x+w,y+h),(255,0,255),cv2.FILLED)
    
    cv2.putText(img,button.text,(x+20,y+65)
    ,cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)

  return img


class Button():
  def __init__(self,pos,text,size=[85,85]):
    self.pos = pos
    self.size = size
    self.text = text

finalText = ""
buttonList=[]
for i in range(len(keys)):
    for j,key in enumerate(keys[i]):
      buttonList.append(Button([100 * j + 50,100 * i + 50],key))


while True:
  success, img = cap.read()
  img = detector.findHands(img)
  lmList, bboxInfo = detector.findPosition(img)
  img = drawAll(img,buttonList)

  
  if lmList:
    for button in buttonList:
      x, y = button.pos
      w, h = button.size

      
      if x<lmList[8][0]<x+w and y<lmList[8][1]<y+h:
        cv2.rectangle(img,button.pos,(x+w,y+h),(175,0,175),cv2.FILLED)
   
        cv2.putText(img,button.text,(x+20,y+65)
        ,cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)

        l, _, _ = detector.findDistance(8,12,img,draw=False) 
        print(l)

        
        if l<20:
          cv2.rectangle(img,button.pos,(x+w,y+h),(0,255,0),cv2.FILLED) 

          cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
          
          finalText += button.text
          sleep(0.15)

         
         

  cv2.rectangle(img,(50, 350),(700,450),(175,0,176),cv2.FILLED) 

  cv2.putText(img,finalText,(60,430)
  ,cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)

  
  
# for displaying the keyboard
  cv2.imshow("Image", img)
  cv2.waitKey(1)





