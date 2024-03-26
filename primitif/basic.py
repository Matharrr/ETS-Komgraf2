import math
import numpy as np
import primitif.line
import py5

def round(x):
    return int(x + 0.5)

def draw_margin(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(margin,margin,width-margin,margin))
    py5.points(primitif.line.line_dda(margin,height-margin,width-margin,height-margin))
    py5.points(primitif.line.line_bresenham(margin,margin,margin,height-margin))
    py5.points(primitif.line.line_bresenham(width-margin,margin,width-margin,height-margin))

def draw_grid(width, height, margin, c=[0,0,0,255]):
    # Sumbu Y
    xa = margin;
    ya = 2*margin;
    xb = width - xa
    yb = height - ya
    y_range = (height / margin)
    
    py5.stroke(c[0], c[1], c[2], c[3])
    for count in range(1, int(y_range)):
        py5.points(primitif.line.line_dda(xa,ya,xb,ya))
        ya = ya + margin

    # Sumbu X
    xa = 2*margin
    ya = margin
    xb = width - xa
    yb = height - ya
    x_range = (width / margin)
    for count in range(1, int(x_range)):
        py5.points(primitif.line.line_dda(xa,ya,xa,yb))
        xa = xa + margin
        
def draw_bentuk(pts, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(pts)

def draw_kartesian(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(width/2,margin,width/2,height-margin))
    py5.points(primitif.line.line_bresenham(margin,height/2,width-margin,height/2))

def persegi(xa, ya, panjang, c=[0,0,0,255]):
    return np.concatenate(
        (
            primitif.line.line_dda(xa,ya,xa+panjang,ya),
            primitif.line.line_dda(xa+panjang,ya,xa+panjang,ya+panjang),
            primitif.line.line_dda(xa+panjang,ya+panjang,xa,ya+panjang),
            primitif.line.line_dda(xa,ya+panjang,xa,ya)
        ),
        axis=0
    )

def persegi_panjang(xa, ya, panjang, lebar):
    return np.concatenate(
        (
            primitif.line.line_dda(xa,ya,xa+panjang,ya),
            primitif.line.line_dda(xa+panjang,ya,xa+panjang,ya+lebar),
            primitif.line.line_dda(xa+panjang,ya+lebar,xa,ya+lebar),
            primitif.line.line_dda(xa,ya+lebar,xa,ya),
        ),
        axis=0
    )
    
def segitiga_siku(xa, ya, alas, tinggi):
    return np.concatenate(
        (
            primitif.line.line_bresenham(xa, ya, xa+alas, ya),
            primitif.line.line_bresenham(xa, ya, xa, ya+tinggi),
            primitif.line.line_bresenham(xa, ya+tinggi, xa+alas, ya)
        ),
        axis=0
    )
    
def segitiga_sama_kaki(xa, ya, alas, tinggi):
    return np.concatenate(
        (
            primitif.line.line_bresenham(xa, ya, xa+alas, ya),
            primitif.line.line_bresenham(xa, ya, xa+(alas/2), ya+tinggi),
            primitif.line.line_bresenham(xa+(alas/2), ya+tinggi, xa+alas, ya)
        ),
        axis=0
    )

def trapesium_siku(xa, ya, aa, ab, tinggi, c=[0,0,0,255]):
    return np.concatenate(
        (
        py5.stroke(c[0], c[1], c[2], c[3]),
        py5.points(primitif.line.line_dda(xa,ya,xa+ab,ya)),
        py5.points(primitif.line.line_dda(xa,ya,xa,ya-tinggi)),
        py5.points(primitif.line.line_dda(xa,ya-tinggi,xa+aa,ya-tinggi)),
        py5.points(primitif.line.line_dda(xa+aa,ya-tinggi,xa+ab,ya)),
        ),
        axis=0
    )

def kali(xa, ya, panjang, c=[0,0,0,255]):
    return np.concatenate(
        (
        py5.stroke(c[0], c[1], c[2], c[3]),
        py5.points(primitif.line.line_dda(xa-panjang, ya-panjang, xa+panjang, ya+panjang)),
        py5.points(primitif.line.line_dda(xa+panjang, ya-panjang, xa-panjang, ya+panjang)),
        ),
        axis=0
    )

def ellipsePlotPoints(xc, yc, x, y):
    res = [
        [xc + x, yc + y],
        [xc - x, yc + y],
        [xc + x, yc - y],
        [xc - x, yc - y],
    ]
    return res

def circlePlotPoints(xc, yc, x, y):
    res = [
        [xc + x, yc + y],
        [xc - x, yc + y],
        [xc + x, yc - y],
        [xc - x, yc - y],
        [xc + y, yc + x],
        [xc - y, yc + x],
        [xc + y, yc - x],
        [xc - y, yc - x],
    ]
    return res

def lingkaran(xc, yc, radius):
    x = 0
    y = radius
    p = 1 - radius
    res = circlePlotPoints(xc, yc, x, y)
    while (x < y):
        x += 1
        if (p < 0):
            p += 2*x + 1
        else:
            y -= 1
            p += 2*(x-y) + 1

        res = np.concatenate(
            (
                res, circlePlotPoints(xc, yc, x, y)
            ), axis=0)
    return res

def ellips(xc, yc, Rx, Ry):
    x = 0
    y = Ry
    p = (Ry**2) - (Rx**2)*Ry + (0.25)*(Rx**2)
    res = ellipsePlotPoints(xc, yc, x, y)
    while ((2*(Ry**2)*x) < (2*(Rx**2)*y)):
        x += 1
        if (p < 0):
            p += (2*(Ry**2)*x) + (Ry**2)
        else:
            y -= 1
            p += (2*(Ry**2)*x) - (2*(Rx**2)*y) + (Ry**2)

        res = np.concatenate(
            (
                res, ellipsePlotPoints(xc, yc, x, y)
            ), axis=0)

    p = (Ry**2)*(x + 0.5)**2 + (Rx**2)*(y - 1)**2 - (Rx**2)*(Ry**2)
    while (y > 0):
        y -= 1
        if (p > 0):
            p -= (2*(Rx**2)*y) + (Rx**2)
        else:
            x += 1
            p += (2*(Ry**2)*x) - (2*(Rx**2)*y) + (Rx**2)

        res = np.concatenate(
            (
                res, ellipsePlotPoints(xc, yc, x, y)
            ), axis=0)

    return res