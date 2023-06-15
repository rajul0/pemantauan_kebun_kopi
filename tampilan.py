import tkinter
import tkinter.messagebox
from matplotlib import pyplot

layar = tkinter.Tk()
layar.geometry("500x500")

def tombolTambahKlik():
  idPohon = entryId.get()
  idPohon = int(idPohon)

  latPohon = entryLat.get()
  latPohon = int(latPohon)

  lonPohon = entryLon.get()
  lonPohon = int(lonPohon)
  
  from basisdata import ambilSemuaDaftarPohon
  semuaDaftarPohon = ambilSemuaDaftarPohon()
  daftarPohon = []
  for i in range(len(semuaDaftarPohon)):
    daftarPohon.append(semuaDaftarPohon[i][1])
    
  global layarTampilanTambahPohon
  if idPohon in daftarPohon:
    tkinter.messagebox.showwarning("Waduh", f"Pohon {idPohon} Sudah Terdaftar")
    layarTampilanTambahPohon.destroy()
    return
    
  from basisdata import tambahPohon
  tambahPohon(idPohon,latPohon,lonPohon)

  layarTampilanTambahPohon.destroy()
  tkinter.messagebox.showinfo("yee", f"Berhasil Menambahkan pohon{idPohon}")
  
def tampilanTambahPohon():
  
  global layarTampilanTambahPohon
  layarTampilanTambahPohon = tkinter.Toplevel(layar)

  frame1TambahPohon = tkinter.Frame(layarTampilanTambahPohon)
  frame1TambahPohon.pack(anchor = tkinter.NW)

  # Bagian Id Pohon
  labelId = tkinter.Label(frame1TambahPohon,text = "ID Pohon: ")
  labelId.pack(side = tkinter.LEFT)
  
  global entryId
  entryId= tkinter.Entry(frame1TambahPohon,width = 10)
  entryId.pack(side = tkinter.LEFT)

  # Bagian Lal dan Lon pohon
  frame2TambahPohon = tkinter.Frame(layarTampilanTambahPohon)
  frame2TambahPohon.pack(anchor = tkinter.NW)
  
  labelLat = tkinter.Label(frame2TambahPohon,text = "Lat: ")
  labelLat.pack(side = tkinter.LEFT)
  
  global entryLat
  entryLat = tkinter.Entry(frame2TambahPohon)
  entryLat.pack(side = tkinter.LEFT)

  labelLon = tkinter.Label(frame2TambahPohon,text = "Lon: ")
  labelLon.pack(side = tkinter.LEFT)

  global entryLon
  entryLon = tkinter.Entry(frame2TambahPohon)
  entryLon.pack(side = tkinter.LEFT)

  frame3TombolTambah = tkinter.Frame(layarTampilanTambahPohon)
  frame3TombolTambah.pack(anchor = tkinter.NW)
  
  tombolTambahId = tkinter.Button(frame3TombolTambah,text = "Tambah",command= tombolTambahKlik)
  tombolTambahId.pack(side = tkinter.LEFT)

  tombolBatal = tkinter.Button(frame3TombolTambah,text = "Batal",command= layarTampilanTambahPohon.destroy)
  tombolBatal.pack(side = tkinter.LEFT)
  

# Daftar Pohon  -----------------

def tampilanDaftarPohon():
  
  layarTampilanDaftarPohon = tkinter.Toplevel(layar)

  scrollbar = tkinter.Scrollbar(layarTampilanDaftarPohon)
  scrollbar.pack( side = tkinter.RIGHT, fill = tkinter.Y )
  
  cnv1 = tkinter.Canvas(layarTampilanDaftarPohon,yscrollcommand = scrollbar.set)
  cnv1.pack(anchor = tkinter.NW)  
  
  frame1DaftarPohon = tkinter.Frame(cnv1)
  frame1DaftarPohon.pack(anchor = tkinter.NW)

  from basisdata import ambilSemuaDaftarPohon
  daftarPohon = ambilSemuaDaftarPohon()

  judulHeader = ["NO","ID Pohon","Lat", "Lon"]
  daftarPohon.insert(0,judulHeader)
  total_row = len(daftarPohon)
  total_column = len(daftarPohon[0])
  
      # Tabel Daftar Pohon
  for baris in range(total_row):
    for kolom in range(total_column):      
      isiTabel = tkinter.Label(frame1DaftarPohon,text = daftarPohon[baris][kolom],width=7,font=("Times New Roman",12,'bold'))
      isiTabel.grid(row = baris, column=kolom)
      scrollbar.config(command = cnv1.yview )

def tombolHapusKlik():
  global entryIdHapus
  idPohonHapus = entryIdHapus.get()
  idPohonHapus = int(idPohonHapus)

  from basisdata import ambilIdPohon,hapusPohon,ambilDataSatuPohon
  if idPohonHapus in ambilIdPohon() or idPohonHapus in ambilDataSatuPohon(idPohonHapus):
    hapusPohon(idPohonHapus)
    layarTampilanHapus.destroy()
    tkinter.messagebox.showinfo("Yee", f"Pohon {idPohonHapus} berhasil Di hapus")

  else: 
    tkinter.messagebox.showwarning("Waduh", f"Pohon {idPohonHapus} tidak ada di basisdata")
    
  
def tampilanHapusPohon():
  
  global layarTampilanHapus
  layarTampilanHapus = tkinter.Toplevel(layar)
  layarTampilanHapus.geometry("500x500")
  
  # FRame 1
  frame1HapusPohon = tkinter.Frame(layarTampilanHapus)
  frame1HapusPohon.pack(anchor = tkinter.NW)

  # Bagian Id Pohon
  labelId = tkinter.Label(frame1HapusPohon,text = "ID Pohon: ")
  labelId.pack(side = tkinter.LEFT)
  
  global entryIdHapus
  entryIdHapus= tkinter.Entry(frame1HapusPohon,width = 10)
  entryIdHapus.pack(side = tkinter.LEFT)

  # Frame 2 
  frame2HapusPohon = tkinter.Frame(layarTampilanHapus)
  frame2HapusPohon.pack(anchor = tkinter.NW)
  
  tombolHapus = tkinter.Button(frame2HapusPohon,text = "Hapus",command= tombolHapusKlik)
  tombolHapus.pack(side = tkinter.LEFT)

  tombolBatal = tkinter.Button(frame2HapusPohon,text = "Batal",command= layarTampilanHapus.destroy)
  tombolBatal.pack(side = tkinter.LEFT)


def tampilkanGrafik1(idPohon,data):
  sens0 =[i[1] for i in data]
  sens1 =[i[2] for i in data]
  sens2 =[i[3] for i in data]
  sens3=[i[4] for i in data]
  sens4=[i[5] for i in data]
  sens5 =[i[6] for i in data]
  sens6 =[i[7] for i in data]
  sens7 =[i[8] for i in data]
  sens8 =[i[9] for i in data]
  sens9 =[i[10] for i in data]
  waktu = [i[11] for i in data]
  waktu = [str(i)[9:] for i in waktu]

  pyplot.plot(waktu, sens0, "w->", label="Suhu Udara")
  pyplot.plot(waktu, sens1, "m->", label="Kelembaban Udara")
  pyplot.plot(waktu, sens2, "r->", label="Curah Hujan")
  pyplot.plot(waktu, sens3, "c->", label="Tingkat Sinar UV")
  pyplot.plot(waktu, sens4, "m->", label="Suhu Tanah")
  pyplot.plot(waktu, sens5, "y->", label="Kelembaban Tanah")
  pyplot.plot(waktu, sens6, "b->", label="PH Tanah")
  pyplot.plot(waktu, sens7, "g->", label="Kadar N dalam Tanah")
  pyplot.plot(waktu, sens8, "y->",label="Kadar P dalam Tanah")
  pyplot.plot(waktu, sens9, "b->", marker = '.', label="Kadar K dalam Tanah")
  pyplot.xlabel("Waktu (Menit)")
  pyplot.ylabel("Nilai Sensor")
  pyplot.legend()
  pyplot.title(f"Grafik Semua Sensor untuk Pohon {idPohon}")
  pyplot.show()

  
  
  
  
def grafik1():
  idPohon = entIdPohon.get()
  idPohon = int(idPohon)
  tahun = entryTahunDari.get()
  tahun = int(tahun)
  bulan =entryBulanDari.get()
  bulan = int(bulan)
  tanggal = entryTanggalDari.get()
  tanggal = int(tanggal)
  jam = entryJamDari.get()
  jam = int(jam)
  menit = entryMenitDari.get()
  menit = int(menit)
  if len(str(menit)) == 1:
    menit = f"0{menit}"

  # Waktu Sampai
  tahun2 = entryTahunSampai.get()
  tahun2 = int(tahun2)
  bulan2 =entryBulanSampai.get()
  bulan2 = int(bulan2)
  tanggal2 = entryTanggalSampai.get()
  tanggal2 = int(tanggal2)
  jam2 = entryJamSampai.get()
  jam2 = int(jam2)
  menit2 = entryMenitSampai.get()
  menit2 = int(menit2)
  
  if len(str(menit2)) == 1:
    menit2 = f"0{menit2}"
  waktu1 = int(f"{tahun}{bulan}{tanggal}{jam}{menit}")
  waktu2 = int(f"{tahun2}{bulan2}{tanggal2}{jam2}{menit2}")
  print(waktu1,waktu2)

  from basisdata import ambilDataAntaraWaktu
  data = ambilDataAntaraWaktu(idPohon,waktu1,waktu2)
  
  tampilkanGrafik1(idPohon,data)
  
  
  
def tampilanGrafikSatu():
  
  layarTampilanGrafikSatu = tkinter.Toplevel(layar)
  layarTampilanGrafikSatu.geometry("500x500")
  
  frame1Grafik1 = tkinter.Frame(layarTampilanGrafikSatu)
  frame1Grafik1.pack(anchor = tkinter.NW)

  labelJudul = tkinter.Label(frame1Grafik1,text = "Grafik Semua Sensor \n Untuk Satu Pohon dalam rentang waktu tertentu")
  labelJudul.pack(anchor = tkinter.NW)

  # bagian Id Pohon
  frameIdPohon = tkinter.Frame(layarTampilanGrafikSatu)
  frameIdPohon.pack(anchor = tkinter.NW)

  global entIdPohon
  lblIdPohon = tkinter.Label(frameIdPohon,text = "ID: ",font=("Times New Roman",10,"bold"))
  lblIdPohon.pack(anchor = tkinter.NW)
  entIdPohon = tkinter.Entry(frameIdPohon)
  entIdPohon.pack(anchor = tkinter.NW)
  
  # Bagian dari dan sampai
  frame2Grafik1 = tkinter.Frame(layarTampilanGrafikSatu)
  frame2Grafik1.pack(anchor = tkinter.NW)

  labelDari = tkinter.Label(frame2Grafik1,text = "Dari",font=("Times New Roman",10,"bold"))
  labelDari.grid(row = 0,column = 0,padx= 50)
  
  labelSampai = tkinter.Label(frame2Grafik1,text = "Sampai",font=("Times New Roman",10,"bold"))
  labelSampai.grid(row = 0,column = 2,padx = (100,10))

  labelTahunDari =tkinter.Label(frame2Grafik1,text = "Tahun : ")
  labelTahunDari.grid(row = 1,column = 0,padx =5)

  global entryTahunDari
  entryTahunDari = tkinter.Entry(frame2Grafik1,width=8)
  entryTahunDari.grid(row=1,column = 1)

  labelBulanDari =tkinter.Label(frame2Grafik1,text = "Bulan : ")
  labelBulanDari.grid(row = 2,column = 0,padx =5)

  global entryBulanDari
  entryBulanDari = tkinter.Entry(frame2Grafik1,width=8)
  entryBulanDari.grid(row=2,column = 1)

  labelTanggalDari =tkinter.Label(frame2Grafik1,text = "Tanggal : ")
  labelTanggalDari.grid(row = 3,column = 0,padx =5)

  global entryTanggalDari
  entryTanggalDari = tkinter.Entry(frame2Grafik1,width=8)
  entryTanggalDari.grid(row=3,column = 1)

  global entryJamDari
  labelJamDari =tkinter.Label(frame2Grafik1,text = "Jam : ")
  labelJamDari.grid(row = 4,column = 0,padx =5)
  
  entryJamDari = tkinter.Entry(frame2Grafik1,width=8)
  entryJamDari.grid(row=4,column = 1)

  labelMenitDari =tkinter.Label(frame2Grafik1,text = "Menit : ")
  labelMenitDari.grid(row = 5,column = 0,padx =5)

  global entryMenitDari
  entryMenitDari = tkinter.Entry(frame2Grafik1,width=8)
  entryMenitDari.grid(row=5,column = 1)

  # Bagian Sampai
  labelTahunSampai =tkinter.Label(frame2Grafik1,text = "Tahun : ")
  labelTahunSampai.grid(row = 1,column = 2,padx =5)

  global entryTahunSampai 
  entryTahunSampai = tkinter.Entry(frame2Grafik1,width=8)
  entryTahunSampai.grid(row=1,column = 3)

  labelBulanSampai =tkinter.Label(frame2Grafik1,text = "Bulan : ")
  labelBulanSampai.grid(row = 2,column = 2,padx =5)

  global entryBulanSampai
  entryBulanSampai = tkinter.Entry(frame2Grafik1,width=8)
  entryBulanSampai.grid(row=2,column = 3)

  labelTanggalSampai =tkinter.Label(frame2Grafik1,text = "Tanggal : ")
  labelTanggalSampai.grid(row = 3,column = 2,padx =5)

  global entryTanggalSampai
  entryTanggalSampai = tkinter.Entry(frame2Grafik1,width=8)
  entryTanggalSampai.grid(row=3,column = 3)

  labelJamSampai =tkinter.Label(frame2Grafik1,text = "Jam : ")
  labelJamSampai.grid(row = 4,column = 2,padx =5)

  global entryJamSampai
  entryJamSampai = tkinter.Entry(frame2Grafik1,width=8)
  entryJamSampai.grid(row=4,column = 3)

  labelMenitSampai =tkinter.Label(frame2Grafik1,text = "Menit : ")
  labelMenitSampai.grid(row = 5,column = 2,padx =5)

  global entryMenitSampai
  entryMenitSampai = tkinter.Entry(frame2Grafik1,width=8)
  entryMenitSampai.grid(row=5,column = 3)

  frame3Grafik1 = tkinter.Frame(layarTampilanGrafikSatu)
  frame3Grafik1.pack(anchor = tkinter.NW , pady = 10)

  global grafik1
  tombolTampilkan = tkinter.Button(frame3Grafik1,text = "Tampilkan",command=grafik1)
  tombolTampilkan.pack(side = tkinter.LEFT)

  tombolTampilkan = tkinter.Button(frame3Grafik1,text = "Batal",command=layarTampilanGrafikSatu.destroy)
  tombolTampilkan.pack(side = tkinter.LEFT)

  
def tampilanGrafikDua():
  
  layarTampilanGrafik2 = tkinter.Toplevel(layar)
  layarTampilanGrafik2.geometry("500x500")

  frame1Grafik1 = tkinter.Frame(layarTampilanGrafik2)
  frame1Grafik1.pack(anchor = tkinter.NW)

  labelJudul = tkinter.Label(frame1Grafik1,text = "Grafik Semua Sensor \n Untuk Satu Pohon dalam rentang waktu tertentu")
  labelJudul.pack(anchor = tkinter.NW)

  frame2Grafik1 = tkinter.Frame(layarTampilanGrafik2)
  frame2Grafik1.pack(anchor = tkinter.NW)

  labelDari = tkinter.Label(frame2Grafik1,text = "Dari",font=("Times New Roman",10,"bold"))
  labelDari.grid(row = 0,column = 0,padx= 50)
  
  labelSampai = tkinter.Label(frame2Grafik1,text = "Sampai",font=("Times New Roman",10,"bold"))
  labelSampai.grid(row = 0,column = 2,padx = (100,10))

  labelTahunDari =tkinter.Label(frame2Grafik1,text = "Tahun : ")
  labelTahunDari.grid(row = 1,column = 0,padx =5)

  global entryTahunDari
  entryTahunDari = tkinter.Entry(frame2Grafik1,width=8)
  entryTahunDari.grid(row=1,column = 1)

  labelBulanDari =tkinter.Label(frame2Grafik1,text = "Bulan : ")
  labelBulanDari.grid(row = 2,column = 0,padx =5)

  global entryBulanDari
  entryBulanDari = tkinter.Entry(frame2Grafik1,width=8)
  entryBulanDari.grid(row=2,column = 1)

  labelTanggalDari =tkinter.Label(frame2Grafik1,text = "Tanggal : ")
  labelTanggalDari.grid(row = 3,column = 0,padx =5)

  global entryTanggalDari
  entryTanggalDari = tkinter.Entry(frame2Grafik1,width=8)
  entryTanggalDari.grid(row=3,column = 1)

  labelJamDari =tkinter.Label(frame2Grafik1,text = "Jam : ")
  labelJamDari.grid(row = 4,column = 0,padx =5)

  global entryJamDari
  entryJamDari = tkinter.Entry(frame2Grafik1,width=8)
  entryJamDari.grid(row=4,column = 1)

  labelMenitDari =tkinter.Label(frame2Grafik1,text = "Menit : ")
  labelMenitDari.grid(row = 5,column = 0,padx =5)

  global entryMenitDari
  entryMenitDari = tkinter.Entry(frame2Grafik1,width=8)
  entryMenitDari.grid(row=5,column = 1)

  # Bagian Sampai
  labelTahunSampai =tkinter.Label(frame2Grafik1,text = "Tahun : ")
  labelTahunSampai.grid(row = 1,column = 2,padx =5)

  global entryTahunSampai
  entryTahunSampai = tkinter.Entry(frame2Grafik1,width=8)
  entryTahunSampai.grid(row=1,column = 3)

  labelBulanSampai =tkinter.Label(frame2Grafik1,text = "Bulan : ")
  labelBulanSampai.grid(row = 2,column = 2,padx =5)

  global entryBulanSampai
  entryBulanSampai = tkinter.Entry(frame2Grafik1,width=8)
  entryBulanSampai.grid(row=2,column = 3)

  global entryTanggalSampai
  labelTanggalSampai =tkinter.Label(frame2Grafik1,text = "Tanggal : ")
  labelTanggalSampai.grid(row = 3,column = 2,padx =5)
  
  entryTanggalSampai = tkinter.Entry(frame2Grafik1,width=8)
  entryTanggalSampai.grid(row=3,column = 3)

  labelJamSampai =tkinter.Label(frame2Grafik1,text = "Jam : ")
  labelJamSampai.grid(row = 4,column = 2,padx =5)

  global entryJamSampai
  entryJamSampai = tkinter.Entry(frame2Grafik1,width=8)
  entryJamSampai.grid(row=4,column = 3)

  labelMenitSampai =tkinter.Label(frame2Grafik1,text = "Menit : ")
  labelMenitSampai.grid(row = 5,column = 2,padx =5)
  
  global entryMenitSampai
  entryMenitSampai = tkinter.Entry(frame2Grafik1,width=8)
  entryMenitSampai.grid(row=5,column = 3)

  frame3Grafik1 = tkinter.Frame(layarTampilanGrafik2)
  frame3Grafik1.pack(anchor = tkinter.NW , pady = 10)

  tombolTampilkan = tkinter.Button(frame3Grafik1,text = "Tampilkan",command='')
  tombolTampilkan.pack(side = tkinter.LEFT)

  tombolTampilkan = tkinter.Button(frame3Grafik1,text = "Batal",command=layarTampilanGrafik2.destroy)
  tombolTampilkan.pack(side = tkinter.LEFT)
  
  
def menu():
  frameMenu = tkinter.Frame(layar,bg = "blue")
  frameMenu.pack(anchor = tkinter.NW,expand = True,fill = "both")

  tombolTambah = tkinter.Button(frameMenu,text = "Tambah Pohon",command= tampilanTambahPohon)
  tombolTambah.grid(row = 0,column = 0,padx = 10)

  tombolDaftarPohon = tkinter.Button(frameMenu,text = "Daftar Pohon",command= tampilanDaftarPohon)
  tombolDaftarPohon.grid(row = 0,column = 1,padx = 10)

  tombolHapusPohon = tkinter.Button(frameMenu,text = "Hapus Pohon",command= tampilanHapusPohon)
  tombolHapusPohon.grid(row = 0,column = 2)

  tombolGrafik1 = tkinter.Button(frameMenu,text = "Grafik Sensor \n SatuPohon",bg = "red",command= tampilanGrafikSatu)
  tombolGrafik1.grid(row = 1,column = 0,pady = 20)

  tombolGrafik2 = tkinter.Button(frameMenu,text = "Grafik Sensor \n Semua Pohon",command= tampilanGrafikDua)
  tombolGrafik2.grid(row = 1,column = 2)
