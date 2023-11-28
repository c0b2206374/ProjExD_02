import sys
import pygame as pg
import random 

WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0
    bom = pg.Surface((20, 20))
    pg.draw.circle(bom, (255, 0, 0), (10, 10), 10)
    bom.set_colorkey((0, 0, 0))
    bom_rct = bom.get_rect()
    bom_rct.centerx = random.randint(0, WIDTH)
    bom_rct.centery = random.randint(0, HEIGHT)
    vx,vy = +5,+5



    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])

        bom_rct.move_ip(vx,vy)
        screen.blit(bom,bom_rct)
        

        screen.blit(kk_img, [900, 400])
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()