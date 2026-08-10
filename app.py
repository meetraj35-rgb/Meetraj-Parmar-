from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        img = qrcode.make(text) 
        img.save("static/qrcode.png")

        return render_template("index.html", qr="qrcode.png")

    return render_template("index.html")

app.run(host="0.0.0.0", port=5000, debug=True)