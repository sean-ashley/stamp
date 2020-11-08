#inspired by https://medium.com/datadriveninvestor/video-streaming-using-flask-and-opencv-c464bf8473d6
from flask import Flask, render_template, Response, jsonify
from frame_extraction import Camera


app = Flask(__name__)

@app.route('/')
#render webpage
def index():
    return render_template("index.html")

#function that gets camera feed
def gen(camera):
    while True:
    #retrieve the frame and return it as an iterator
        frame = camera.extract_frames()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#function that determines if the user is in front of the camera
def present(camera):
    return jsonify(camera.is_user_on_screen())



#define camera feed that will be displayed on the page
@app.route('/feed')
def feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
#this is route where it will give you a json response depending on if you are in front of the camera or not.
@app.route('/screen')
def screen():
    return present(Camera())

if __name__ == '__main__':
    # defining server ip address and port
    app.run(host="0.0.0.0", port=80)


