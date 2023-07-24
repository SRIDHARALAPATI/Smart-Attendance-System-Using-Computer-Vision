import cv2
import sqlite3
import openpyxl
import numpy as np



def getProfile(id):
    conn=sqlite3.connect("studentDb")
    cmd="select * from student where ID="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

def detection():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    vid=cv2.VideoCapture(0);
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read("recognizer\\trainingData.yml")
    id=0
#font = cv2.FONT_HERSHEY_SIMPLEX
#font=cv2.cv.InitFont(cv2.cv.CV_FONT_COMPLEX_SMALL,5,1,0,4)
    while(True):
        ret,img=vid.read();
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
    #cv2.imshow(“Face”, img)

        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            id, conf = rec.predict(gray[y:y + h, x:x + w]) # prediction confidence , getting id
            profile=getProfile(id)
            if(profile!=None):
                cv2.putText(img, "ID:"+str(profile[0]), (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
                cv2.putText(img, "Name:"+str(profile[1]), (x, y+h+60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
                cv2.putText(img, "Dept:"+str(profile[2]), (x, y+h+90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
                cv2.putText(img, "Gender:"+str(profile[3]), (x, y+h+120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
        cv2.imshow("Face",img)
        if(cv2.waitKey(1) == ord('q')):
            break;
    wb = openpyxl.load_workbook('attendance.xlsx')
    sheet = wb.get_sheet_by_name('Sheet1')
    for cellObj in list(sheet.columns)[0]:
        if (cellObj.value == id):
            sheet['B'+str(cellObj.row)]=1
        wb.save('attendance.xlsx')

    vid.release()
    cv2.destroyAllWindows()
#detection()