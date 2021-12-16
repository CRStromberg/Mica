from flask import Flask, flash, redirect, render_template, request, session, abort, Response
from camera_pi import Camera
import os
import mods

app = Flask(__name__)

@app.route('/', methods=['POST' , 'GET'])
def home():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        print(request.method)
        if request.method == 'POST':
            if request.form.get('Give Mica Treat') == 'Give Mica Treat':
                #pass
                 mods.motor()
            elif request.form.get('Call Mica') == 'Call Mica':
                #pass do something else
                mods.aud()
            else:
                #pass
                return render_template("home.html")
        elif request.method == 'GET':
            #return render_template("index.html")
            print("No Post Back Call")
    return render_template("home.html")

@app.route('/login', methods=['POST' , 'GET'])
def do_admin_login():
    if request.form['password'] == 'pass' and request.form['username'] == 'admin':
        session['logged_in'] = True
        print(request.method)
        if request.method == 'POST':
            if request.form.get('Give Mica Treat') == 'Give Mica Treat':
                #pass
                mods.motor()
            elif request.form.get('Call Mica') == 'Call Mica':
                #pass do something else
                mods.aud()
            else:
                #pass
                return render_template("home.html")
        elif request.method == 'GET':
            #return render_template("index.html")
            print("No Post Back Call")
        return render_template("home.html")

    else:
        flash('wrong password!')
        return home()

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)