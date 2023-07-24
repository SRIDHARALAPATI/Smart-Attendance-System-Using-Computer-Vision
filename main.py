# Welcome
# Project : Face recognition using opencv
    # Face Recognition
        # Dataset Creation (datasetCreator.py to create dataset of 1 person at a time)
        # Training
        # Recognition
    # introtopy.py is a sample script for detecting faces
import datasetCreator as d
import detector as det
import tkinter
import att


mywindow = tkinter.Tk()
mywindow.title("Smart Attendance System")
mywindow.configure(bg="white")

head = tkinter.Label(mywindow,text = "Attendance System Using Face Recognition", font= ("times new roman",20),bg="pink").grid(row=0,rowspan=3)

bt1 = tkinter.Button(mywindow,text = "Student Registration",command = d.datacreation,bg="indigo",fg = "white",height=2, font= ("times new roman",15) ).grid(row=3,padx=5,pady=5,sticky="nesw")
bt2 = tkinter.Button(mywindow,text = "Mark Attendance"     ,command = det.detection,bg="indigo",fg = "white",height=2, font= ("times new roman",15) ).grid(row=4,padx=5,pady=5,sticky ="nesw")
bt3 = tkinter.Button(mywindow,text = "Attendance Report"   ,command = att.report,bg="indigo",fg = "white",height=2, font= ("times new roman",15) ).grid(row=5,padx=5,pady=5,sticky ="nesw")

#bt4 = tkinter.Button(mywindow,text = "About the Developers",bg="lavender",fg = "black",height=2, font= ("times new roman",15) ).grid(row=6,padx=5,pady=5,sticky ="nesw")
#bt5 = tkinter.Button(mywindow,text = "Exit"                ,command = mywindow.destroy,bg="lavender",fg = "black",height=2, font= ("times new roman",15) ).grid(row=7,padx=5,pady=5,sticky ="nesw")

bt6 = tkinter.Button(mywindow,width=20, height=2,text="About",font= ("times new roman",15),bg="lavender",fg = "black").grid(row=8,column=0,sticky="nw",padx=10,pady=5)
bt7 = tkinter.Button(mywindow,width=20, height=2,text="Exit" ,font= ("times new roman",15),bg="lavender",fg = "black",command= mywindow.destroy).grid(row=8,column=0,sticky="ne" ,padx=10,pady=5)

mywindow.mainloop()