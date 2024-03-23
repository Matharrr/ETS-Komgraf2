import py5
from KatakDewasa import KatakDewasa
from Kecebong import Kecebong
from Telur import Telur
from Kecebong_Berkaki import Kecebong_Berkaki
from KatakMuda import KatakMuda
from background.teratai import Teratai

egg = Telur(160, 200)
cebong = Kecebong(307, 438)
cebong_kaki  = Kecebong_Berkaki(500, 500)
Katak_muda = KatakMuda(701, 427)
Katak_dewasa = KatakDewasa(800, 280)
teratai1 = Teratai(800, 300)
teratai2 = Teratai(600, 300)
teratai3 = Teratai(400, 300)

def setup():
    py5.rect_mode(py5.CENTER) 
    py5.background(191)

def draw():
    teratai1.draw()
    teratai2.draw()
    teratai3.draw()
    egg.draw()
    cebong.draw()
    cebong_kaki.draw()
    Katak_muda.draw()
    Katak_dewasa.draw()
    
def settings():
    py5.size(1000, 600)
    
#mengetahui koordinat dari klik mouse
def mouse_pressed():
    print(f"{py5.mouse_x}, {py5.mouse_y}")
    
py5.run_sketch()