import sys, pygame, random
from pygame.locals import *

pygame.init()
pygame.font.init()
random.seed()

'''
Global variables are here.
'''
totalTime = 0


'''
Base class for all enemies, extends the Sprite class.
'''
class Crvl(pygame.sprite.Sprite):
    def __init__(self, position, *args, **kwargs):
        super(Crvl, self).__init__(*args, **kwargs)
        self.rect = [position*32, 0, 32, 32]
        
'''
Real enemy classes start here.
'''
class Craval(Crvl):
    def __init__(self, *args, **kwargs):
        super(Craval, self).__init__(*args, **kwargs)
        self.image = pygame.image.load("craval.png")
        
        
    def update(self):
        if (totalTime%600 == 0): crv #craval.shoot

#Make more classes.

'''
Crvl groups start here.
'''
class CrvlManager(pygame.sprite.RenderUpdates):
    #def update(self):
    #    for crv in self.sprites():
    #        if (totalTime%600 == 0): crv #craval.shoot
    #        if (totalTime%500 == 0): crv #crevel.shoot
    #        if (totalTime%400 == 0): crv #crivil.shoot
    #        if (totalTime%300 == 0): crv #crovol.shoot
    #        if (totalTime%200 == 0): crv #cruvul.shoot
    #        if (totalTime%100 == 0): crv #cryvyl.shoot
    
    def newEnemy():
        
        self.add(Crvl())
        #Remove this code soon.
    
    

"""
Main execution starts here.
"""
screen = pygame.display.set_mode([640, 480])
screen.fill([192,192,192])
screen.blit(pygame.image.load("floor.png"), [0,416])
screen.blit(pygame.image.load("ceiling.png"), [0,32])
screen.blit(pygame.image.load("craval.png"), [224, 0])
screen.blit(pygame.image.load("crevel.png"), [256, 0])
screen.blit(pygame.image.load("crivil.png"), [288, 0])
screen.blit(pygame.image.load("crovol.png"), [320, 0])
screen.blit(pygame.image.load("cruvul.png"), [352, 0])
screen.blit(pygame.image.load("cryvyl.png"), [384, 0])
pygame.display.flip() #Try to update this to display.update soon so that this won't absolutely suck to reload.
newCrv = Craval(5)
print newCrv.rect
cm = CrvlManager()
cm.add(newCrv)
pygame.display.update(cm.draw(screen))
'''
FIND OUT WHY THE RENDERUPDATES ISN'T RENDERING UPDATES!?!?
'''

"""
Loop and updating starts here.
"""
while(1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #if event.type == pygame.MOUSEBUTTONDOWN: pygame.display.update([0,0,128,128])
    #screen.blit(pygame.image.load("ceiling.png"), [0,64])
    pygame.time.wait(10)
    