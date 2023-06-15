from datetime import datetime,timedelta
import json
from urllib.request import urlopen
import time


# Buat tabel basisdata,data pohon,daftar_pohon
from basisdata import buatBasisdata,buatTabelDaftarPohon,buatTabelDataPohon

buatBasisdata()
buatTabelDaftarPohon()
buatTabelDataPohon()

def ambilData(idPohon,sensorType):
  NPM = "2104111010095"

  alamat = f"https://belajar-python-unsyiah.an.r.appspot.com/sensor/read?npm={NPM}&id_tree={idPohon}&sensor_type={sensorType}"

  url = urlopen(alamat)

  dokumen = url.read().decode('utf-8')

  data = json.loads(dokumen)

  return data


while True:
  from basisdata import ambilIdPohon
  daftarPohon = ambilIdPohon()
  for satuPohon in daftarPohon:
    dataPohon = []
    dataSensor = []
    
    for i in range(10):
      data = ambilData(satuPohon,i)
      a= list(data.keys())
      tmpData = []
      for x in a:
        tmpData.append(data[x])
      dataPohon.append(tmpData)
    
    for satu_pohon in dataPohon:
      dataSensor.append(satu_pohon[2])
      
    a = datetime.now() + timedelta(hours = 7) 
    menit = a.minute
    if len(str(menit)) ==  1:
      menit = f"0{menit}"
    waktu = int(f"{a.year}{a.month}{a.day}{a.hour}{menit}")
  
    from basisdata import tambahDataPohon,ambilDataPohon
    tambahDataPohon(satuPohon,dataSensor[0],dataSensor[1],dataSensor[2],dataSensor[3],dataSensor[4],dataSensor[5],dataSensor[6],dataSensor[7],dataSensor[8],dataSensor[9],waktu)
    print(ambilDataPohon())
    time.sleep(30)