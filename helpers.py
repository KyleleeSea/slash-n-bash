from cmu_112_graphics import *
import decimal

def cutSpritesheet(startX, adjW, w, startY, endY, spritesheet, app):
    animation = spritesheet.crop((startX+adjW, startY, (w-startX)+adjW, endY))
    return app.scaleImage(animation, (((7/8)*app.height)//128))

def cutEnemySheet(startX, adjW, w, startY, endY, spritesheet, app):
    animation = spritesheet.crop((startX+adjW, startY, (w-startX)+adjW, endY))
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#flipImage
    # Using transpose to flip an image
    animation = animation.transpose(Image.FLIP_LEFT_RIGHT)
    return app.scaleImage(animation, ((1.2*app.height)//128))

def getYs(row):
    return (128*row, 128*(row+1))

def rotateList(L, n=2):
    return L[n:] + L[0:n]

# 1 corresponds to dmg, 2 to blockEff, 3 to vulnerability status
def createCombatTuple(frame):
    return (frame[1], frame[2], frame[3])