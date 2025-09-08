from flask import Flask, render_template, request
import random
app = Flask(__name__)



@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")



@app.route("/8Ball", methods = ["POST"])
def ball():

    napis = request.form.get("text", "").lower()

    naključni_odgovori = [
        "Seveda!", 
        "Brez dvoma.", 
        "Lahko računaš na to.", 
        "Zelo verjetno.", 
        "Izgleda dobro.", 
        "Poskusi znova kasneje.", 
        "Raje ti ne povem zdaj.", 
        "Ne računaj na to.", 
        "Moj odgovor je ne.", 
        "Zelo dvomim."
    ]


    if "ljubezen" in napis:
        r =  "Kupi raje GPU"
    elif "vikend" in napis:
        r =  "TikTok all day"
    elif "denar" in napis:
        r =  "Burek only"
    elif "profesor" in napis:
        r =  "F speedrun"
    elif napis.endswith("!"):
        r =  "Ne kriči"
    else:
        r =  random.choice(naključni_odgovori)
    
    return  render_template("index.html", rezultat = r)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
#app.run(debug=True, port=5000)