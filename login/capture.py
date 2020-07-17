from os import walk
from PIL import Image
import requests
from io import BytesIO

class capture:
    
    def __init__(self):
        self.knownPath = 'login/static/faces'
        self.images = [
            'https://firebasestorage.googleapis.com/v0/b/numbergame-8d811.appspot.com/o/Akansha_Singh_1701003.jpg?alt=media&token=ab43f7b9-7d98-45a6-9505-c0422ae38513',
            'https://firebasestorage.googleapis.com/v0/b/numbergame-8d811.appspot.com/o/Anivrat_Goel_1701000.jpg?alt=media&token=69d33273-efca-4e42-a69c-e4e5c0a0fa48',
            'https://firebasestorage.googleapis.com/v0/b/numbergame-8d811.appspot.com/o/Monisha_Ranjan_1701037.jpg?alt=media&token=8c116208-5b43-48f5-8f46-543cb46757e3',
            'https://firebasestorage.googleapis.com/v0/b/numbergame-8d811.appspot.com/o/Sahil_Kalamkar_1701070.jpg?alt=media&token=ec332f10-54f5-4308-b1d9-c4e5c074b133',
            'https://firebasestorage.googleapis.com/v0/b/numbergame-8d811.appspot.com/o/Praveen_Kumar_1601041.jpg?alt=media&token=297a542e-5c46-4371-b2d7-19c03dcdf9ea'
        ]
        self.names = [
            'Akansha_Singh_1701003','Anivrat_Goel_1701000','Monisha_Ranjan_1701037','Sahil_Kalamkar_1701070','Praveen_Kumar_1601041'
        ]

    def getKnownFiles(self):
        f = []
        for (dirpath, dirnames, filenames) in walk(self.knownPath):
            for file in filenames:
                # print(file)
                fullPath = self.knownPath+"/"+file
                # print(fullPath)
                f.append(fullPath)
        
        return f
    
    def process(self):
        import face_recognition
        import cv2
        import numpy as np
        f = self.images
        # print("KnownImages",f)
        video_capture = cv2.VideoCapture(0)

        # Create arrays of known face encodings and their names
        known_face_encodings =[]
        known_face_names = self.names

        # get the Known Face Encodings
        for url in f:
            response = requests.get(url)
            print(response)
            img = BytesIO(response.content)
            print(img)
            face = face_recognition.load_image_file(img)
            faceEnc = face_recognition.face_encodings(face)[0]
            known_face_encodings.append(faceEnc)
            

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        capturesFrames = []
        c = 0
        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()
            
            if frame is not None:
                # print("Frame CAP")
                # Resize frame of video to 1/4 size for faster face recognition processing
                small_frame = cv2.resize(frame, None, fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1]

                capturesFrames.append(rgb_small_frame)
            c += 1
            if c>100:
                break
        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

        for img in capturesFrames:
        
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(img)
            face_encodings = face_recognition.face_encodings(img, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = -1
                if len(face_distances):
                    best_match_index = np.argmin(face_distances)
                if best_match_index!=-1 and matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        
        retVal = "Unknown"
        for name in face_names:
            if name!="Unknown":
                retVal = name
                break
        return retVal