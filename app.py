import requests
from flask import Flask, render_template, request
app = Flask (__name__)

@app.route("/", methods=["get", "post"])
def cuaca():
    if request.method =="POST":
        kota = request.form["kota"]
        api_key = "62dc3fe9ccb2ae36cf3d6aa692ca11ec"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={kota}&appid={api_key}&units=metric"
        data = requests.get(url).json()
        suhu = data["main"]["temp"]
        deskripsi = data["weather"][0]["description"]
        return render_template("cuaca.html", kota=kota, suhu=suhu,deskripsi=deskripsi)
    return render_template("cuaca.html")
if __name__ == "__main__":
    app.run(debug=True, port=5001)