import requests

response = requests.get("https://slrbxpdk-3000.asse.devtunnels.ms/mahasiswa")
data = response.json()

for i in range(len(data)):
    print (f"ID     : {data[i]['id']}")
    print (f"Nama   : {data[i]['nama']}")
    print (f"NPM    : {data[i]['npm']}")
    print (f"Kelas  : {data[i]['kelas']}")
    print ()