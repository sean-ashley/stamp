#code inspired by https://medium.com/datadriveninvestor/video-streaming-using-flask-and-opencv-c464bf8473d6
import face_recognition
import cv2
#define camera class
class Camera(object):

    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        #releasing camera
        self.video.release()


    #function that 
    def extract_frames(self):

        # Grab a single frame of video
        ret, frame = self.video.read()


        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame,model="cnn")

        #loop thru the face locations and make rectangles
        for (top, right, bottom, left) in face_locations:
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, "Loser" ,  (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


        #convert the frame into a jpeg file
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def is_user_on_screen(self):
                #declare livestream
        """ Checks whether or not a user is on the screen"""


        # Grab a single frame of video
        ret, frame = self.video.read()


        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame,model="cnn")

        #if they are not on the screen return false
        if not face_locations:
            return False
        
        #otherwise return true
        return True
        





