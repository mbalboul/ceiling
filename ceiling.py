import sys, pygame, random, math
from pygame.locals import *

pygame.init()
pygame.font.init()
random.seed()

"""
Global variables are here.
"""
totalTime = 0 #This is a simple time counter.
crvlManager = 0 #This is declared as a global variable so I can call it from within classes if need be.
bulletManager = 0 


"""
Base class for all enemies, extends the Sprite class.
"""
class Crvl(pygame.sprite.Sprite):
    def __init__(self, position, *args, **kwargs):
        super(Crvl, self).__init__(*args, **kwargs)
        self.rect = pygame.Rect(position*32, 0, 32, 32)
        
"""
Real enemy classes start here.
"""
class Craval(Crvl):
    def __init__(self, *args, **kwargs):
        super(Craval, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("craval.png")
        self.timer = 0
        for i in pygame.sprite.spritecollide(self, crvlManager, 1):
            i.kill()
        
    def update(self):
        self.timer += 1
        if (self.timer == 289): 
            bulletManager.add(Bullet(0, self.rect.centerx)) #craval.shoot
            '''
            #This is the cryvyl pattern.
            bulletManager.add(Bullet(-30, self.rect.centerx)) #craval.shoot
            bulletManager.add(Bullet(-45, self.rect.centerx)) #craval.shoot
            bulletManager.add(Bullet(-60, self.rect.centerx)) #craval.shoot
            bulletManager.add(Bullet(30, self.rect.centerx)) #craval.shoot
            bulletManager.add(Bullet(45, self.rect.centerx)) #craval.shoot
            bulletManager.add(Bullet(60, self.rect.centerx)) #craval.shoot
            '''
            '''
            #This is the cruvul pattern.
            bulletManager.add(Bullet(-45, self.rect.centerx)) #craval.shoot
            bulletManager.add(Bullet(-30, self.rect.centerx)) #craval.shoot
            bulletManager.add(Bullet(0, self.rect.centerx)) #craval.shoot
            bulletManager.add(Bullet(30, self.rect.centerx)) #craval.shoot
            bulletManager.add(Bullet(45, self.rect.centerx)) #craval.shoot
            '''
            self.timer = 0
            #print totalTime

class Crevel(Crvl):
    def __init__(self, *args, **kwargs):
        super(Crevel, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("crevel.png")
        self.timer = 0
        for i in pygame.sprite.spritecollide(self, crvlManager, 1):
            i.kill()
        
        
    def update(self):
        self.timer += 1
        if (self.timer == 289): 
            bulletManager.add(Bullet(-30, self.rect.centerx))
            bulletManager.add(Bullet(30, self.rect.centerx))
            self.timer = 0


class Crivil(Crvl):
    def __init__(self, *args, **kwargs):
        super(Crivil, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("crivil.png")
        self.timer = 0
        for i in pygame.sprite.spritecollide(self, crvlManager, 1):
            i.kill()
        
        
    def update(self):
        self.timer += 1
        if (self.timer == 289): 
            bulletManager.add(Bullet(0, self.rect.centerx))
            bulletManager.add(Bullet(-30, self.rect.centerx))
            bulletManager.add(Bullet(30, self.rect.centerx))
            self.timer = 0
            
    
class Crovol(Crvl):
    def __init__(self, *args, **kwargs):
        super(Crovol, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("crovol.png")
        self.timer = 0
        for i in pygame.sprite.spritecollide(self, crvlManager, 1):
            i.kill()
        
    def update(self):
        self.timer += 1
        if (self.timer == 289): 
            bulletManager.add(Bullet(-30, self.rect.centerx))
            bulletManager.add(Bullet(30, self.rect.centerx))
            bulletManager.add(Bullet(-45, self.rect.centerx))
            bulletManager.add(Bullet(45, self.rect.centerx))
            self.timer = 0


class Cruvul(Crvl):
    def __init__(self, *args, **kwargs):
        super(Cruvul, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("cruvul.png")
        self.timer = 0
        for i in pygame.sprite.spritecollide(self, crvlManager, 1):
            i.kill()
        
    def update(self):
        self.timer += 1
        if (self.timer == 289): 
            bulletManager.add(Bullet(0, self.rect.centerx))
            bulletManager.add(Bullet(-30, self.rect.centerx))
            bulletManager.add(Bullet(30, self.rect.centerx))
            bulletManager.add(Bullet(-45, self.rect.centerx))
            bulletManager.add(Bullet(45, self.rect.centerx))
            self.timer = 0
            
          
class Cryvyl(Crvl):
    def __init__(self, *args, **kwargs):
        super(Cryvyl, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("cryvyl.png")
        self.timer = 0
        for i in pygame.sprite.spritecollide(self, crvlManager, 1):
            i.kill()
        
    def update(self):
        self.timer += 1
        if (self.timer == 289): 
            bulletManager.add(Bullet(-30, self.rect.centerx))
            bulletManager.add(Bullet(30, self.rect.centerx))
            bulletManager.add(Bullet(-45, self.rect.centerx))
            bulletManager.add(Bullet(45, self.rect.centerx))
            bulletManager.add(Bullet(-60, self.rect.centerx))
            bulletManager.add(Bullet(60, self.rect.centerx))
            self.timer = 0
          
            
"""
This group manages Crvls.
"""
class CrvlManager(pygame.sprite.RenderUpdates):
    
    def newEnemy(self):
        lottery = random.randint(0,totalTime/100)
        if (lottery <= 1): self.add(Craval(random.randint(0,19)))
        elif (lottery <= 4): self.add(Crevel(random.randint(0,19)))
        elif (lottery <= 8): self.add(Crivil(random.randint(0,19)))
        elif (lottery <= 16): self.add(Crovol(random.randint(0,19)))
        elif (lottery <= 32): self.add(Cruvul(random.randint(0,19)))
        else: self.add(Cryvyl(random.randint(0,19)))
        #Open these up once you prepare the new enemies.
    

"""
Bullet sprite is here.  Note to self: Remember to incorporate sin and cosine functions.
"""
#This takes two parameters: angle and position.  Angle determines its velocity vector's direction, and
#Position determines where it is initially placed.
class Bullet(pygame.sprite.Sprite):
    def __init__(self, angle, position, *args, **kwargs):
        super(Bullet, self).__init__(*args, **kwargs)
        
        angle = angle*math.pi/180
        x_dis = position - 4 + (16*math.sin(angle))
        y_dis = 16 - (16*math.cos(angle))
        #print (angle)
        #print x_dis
        #print y_dis
        self.rect = pygame.Rect(x_dis, y_dis, 4, 4) #update this.
        self.x_velocity = 3.6 * math.sin(angle) #Sine is used because we are 90 degrees displaced from
        self.y_velocity = -5 * math.cos(angle) #the unit circle. Duh.
        self.acceleration = 0.45
        self.time = 0
        self.image = pygame.image.load("bullet.png")
        #print self.x_velocity
        #print self.y_velocity
        
    def update(self):
        self.rect = self.rect.move(self.x_velocity, self.y_velocity + self.acceleration*self.time) #Kinematics!
        self.time += 1
        #self.rect = pygame.Rect(32, 0, 4, 4)
        #print self.rect
        if self.rect.bottom > 640: self.kill()



"""
Main execution starts here.
"""
screen = pygame.display.set_mode([640, 480])
screen.fill([192,192,192])
screen.blit(pygame.image.load("floor.png"), [0,416])
screen.blit(pygame.image.load("ceiling.png"), [0,32])
pygame.display.flip()
crvlManager = CrvlManager() #THIS is where I turn the empty reference into something useful.
crvlManager.add(Craval(9.5))
bulletManager = pygame.sprite.RenderUpdates()

"""
Loop and updating starts here.
"""
while(1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #if event.type == pygame.MOUSEBUTTONDOWN: pygame.display.update([0,0,128,128])
    #screen.blit(pygame.image.load("ceiling.png"), [0,64])
    pygame.time.wait(10)
    totalTime += 1
    screen.fill([192,192,192])
    screen.blit(pygame.image.load("floor.png"), [0,416])
    screen.blit(pygame.image.load("ceiling.png"), [0,32])
    crvlManager.update()
    bulletManager.update()
    if (totalTime%100 == 0): crvlManager.newEnemy()
    pygame.display.update(crvlManager.draw(screen))
    pygame.display.update(bulletManager.draw(screen))
    