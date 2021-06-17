class bunga :
    def __init__(self,nama,jumlah_kelopak,harga):
        self.nama=nama
        self.jumlah_kelopak=jumlah_kelopak
        self.harga=harga

    def set_nama(self,new_nama):
        self.nama=new_nama

    def set_jumlah_kelopak(self,new_jumlah_kelopak):
        self.nama=new_jumlah_kelopak

    def harga(self,new_harga):
        self.nama=new_harga

bunga=bunga("Tulip",8,18000)
print(" Bunga",bunga1.nama,"berkelopak",bunga1.jumlah_kelopak,"harga ",bunga1.harga)
bunga1.set_nama("Tulip")
print(" Bunga",bunga1.nama,"berkelopak",bunga1.jumlah_kelopak,"harga ",bunga1.harga)