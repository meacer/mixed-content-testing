import os

from flask import Flask
from flask import request
from flask import send_file

app = Flask(__name__)


@app.route("/image.png")
def send_image():
    if request.base_url.startswith("https://"):
        return send_file('static/https-image.png', mimetype='image/png')
    else:
        return send_file('static/http-image.png', mimetype='image/png')

@app.route("/")
def hello_world():
    img_url = "http://%s/image.png" % request.headers['Host']
    return "<html><h1>Mixed content testing</h1>Image from %s:<br><img src='%s'></html>" % (img_url, img_url)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

