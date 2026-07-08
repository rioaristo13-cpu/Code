from flask import Flask

app = Flask(__name__)

students = [
                {
                "nama": "John Cahyono",
                "npm": "50427723",
                "kelas":"3IA23",
                },
                {
                "nama": "Aristo Azario Christyan",
                "npm": "50425143",
                "kelas":"1IA15",
                },
                {
                "nama": "Asep Yahudi",
                "npm": "51664366",
                "kelas":"2IA21",
                }
            ]

@app.route("/data/<val>")
def data(val):
    matching_items = []
    for item in students:
        for value in item.values():
            if isinstance(value, str) and val.lower() in value.lower():
                matching_items.append(item)
                break
    if matching_items:
        return {"data": matching_items}
    else:
        return "Data tidak ditemukan"

if __name__ == "__main__":
    app.run(debug=True)