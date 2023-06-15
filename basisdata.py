import sqlite3

def buatBasisdata():
  koneksi = sqlite3.connect("kebun_kopi.db")
  koneksi.close()

def buatTabelDaftarPohon():
  # Buka koneksi ke database
  koneksi = sqlite3.connect("kebun_kopi.db")

  # Buat tabel fakultas
  sql = """CREATE TABLE IF NOT EXISTS daftar_pohon(
          id INTEGER PRIMARY KEY,
          idPohon INTEGER,
          lat INTEGER,
          lon INTEGER);"""
  
  koneksi.execute(sql)
  koneksi.commit()
  # Tutup koneksi
  koneksi.close()

def buatTabelDataPohon():
  koneksi = sqlite3.connect("kebun_kopi.db")

  # Buat tabel fakultas
  sql = """CREATE TABLE IF NOT EXISTS data_pohon(
          idPohon INTEGER,
          sensor0 float,
          sensor1 float,
          sensor2 float,
          sensor3 float,
          sensor4 float,
          sensor5 float,
          sensor6 float,
          sensor7 float,
          sensor8 float,
          sensor9 float,
          waktu integer);"""
  
  koneksi.execute(sql)
  koneksi.commit()
  # Tutup koneksi
  koneksi.close()
  
def tambahPohon(idPohon,lat,lon):
  koneksi = sqlite3.connect("kebun_kopi.db")

  # Buat tabel fakultas
  sql = """INSERT INTO daftar_pohon(idPohon,lat,lon)
          VALUES(?,?,?);"""
  koneksi.execute(sql,(idPohon,lat,lon,))
  koneksi.commit()
  koneksi.close()

def tambahDataPohon(idPohon,sens0,sens1,sens2,sens3,sens4,sens5,sen6,sens7,sens8,sens9,waktu):
  koneksi = sqlite3.connect("kebun_kopi.db")

  # Buat tabel fakultas
  sql = """INSERT INTO data_pohon(idPohon,sensor0,sensor1,sensor2,sensor3,sensor4,sensor5,sensor6,sensor7,sensor8,sensor9,waktu)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?);"""
  koneksi.execute(sql,(idPohon,sens0,sens1,sens2,sens3,sens4,sens5,sen6,sens7,sens8,sens9,waktu))
  koneksi.commit()
  koneksi.close()

def ambilSemuaDaftarPohon():
  koneksi = sqlite3.connect("kebun_kopi.db")

  # Buat tabel fakultas
  sql = """SELECT * FROM daftar_pohon"""
  
  kursor = koneksi.execute(sql)
  hasil = kursor.fetchall()
  daftarPohon = []
  for satu_baris in hasil:
      daftarPohon.append(satu_baris)
    
  koneksi.commit()
  koneksi.close()
  return daftarPohon

def ambilDataPohon():
  koneksi = sqlite3.connect("kebun_kopi.db")

  # Buat tabel fakultas
  sql = """SELECT * FROM data_pohon"""
  
  kursor = koneksi.execute(sql)
  hasil = kursor.fetchall()
  dataPohon = []
  for satu_baris in hasil:
      dataPohon.append(satu_baris)
    
  koneksi.commit()

  koneksi.close()
  return dataPohon
  
def ambilIdPohon():
  koneksi = sqlite3.connect("kebun_kopi.db")

  # Buat tabel fakultas
  sql = """SELECT idPohon FROM daftar_pohon"""
  
  kursor = koneksi.execute(sql)
  hasil = kursor.fetchall()
  daftarPohon = []
  for satu_baris in hasil:
      daftarPohon.append(satu_baris[0])
  koneksi.commit()
  koneksi.close()
  return daftarPohon

def hapusPohon(idPohon):
 
  koneksi = sqlite3.connect("kebun_kopi.db")
  sql = "delete from daftar_pohon where idPohon = ?;"
  koneksi.execute(sql, (idPohon,))
  koneksi.commit()
  sql = """delete from data_pohon where idPohon=?;"""
  koneksi.execute(sql, (idPohon,))
  koneksi.commit()
  koneksi.close()

def ambilDataSatuPohon(idPohon):
  koneksi = sqlite3.connect("kebun_kopi.db")
  sql = """SELECT * FROM data_pohon where idPohon = ?;"""
  kursor = koneksi.execute(sql, (idPohon,))
  hasil = kursor.fetchall()
  dataSatuPohon = []
  for satu_baris in hasil:
      dataSatuPohon.append(satu_baris[0])
  koneksi.commit()
  koneksi.close()
  
  return dataSatuPohon

def ambilDataAntaraWaktu(idPohon,waktumulai,waktuakhir):
  koneksi = sqlite3.connect("kebun_kopi.db")
  sql = """SELECT * FROM data_pohon where idPohon = ? and waktu between ? and ?;"""
  kursor = koneksi.execute(sql,(idPohon,waktumulai,waktuakhir,))
  hasil = kursor.fetchall()
  dataPohon=[]
  for i in hasil:
    dataPohon.append(i)
  return dataPohon