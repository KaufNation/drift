import sys, pygame, math, random
pygame.init()

WIDTH = 320*2
HEIGHT = WIDTH

TICK_SIZE = .0002

MAX_RADIUS = 320

cur_theta = 0


size = width, height = WIDTH, HEIGHT
speed = [2, 2]
black = 0, 0, 0
grey = 127, 127, 127
white = 255, 255, 255
R, G, B = 25, 20, 15
dR, dG, dB = .001, .002, .003
#rad_change = .05

screen = pygame.display.set_mode(size)

#ball = pygame.image.load("intro_ball.gif")
#ballrect = ball.get_rect()

tick = 0
x = 0
cur_rad_mult = 0
rad_mult_growth = .00055
circ1_mult = 1
circ2_mult = math.pi/3
circ3_mult = math.pi/9
circ4_mult = math.pi/27

pygame.draw.circle(screen, white, (WIDTH/2,HEIGHT/2), WIDTH/2-10, 1)

def color(R, G, B, dR, dG, dB):
    R = R + dR
    G = G + dG
    B = B + dB
    if R > 255:
        R = 255
        dR = dR*-1
    if R < 0:
        R = 0
        dR = dR*-1
    if G > 255:
        G = 255
        dG = dG*-1
    if G < 0:
        G = 0
        dG = dG*-1
    if B > 255:
        B = 255
        dB = dB*-1
    if B < 0:
        B = 0
        dB = dB*-1
    return R, G, B, dR, dG, dB

a = random.randint(1,5)
b = random.randint(1,5)*20
c = b
d = a

def des(tick, count):
    if count == 0:
        j = 3
        k = 3
        a = 1
        b = 60
        c = 1
        d = 120

        return (math.cos(a*tick)-math.cos(b*tick)**j)*150, (math.sin(c*tick)-math.sin(d*tick)**k)*150

    elif count == 1:
        j = 3
        k = 4
        a = 1
        b = 60
        c = 1
        d = 120

        return (math.cos(a*tick)-math.cos(b*tick)**j)*140, (math.sin(c*tick)-math.sin(d*tick)**k)*140+HEIGHT/16

    elif count == 2:
        j = 3
        k = 3
        a = 80
        b = 1
        c = 1
        d = 80

        return (math.cos(a*tick)-math.cos(b*tick)**j)*150, (math.sin(c*tick)-math.sin(d*tick)**k)*150

    elif count == 3:
        j = 3
        k = 3
        a = 1
        b = 80
        c = 1
        d = 80

        return (math.cos(a*tick)-math.cos(b*tick)**j)*150, (math.sin(c*tick)-math.sin(d*tick)**k)*150

    elif count == 4:
        j = 3
        k = 4
        a = 1
        b = 80
        c = 80
        d = 80

        return (math.cos(a*tick)-math.cos(b*tick)**j)*140, (math.sin(c*tick)-math.sin(d*tick)**k)*140+HEIGHT/8

    elif count == 5:
        i = 1
        j = 2
        a = 1
        b = 60
        c = 1
        d = 1
        e = 60

        return (i*math.cos(a*tick)-math.cos(b*tick)*math.sin(c*tick))*100, (j*math.sin(d*tick)-math.sin(e*tick))*100

    elif count == 6:
        i = 1
        j = 2
        a = 80
        b = 1
        c = 2
        d = 1
        e = 80

        return (i*math.cos(a*tick)-math.cos(b*tick)*math.sin(c*tick))*100, (j*math.sin(d*tick)-math.sin(e*tick))*100

    elif count == 7:
        a = 1
        b = 6
        c = 14

        return (math.cos(a*tick)+math.cos(b*tick)/2+math.sin(c*tick)/3)*cur_rad_mult, (math.sin(a*tick)+math.sin(b*tick)/2+math.cos(c*tick)/3)*cur_rad_mult
    
    elif count == 8:
        a = 1
        b = 11
        c = 14

        return (math.cos(a*tick)+math.cos(b*tick)/2+math.sin(c*tick)/3)*cur_rad_mult, (math.sin(a*tick)+math.sin(b*tick)/2+math.cos(c*tick)/3)*cur_rad_mult

    elif count == 9:
        a = 1
        b = 16
        c = 14

        return (math.cos(a*tick)+math.cos(b*tick)/2+math.sin(c*tick)/3)*cur_rad_mult, (math.sin(a*tick)+math.sin(b*tick)/2+math.cos(c*tick)/3)*cur_rad_mult

    elif count == 10:
        a = 1
        b = 16
        c = 3

        return (math.cos(a*tick)+math.cos(b*tick)/2+math.sin(c*tick)/3)*cur_rad_mult, (math.sin(a*tick)+math.sin(b*tick)/2+math.cos(c*tick)/3)*cur_rad_mult

    elif count == 11:
        a = 16
        b = 16
        c = 7

        return (math.cos(a*tick)+math.cos(b*tick)/2+math.sin(c*tick)/3)*150, (math.sin(a*tick)+math.sin(b*tick)/2+math.cos(c*tick)/3)*150


def des2(tick, j, k, a ,b ,c ,d):

    return (math.cos(a*tick)-math.cos(b*tick)**j)*150, (math.sin(c*tick)-math.sin(d*tick)**k)*150

#def des3(tick, i. j, a ,b ,c ,d, e):

    #return (i*math.cos(a*tick)-math.cos(b*tick)*math.sin(c*tick))*100, (j*math.sin(d*tick)-math.sin(e*tick))*100

def wait(count):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                print("Saved design ", count)
                return True


count = 0

i = 1
j = 3
k = 3
a = 1
b = 60
c = 1
d = 120
e = 1

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #x1 = (math.sin(tick*circ1_mult))*cur_rad_mult/2
    #y1 = (math.cos(tick*circ1_mult))*cur_rad_mult/2
    #x1, y1 = des(tick, count%12)
    x1, y1 = des2(tick, j, k, a, b, c, d)
    #x1, y1 = des3(tick, i, j, a, b, c, d, e)

    #x2 = (math.sin(tick*circ2_mult))*cur_rad_mult/4
    #y2 = (math.cos(tick*circ2_mult))*cur_rad_mult/4

    #x3 = (math.sin(tick*circ3_mult))*cur_rad_mult/16
    #y3 = (math.cos(tick*circ3_mult))*cur_rad_mult/16

    #x4 = (math.sin(tick*circ4_mult))*cur_rad_mult/64
    #y4 = (math.cos(tick*circ4_mult))*cur_rad_mult/64

    #x3 = 0
    #y3 = 0

    #x4 = 0
    #y4 = 0

    #xpos = WIDTH/2+int(x1+x2+x3+x4)
    #ypos = HEIGHT/2+int(y1+y2+y3+y4)

    #xpos = WIDTH/2+int(x1)
    #ypos = HEIGHT/2+int(y1)
    xpos = WIDTH/2+int(x1.real)
    ypos = HEIGHT/2+int(y1.real)
    # - 11 for the buffer around the radius
    if (int(math.pow(x1.real*x1.real+y1.real*y1.real,0.5)) < MAX_RADIUS-11):
        pygame.draw.circle(screen, (R,G,B), (xpos,ypos), 1, 1)
    cur_rad_mult = cur_rad_mult + rad_mult_growth

    #if MAX_RADIUS > 320 or MAX_RADIUS < 0:
        #rad_change = rad_change*-1
        #MAX_RADIUS = MAX_RADIUS + rad_change

    #Makes color change over time
    #R, G, B, dR, dG, dB = color(R, G, B, dR, dG, dB)
    R, G, B = 255, 255, 255

    #ballrect = ballrect.move(speed)
    #if ballrect.left < 0 or ballrect.right > width:
    #    speed[0] = -speed[0]
    #if ballrect.top < 0 or ballrect.bottom > height:
    #    speed[1] = -speed[1]

    #screen.fill(black)
    #screen.blit(ball, ballrect)
    if (x >= 100000):
        #print((xpos),(ypos),MAX_RADIUS)
        #print((xpos-WIDTH/2)**2,(ypos-HEIGHT/2)**2,MAX_RADIUS**2)
        pygame.display.flip()
        print("design: ", count)
        #wait for key onput
        if (wait(count)):
            print("j: ", j, ", ","k: ", k, ", ","a: ", a, ", ","b: ", b, ", ","c: ", c, ", ","d: ", d)
            pygame.image.save(screen, "generated_design_%d%s" % (count,".jpeg"))
        screen.fill(black)
        pygame.draw.circle(screen, white, (WIDTH/2,HEIGHT/2), WIDTH/2-10, 1)
        x = 0
        cur_rad_mult = 0
        count = count + 1
        #for des2
        j = random.randrange(1,9,2)
        k = random.randrange(1,9,2)
        a = random.randrange(1,5,1)
        b = random.randrange(20,240,20)
        c = random.randrange(1,5,1)
        d = int(b*random.choice([.5,1,2]))
        #for des3
        #i = 1
        #j = 2
        #a = 1
        #b = 60
        #c = 1
       #d = 1
        #e = 60

    tick = tick + TICK_SIZE
    x = x + 1
