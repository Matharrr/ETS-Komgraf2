import py5
from KatakDewasa import KatakDewasa
from Kecebong import Kecebong
from Telur import Telur
from Kecebong_Berkaki import Kecebong_Berkaki
from KatakMuda import KatakMuda

egg = Telur(160, 310)
cebong = Kecebong(290, 400)
cebong_kaki  = Kecebong_Berkaki(500, 500)
Katak_muda = KatakMuda(700, 500)
Katak_dewasa = KatakDewasa(900, 500)

def setup(self):
    py5.rect_mode(py5.CENTER) 
    py5.background(191)

def draw():
    egg.draw()
    cebong.draw()
    cebong_kaki.draw()
    Katak_muda.draw()
    Katak_dewasa.draw()
    
def settings():
    py5.size(1000, 600)
    
#mengetahui koordinat dari klik mouse
def mouse_pressed():
    print(py5.mouse_x, py5.mouse_y)

py5.run_sketch()