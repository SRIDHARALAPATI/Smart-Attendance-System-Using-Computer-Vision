import cv2
import sqlite3
import trainer as t
import openpyxl
import numpy as np

def insertOrUpdate(id,name,Dept,gender):
    conn = sqlite3.connect("studentDb")
    cmd ="select * from student where ID="+str(id)
    cursor = conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd = "update student set Name=" + str(name)+"where ID="+str(id)

    else:
        cmd = "insert into student(ID,Name,Department,Gender) Values("+str(id)+",'"+str(name)+"','"+str(Dept)+"','"+str(gender)+"')"
    conn.execute(cmd)
    conn.commit()
    conn.close()

# creating a dataset dynamically for 1 person
# or start with a static set and add dynamically
    # in that case keep in mind of the id's

def datacreation():
    facedetectcascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    vid = cv2.VideoCapture(0)

    id= input("Enter the id ")
    name = input("Enter your Name")
    Dept = input("Enter your Department Name")
    gender = input("Enter you Gender:")
    insertOrUpdate(id,name,Dept, gender)
    sno=0 #sample number for a given id
    wb = openpyxl.load_workbook('attendance.xlsx')
    sheet = wb.get_sheet_by_name('Sheet1')
    sheet['A' + str(sheet.max_row + 1)] = int(id)
    wb.save('attendance.xlsx')
    while True:
        check, frame = vid.read();
        # for classifier we need gray scale image
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facedetectcascade.detectMultiScale(gray_frame, 1.05, 5)
        cv2.imshow("Face Detection", frame)
        key = cv2.waitKey(100)

        for x, y, w, h in faces:
            # after a face is detected, we store it
            sno = sno + 1
            cv2.imwrite("dataset/"+str(id)+"."+str(sno)+".jpg", gray_frame[y:y+h,x:x+w])
            # or store entire frame in dataset as frame in imwrite( ,frame)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)  # here pass color image i.e., frame
            # since gray is needed only for cascade classifier
            cv2.waitKey(1000) # giving 1 sec time for the person to change expression for dataset creation
        #cv2.imshow("Face Detection", frame)
        #key = cv2.waitKey(100)
        #if (key == ord("q")):
            #break
        # to get out of loop we dont need infinite loop but only a few samples for recognizing a person.. So..
        if(sno==10):
            break
    vid.release()
    #cv2.destroyAllWindows()
    cv2.destroyWindow("Face Detection")
    t.trainingModule()
#datacreation()