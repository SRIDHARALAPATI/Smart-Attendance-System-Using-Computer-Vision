import os
import cv2
import numpy as np
from PIL import Image
def trainingModule():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path='dataset'
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L');
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[0])
        faces.append(faceNp)
        print(ID)

        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    recognizer.train(faces,np.array(IDs))
    recognizer.write('recognizer/trainingData.yml')
    cv2.destroyAllWindows()