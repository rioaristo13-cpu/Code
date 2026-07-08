from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Web ini menggunakan Flask"w

@app.route("/data")
def data():
    return "Nama saya Walter Hartwell White dengan NPM 50425143"

if __name__ == "__main__":
    app.run(port=8088)