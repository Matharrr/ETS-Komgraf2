import py5
import primitif.basic
from metamorfosis_katak.KatakDewasa import KatakDewasa
from metamorfosis_katak.Kecebong import Kecebong
from metamorfosis_katak.Telur import Telur
from metamorfosis_katak.Kecebong_Berkaki import Kecebong_Berkaki
from metamorfosis_katak.KatakMuda import KatakMuda
from background.ilalang import Ilalang
from background.teratai import Teratai
from background.awan import Awan

awan1 = Awan(150, 100)
awan2 = Awan(260, 80)
awan3 = Awan(700, 120)
awan4 = Awan(810, 150)
teratai1 = Teratai(800, 300)
teratai2 = Teratai(600, 300)
teratai3 = Teratai(400, 300)
rumput = Ilalang(172, 255)
egg = Telur(185, 290)
cebong = Kecebong(307, 438)
cebong_kaki  = Kecebong_Berkaki(500, 500)
Katak_muda = KatakMuda(701, 427)
Katak_dewasa = KatakDewasa(800, 280)

def setup():
    py5.rect_mode(py5.CENTER) 
    py5.background(191)

def draw():
    primitif.basic.draw_wavy_line(0, 300, 1000, 300, 8, 12, c=[100,149,207, 255])
    awan1.draw()
    awan2.draw()
    awan3.draw()
    awan4.draw()
    rumput.draw()
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