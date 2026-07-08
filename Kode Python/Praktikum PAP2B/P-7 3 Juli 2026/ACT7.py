from flask import Flask, request, jsonify

app = Flask (__name__)

students = []

@app.route("/get_student", methods=["GET"])
def get_student():
    return jsonify(students)

@app.route("/add_student", methods=["POST"])
def add_student():
    studentbaru = request.json
    for student in students:
        if student["npm"] == studentbaru["npm"]:
            return jsonify({"status":"error","message":"NPM Sudah Ada"}), 400
    students.append(studentbaru)
    return jsonify({"status":"sukses","students":students})

@app.route("/delete_student", methods=["DELETE"])
def delete_student():
    npmhapus = request.args.get("npm")
    global students
    students = [student for student in students if student["npm"] != npmhapus]
    return jsonify({"status":"sukses","students":students})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

