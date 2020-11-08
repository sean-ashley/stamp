#proof of concept code , adapted from https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py#L60




def capture():
    import face_recognition
    import cv2
    import numpy as np
    #declare livestream
    video_capture = cv2.VideoCapture(2)


    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()


        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = frame[:, :, ::-1]

        # Only process every other frame of video to save time


        face_locations = face_recognition.face_locations(rgb_small_frame,model="cnn")

        if not face_locations:
            print("User missing")
        # Display the results
        for (top, right, bottom, left) in face_locations:
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, "Loser" ,  (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

