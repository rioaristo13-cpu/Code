from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

mahasisw_data = [
    {   
    "nama":"Aristo",
    "npm":"12590712",
    "kelas":"1AI15"
    },
    {   
    "nama":"Azario",
    "npm":"21487214",
    "kelas":"2TB23"
    },
    {   
    "nama":"Christyan",
    "npm":"50521231",
    "kelas":"1PS24"
    }
]

class HelloWorld(Resource):
    def get(self):
        return {"message":"hello world"}
    
class Mahasiswa(Resource):
    def get(self, npm=None):
        if npm is None:
            return mahasisw_data

        for mahasiswa in mahasisw_data:
            if mahasiswa['npm'] == npm:
                return mahasiswa
        return {"error":"Mahasiswa tidak ditemukan"}, 404
    
    def post(self):
        new_mahasiswa = request.get_json()
        if not new_mahasiswa or "nama" not in new_mahasiswa or "npm" not in new_mahasiswa:
            return {"error":"Data mahasiswa tidak valid"},404
        
        mahasisw_data.append(new_mahasiswa)
        return new_mahasiswa, 201
    
    def put(self, npm=None):
        if npm is None:
            return {"error":"NPM diperlukan untuk update"},400

        updated_data = request.get_json()
        if not updated_data or "npm" not in updated_data:
            return {"error":"data mahasiswa tidak valid"}, 400

        for mahasiswa in mahasisw_data:
            if mahasiswa['npm'] == updated_data['npm']:
                mahasiswa.update(updated_data)
                return mahasiswa
        return {"error":"Mahasiswa tidak ditemukan"}, 404
            
    def delete(self, npm=None):
        if npm is None:
            return {"error":"NPM diperlukan untuk update"},400

        data = request.get_json()
        if not data or "npm" not in data:
            return {"error":"Data mahasiswa tidak valid"}, 400
        
        for i,mahasiswa in enumerate(mahasisw_data):
            if mahasiswa['npm'] == data['npm']:
                del mahasisw_data[i]
                return {"message":"Data mahasiswa terhapus"}
        return {"error":"Mahasiswa tidak ditemukan"}, 404
    
api.add_resource(HelloWorld, "/")
api.add_resource(Mahasiswa, "/mahasiswa")
api.add_resource(Mahasiswa, "/mahasiswa/<string:npm>", endpoint="mahasiswa_by_npm")


if __name__ == '__main__':
    app.run(debug=True)