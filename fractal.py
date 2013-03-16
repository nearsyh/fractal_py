import sys
import pygame
import random
pygame.init()

width = 800
height = 800
iteration = 100
zoom = 250.0

all_colors = pygame.Surface((width, height), depth=24)
all_colors2 = pygame.Surface((width, height), depth=24)

def nextZ(z, c):
    z_r, z_i = z
    c_r, c_i = c
    zn_r = z_r * z_r - z_i * z_i + c_r
    zn_i = 2 * z_r * z_i + c_i
    return (zn_r, zn_i)

def length(z):
    z_r, z_i = z
    return z_r * z_r + z_i * z_i

for x in range(-width/2, width/2):
    for y in range(-height/2, height/2):
        z_init = (0, 0)
        value = 1.0
        for n in range(0, iteration):
            z_init = nextZ(z_init, (x/zoom, y/zoom))
            if length(z_init) > 4:
                value = value * n / iteration
                break
        all_colors.set_at((x + width/2, y + height/2), (255 * value, 255 * value, 255 * value))
    sys.stdout.write("Mandelbrot : %d%%\r" % ((x + width/2) * 100 / width))
    sys.stdout.flush()
pygame.image.save(all_colors, "mandelbrot.jpg")
sys.stdout.write("Mandelbrot : %d%%\n" % (100))

c = (0.285, 0.01)
for x in range(-width/2, width/2):
    for y in range(-height/2, height/2):
        z_init = (x/zoom, y/zoom)
        value = 1.0
        for n in range(0, iteration):
            z_init = nextZ(z_init, c)
            if length(z_init) > 4:
                value = 1.0 * n / iteration
                break
        all_colors2.set_at((x + width/2, y + height/2), (255 * value, 255 * value, 255 * value))
    sys.stdout.write("Julia : %d%%\r" % ((x + width/2) * 100 / width))
    sys.stdout.flush()
pygame.image.save(all_colors2, "julia.jpg")
sys.stdout.write("Julia : %d%%\n" % (100))
