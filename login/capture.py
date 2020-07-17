from os import walk
class capture:
    
    def __init__(self):
        self.knownPath = 'login/static/faces'
        
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
        f = self.getKnownFiles()
        # print("KnownImages",f)
        video_capture = cv2.VideoCapture(0)

        # Create arrays of known face encodings and their names
        known_face_encodings =[]
        known_face_names = []

        # get the Known Face Encodings
        for img in f:
            name = img.split('.')[0]
            print(img)
            face = face_recognition.load_image_file(img)
            faceEnc = face_recognition.face_encodings(face)[0]
            known_face_encodings.append(faceEnc)
            known_face_names.append(name.split("/")[-1])

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

        print(face_names)
        retVal = "Unknown"
        for name in face_names:
            if name!="Unknown":
                retVal = name
                break
        return retVal