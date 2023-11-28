import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900

zoom = [0,0]

delta = { 
    pg.K_UP: (0, -5), 
    pg.K_DOWN: (0, 5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (5, 0)
}


def check_bound(rct: pg.Rect) -> tuple[bool, bool]:
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:  
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:  
        tate = False
    return yoko, tate
                    

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    end_img = pg.image.load("ex02/fig/0.png")
    end_img = pg.transform.rotozoom(end_img, 0, 3.0)
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect() 
    kk_rct.center = 900, 400 
    bb_img = pg.Surface((20, 20))   
    bb_img.set_colorkey((0, 0, 0)) 
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10) 
    bb_rct = bb_img.get_rect()  
    bb_rct.centerx = random.randint(0, WIDTH)
    bb_rct.centery = random.randint(0, HEIGHT)
    vx, vy = +5, 5  

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, tpl in delta.items():
            if key_lst[k]:  
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]
        

        screen.blit(bg_img, [0, 0])

        screen.blit(kk_img,kk_rct)
        
        if kk_rct.colliderect(bb_rct):
            for i in range(100):
                screen.blit(bg_img, [0, 0])
                screen.blit(end_img,kk_rct)
                pg.display.update()
            print("Game Over")
            return


        kk_rct.move_ip(sum_mv[0], sum_mv[1])
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])


        bb_rct.move_ip(vx, vy) 
        yoko, tate = check_bound(bb_rct)
        if not yoko:  
            vx *= -1
        if not tate:  
            vy *= -1
        bb_rct.move_ip(vx, vy) 
        screen.blit(bb_img, bb_rct)
        
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()