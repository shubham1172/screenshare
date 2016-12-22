from flask import Flask, render_template, request, send_file
from PIL import ImageGrab
from io import BytesIO

app = Flask(__name__)

#Home
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/live')
def live():
    return render_template("live.html")

@app.route('/image')
def image():
    time = request.args.get('time')
    pil_img = ImageGrab.grab()
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg') 

if(__name__=="__main__"):
    app.run(host='192.168.137.1',debug=True,port=8082) 
