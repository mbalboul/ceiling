#My high score with the 16x16 system is 7407... now 8063.
#New high score with the 24x24 system - 6142.

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
playerManager = 0
scoreFont = pygame.font.Font(None, 24)
death = 0 #Record the first death the player experiences by keeping track of it in the first place.


"""
Base class for all enemies, extends the Sprite class.
"""
class Trrt(pygame.sprite.Sprite):
    def __init__(self, position, *args, **kwargs):
        super(Trrt, self).__init__(*args, **kwargs)
        self.rect = pygame.Rect(position*32, 0, 32, 32)
        
"""
Real enemy classes start here.
"""
class Tarrat(Trrt):
    def __init__(self, *args, **kwargs):
        super(Tarrat, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("tarrat.png")
        self.timer = 0
        for i in pygame.sprite.spritecollide(self, crvlManager, 1):
            i.kill()
        
    def update(self):
        self.timer += 1
        if (self.timer == 289): 
            bulletManager.add(Bullet(0, self.rect.centerx)) #tarrat.shoot
            self.timer = 0
            #print totalTime

class Terret(Trrt):
    def __init__(self, *args, **kwargs):
        super(Terret, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("terret.png")
        self.timer = 0
        for i in pygame.sprite.spritecollide(self, crvlManager, 1):
            i.kill()
        
        
    def update(self):
        self.timer += 1
        if (self.timer == 289): 
            bulletManager.add(Bullet(-30, self.rect.centerx))
            bulletManager.add(Bullet(30, self.rect.centerx))
            self.timer = 0


class Tirrit(Trrt):
    def __init__(self, *args, **kwargs):
        super(Tirrit, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("tirrit.png")
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
            
    
class Torrot(Trrt):
    def __init__(self, *args, **kwargs):
        super(Torrot, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("torrot.png")
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


class Turrut(Trrt):
    def __init__(self, *args, **kwargs):
        super(Turrut, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("turrut.png")
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
            
          
class Tyrryt(Trrt):
    def __init__(self, *args, **kwargs):
        super(Tyrryt, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("tyrryt.png")
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
          
          
class Tzrrzt(Trrt):
    def __init__(self, *args, **kwargs):
        super(Tzrrzt, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("tzrrzt.png")
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
            bulletManager.add(Bullet(-60, self.rect.centerx))
            bulletManager.add(Bullet(60, self.rect.centerx))
            self.timer = 0

class Terror(Trrt):
    def __init__(self, *args, **kwargs):
        super(Terror, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("tzrrzt.png")
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
            bulletManager.add(Bullet(-60, self.rect.centerx))
            bulletManager.add(Bullet(60, self.rect.centerx))
            bulletManager.add(Bullet(-90, self.rect.centerx))
            bulletManager.add(Bullet(90, self.rect.centerx))
            self.timer = 0
            
            
"""
This group manages Trrts. Consider renaming Trrts?
"""
class TrrtManager(pygame.sprite.RenderUpdates):
    
    def newEnemy(self):
        lottery = random.randint(0,totalTime/100)
        """
        #Archaic addition pattern - replaced by more even distribution.
        if (lottery <= 1): self.add(Tarrat(random.randint(0,19)))
        elif (lottery <= 4): self.add(Terret(random.randint(0,19)))
        elif (lottery <= 8): self.add(Tirrit(random.randint(0,19)))
        elif (lottery <= 16): self.add(Torrot(random.randint(0,19)))
        elif (lottery <= 32): self.add(Turrut(random.randint(0,19)))
        elif (lottery <= 64): self.add(Tyrryt(random.randint(0,19)))
        else: self.add(Tzrrzt(random.randint(0,19)))
        """
        
        #Fast addition pattern - new enemies are added kind of fast.
        if (lottery < 5): self.add(Tarrat(random.randint(0,19)))
        elif (lottery < 11): self.add(Terret(random.randint(0,19)))
        elif (lottery < 18): self.add(Tirrit(random.randint(0,19)))
        elif (lottery < 26): self.add(Torrot(random.randint(0,19)))
        elif (lottery < 35): self.add(Turrut(random.randint(0,19)))
        elif (lottery < 45): self.add(Tyrryt(random.randint(0,19)))
        else: self.add(Tzrrzt(random.randint(0,19)))
        
        """
        #Totally random pattern - any enemy can be added randomly.
        lottery = random.randint(0,7)
        if (lottery == 0): self.add(Tarrat(random.randint(0,19)))
        elif (lottery == 1): self.add(Terret(random.randint(0,19)))
        elif (lottery == 2): self.add(Tirrit(random.randint(0,19)))
        elif (lottery == 3): self.add(Torrot(random.randint(0,19)))
        elif (lottery == 4): self.add(Turrut(random.randint(0,19)))
        elif (lottery == 5): self.add(Tyrryt(random.randint(0,19)))
        else: self.add(Tzrrzt(random.randint(0,19)))
        """
        """
        #Super easy mode - easy enemies added most commonly, hard most rarely.
        lottery = random.randint(0,127)
        if (lottery < 64): self.add(Tarrat(random.randint(0,19)))
        elif (lottery < 96): self.add(Terret(random.randint(0,19)))
        elif (lottery < 112): self.add(Tirrit(random.randint(0,19)))
        elif (lottery < 120): self.add(Torrot(random.randint(0,19)))
        elif (lottery < 124): self.add(Turrut(random.randint(0,19)))
        elif (lottery < 126): self.add(Tyrryt(random.randint(0,19)))
        else: self.add(Tzrrzt(random.randint(0,19)))
        """
        
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
Player character sprite.
"""
class Player(pygame.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("player_24.png")
        self.rect = pygame.Rect(312, 392, 24, 24)
        self.speed = 0 #This parameter is changed as speed is changed - update handles the actual movement.
        
    def left(self):
        self.speed -= 8
        
    def right(self):
        self.speed += 8
        
    def update(self):
        if (self.rect.right>=639) and (self.speed>0): return #character shouldn't move offscreen
        elif (self.rect.left<=0) and (self.speed<0): return #character shouldn't move offscreen
        else: self.rect = self.rect.move(self.speed,0) #character won't move offscreen

"""
Main execution starts here.
"""
screen = pygame.display.set_mode([640, 480])
screen.fill([192,192,192])
screen.blit(pygame.image.load("floor.png"), [0,416])
screen.blit(pygame.image.load("ceiling.png"), [0,32])
pygame.display.flip()
crvlManager = TrrtManager() #THIS is where I turn the empty reference into something useful.
crvlManager.add(Tarrat(9.5))
bulletManager = pygame.sprite.RenderUpdates()
playerManager = pygame.sprite.RenderUpdates()
player = Player()
playerManager.add(player)

"""
Loop and updating starts here.
"""
while(1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #if event.type == pygame.MOUSEBUTTONDOWN: pygame.display.update([0,0,128,128])
        if event.type == pygame.KEYDOWN:
            if event.dict['key'] == pygame.K_LEFT: #276 means the left key on the keyboard. 275 is right.
                player.left()
            elif event.dict['key'] == pygame.K_RIGHT:
                player.right()
        if event.type == pygame.KEYUP:
            if event.dict['key'] == pygame.K_LEFT: player.right()
            elif event.dict['key'] == pygame.K_RIGHT: player.left()
    #screen.blit(pygame.image.load("ceiling.png"), [0,64])
    pygame.time.wait(10)
    totalTime += 1
    screen.fill([192,192,192])
    screen.blit(pygame.image.load("floor.png"), [0,416])
    screen.blit(pygame.image.load("ceiling.png"), [0,32])
    crvlManager.update()
    bulletManager.update()
    playerManager.update()
    screen.blit(scoreFont.render(format(totalTime), 0, [255,255,255]), [0,80])
    if (death != 0): screen.blit(scoreFont.render(deathstring, 0, [255,255,255]), [0,64])
    if (totalTime%100 == 0): crvlManager.newEnemy()
    pygame.display.update(crvlManager.draw(screen))
    pygame.display.update(bulletManager.draw(screen))
    pygame.display.update(playerManager.draw(screen))
    pygame.display.update([0,64,480,32])
    
    if pygame.sprite.spritecollideany(player, bulletManager):
        print totalTime #Implement a soft-death hard-death score system for the character
        if (death == 0):
            death = 1
            deathstring = "You died at "+format(totalTime)+"."
            player.image = pygame.image.load("player_doom.png") #Consider multiplying colors by 4 instead of 3?
    