from flask import Flask, render_template

app = Flask(__name__)

data = {
    "nama": "Aristo Azario Christyan",
    "npm": "50425143",
    "kelas": "1IA15",
    "jurusan": "Teknik Informatika",
    "fakultas": "Teknologi Industri"
}

@app.route("/")
def index():
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(port=8088)