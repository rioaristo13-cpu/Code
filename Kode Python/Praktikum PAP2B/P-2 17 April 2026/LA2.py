import requests

response = requests.get("http://localhost:3000/mahasiswa")

data = response.json()

print("Hasil GET Request: ")

print(response.status_code)

print(data)
print()

for i in range (len(data)):
    print (f"ID     : {data[i]['id']}")
    print (f"Nama   : {data[i]['nama']}")
    print (f"NPM    : {data[i]['npm']}")
    print (f"Kelas  : {data[i]['kelas']}")
    print ()