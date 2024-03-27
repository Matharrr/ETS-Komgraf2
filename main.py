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
awan2 = Awan(700, 120)


teratai1 = Teratai(800, 300)
teratai2 = Teratai(600, 300)
teratai3 = Teratai(400, 300)

rumput = Ilalang(172, 255)

egg = Telur(185, 290)
egg1 = Telur(195, 290)
egg2 = Telur(205, 290)
egg3 = Telur(215, 290)
egg4 = Telur(225, 290)
egg5 = Telur(195, 298)
egg6 = Telur(205, 298)
egg7 = Telur(215, 298)
egg8 = Telur(197, 306)
egg9 = Telur(185, 306)
egg10 = Telur(195, 306)

cebong = Kecebong(195, 438)

cebong_kaki  = Kecebong_Berkaki(479, 509)

Katak_muda = KatakMuda(799, 429)

Katak_dewasa = KatakDewasa(799, 280)

def draw_background():
    primitif.basic.draw_wavy_line(0, 300, 1000, 300, 8, 12, c=[100,149,207, 255])

    awan1.draw()
    awan1.move(1.2, 0)
    awan2.draw()
    awan2.move(1.8, 0)
    if awan1.awan.x > 500:
        awan1.awan.x = 0
    if awan2.awan.x > 1000:
        awan2.awan.x = 0
    
    rumput.draw()
    
    teratai1.draw()
    teratai2.draw()
    teratai3.draw()
    
def draw():
    py5.background(191)
    draw_background()
    if egg10.y <= 438:
        egg.draw()
        egg1.draw()
        egg2.draw()
        egg3.draw()
        egg4.draw()
        egg5.draw()
        egg6.draw()
        egg7.draw()
        egg8.draw()
        egg9.draw()
        egg10.draw()
        egg10.move(0, 6)
    elif cebong.y <= 509:
        cebong.draw()
        cebong.move(4, 1)
    elif cebong_kaki.y >= 429:
        cebong_kaki.draw()
        cebong_kaki.move(4, -1)
    elif Katak_muda.y <= 429:
        Katak_muda.draw()
        Katak_muda.move(1, 4)
    elif Katak_muda.y >=280:
        Katak_dewasa.draw()
        
        
def setup():
    py5.frame_rate(60)
    py5.rect_mode(py5.CENTER) 
    py5.loop()
    
def settings():
    py5.size(1000, 600)
    
def key_pressed():
    key_pressed = py5.key
    if key_pressed == " ":
        if Katak_dewasa.y == 280:
            Katak_dewasa.is_jumping = True
        if Katak_dewasa.y == 220:
            Katak_dewasa.is_jumping = False
        
        if Katak_dewasa.is_jumping == False:
            Katak_dewasa.move(1, 4)
        else:
            Katak_dewasa.move(1, -4)
            
#mengetahui koordinat dari klik mouse
def mouse_pressed():
    print(f"{py5.mouse_x}, {py5.mouse_y}")
    
py5.run_sketch()