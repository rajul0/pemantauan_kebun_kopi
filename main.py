from tampilan import menu,layar
from basisdata import buatBasisdata,buatTabelDaftarPohon, buatTabelDataPohon

# Buat basisdata dan tabel pohon
buatBasisdata()
buatTabelDaftarPohon()
# buatTabelDataPohon()

menu()
layar.mainloop()
