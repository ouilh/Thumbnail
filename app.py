from flask import Flask, render_template, request, send_file
from pytube import YouTube
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

quality_mapping = {
    "1920x1080": 1920,
    "640x480": 640,
    "480x360": 480, 
    "320x180": 320,
    "120x90": 120,
}

def get_thumbnail(video_url, h, v):
    try:
        yt = YouTube(video_url)
        if yt:
            thumbnail_url = yt.thumbnail_url
            response = requests.get(thumbnail_url)
            img = Image.open(BytesIO(response.content))
            img = img.resize((h, v), Image.ANTIALIAS)
            resized_image_bytesio = BytesIO()
            img.save(resized_image_bytesio, format='JPEG')
            return resized_image_bytesio.getvalue()
        else:
            return None
    except Exception as e:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form["video_url"]
        quality = request.form["quality"]
        h=quality_mapping.get(quality)
        if h==1920 :
            v=1080
        elif h==640:
            v=480
        elif h==480:
            v=360
        elif h==320:
            v=180
        elif h==120:
            v=90
        
        if video_url:
            thumbnail_data = get_thumbnail(video_url, h, v)
            if thumbnail_data:
                return send_file(BytesIO(thumbnail_data), attachment_filename='thumbnail.jpg', as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
