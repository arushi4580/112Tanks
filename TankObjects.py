
import math

class Tank(object):
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.direction = [0, 0]
        self.speed = 5
        self.width = 60
        self.length = 50
        self.angle = angle
        self.arm = 50
        self.endOfArmX = self.x + self.arm * math.cos(math.radians(self.angle))
        self.endOfArmY = self.y + self.arm * math.sin(math.radians(self.angle))
    
    def move(self, screenWidth, screenHeight, margin, wall):
        if (self.x + (self.width // 2) <= screenWidth - margin or self.direction == [-1, 0] or self.direction[0] == 0)\
        and (self.x - (self.width // 2) >= margin or self.direction == [1, 0] or self.direction[0] == 0) \
        and (self.y + (self.length // 2) <= screenHeight - margin or self.direction == [0, -1] or self.direction[1] == 0) \
        and (self.y - (self.length // 2) >= margin or self.direction == [0, 1] or self.direction[1] == 0) and self.wallHit(wall):
            print(self.x, self.x - (self.width // 2), self.y, margin, screenWidth)
            self.x += self.speed * self.direction[0]
            self.y += self.speed * self.direction[1]
            self.endOfArmX = self.x + self.arm * math.cos(math.radians(self.angle))
            self.endOfArmY = self.y + self.arm * math.sin(math.radians(self.angle))
    
    def moveShooter(self, x, y):
        dx = x - self.x
        dy = y - self.y
        if dx == 0 and dy < 0:
            self.angle = 270
        elif dx == 0 and dy > 0:
            self.angle = 90
        else:
            self.angle = math.degrees(math.atan(dy / dx))
            if dx < 0:
                self.angle += 180
        self.endOfArmX = self.x + self.arm * math.cos(math.radians(self.angle))
        self.endOfArmY = self.y + self.arm * math.sin(math.radians(self.angle))
        
    # def hitsWall(self, wall):
    #     if not isinstance(wall, Wall):
    #         return False
    #     if ((wall.x2 >= self.x + (self.width // 2) >= wall.x1) and (wall.y2 >= self.y + (self.length // 2) >= wall.y1)) or ((wall.x1 <= self.x - (self.width // 2) <= wall.x2) and (wall.y2 >= self.y + (self.length // 2) >= wall.y1)) or ((wall.x2 >= self.x + (self.width // 2) >= wall.x1) and (wall.y2 >= self.y - (self.length // 2) >= wall.y1)) or ((wall.x1 <= self.x - (self.width // 2) <= wall.x2) and (wall.y2 >= self.y - (self.length // 2) >= wall.y1)):
    #         return True
    #     return False
    
    def wallHit(self, wall):
        if not isinstance(wall, Wall):
            return False
        # hits left side
        elif (wall.x2 >= self.x + (self.width / 2) >= wall.x1) and ((wall.y1 <= self.y + (self.length / 2) <= wall.y2) or (wall.y1 <= self.y - (self.length / 2) <= wall.y2)):
            print("hit left")
            if self.direction[0] == 1:
                return False
        # hits right side
        elif (wall.x2 >= self.x - (self.width / 2) >= wall.x1) and ((wall.y1 <= self.y + (self.length / 2) <= wall.y2) or (wall.y1 <= self.y - (self.length / 2) <= wall.y2)):
            print("hit top")
            if self.direction[0] == -1:
                return False
        # hits bottom side
        elif (wall.y1 <= self.y - (self.length / 2) <= wall.y2) and ((wall.x2 >= self.x + (self.width / 2) >= wall.x1) or (wall.x2 >= self.x - (self.width / 2) >= wall.x1)):
            print("hit bottom")
            if self.direction[1] == 1:
                print("wrong way")
                return False
        # hits top side
        elif (wall.y1 <= self.y - (self.length / 2) <= wall.y2) and ((wall.x2 >= self.x + (self.width / 2) >= wall.x1) or (wall.x2 >= self.x - (self.width / 2) >= wall.x1)):
            print("hit top")
            if self.direction[1] == -1:
                return False
        return True
    
    def draw(self, canvas, color = "orange"):
        canvas.create_rectangle(self.x - (self.width / 2), self.y - (self.length / 2), self.x + (self.width / 2), self.y + (self.length / 2), fill = color)
        canvas.create_oval(self.x - 12, self.y - 12, self.x + 12, self.y + 12, fill = color)
        canvas.create_line(self.x, self.y, self.x - 5 * math.cos(math.radians(self.angle)), self.y - 5 * math.sin(math.radians(self.angle)), fill = "black", width = 10)
        canvas.create_line(self.x, self.y, self.endOfArmX, self.endOfArmY, fill = "black", width = 10)


#### Types of Tanks ####

class DumbTank(Tank):
    def draw(self, canvas, color = "brown"):
        canvas.create_rectangle(self.x - (self.width / 2), self.y - (self.length / 2), self.x + (self.width / 2), self.y + (self.length / 2), fill = color)
        canvas.create_oval(self.x - 12, self.y - 12, self.x + 12, self.y + 12, fill = color)
        canvas.create_line(self.x, self.y, self.x - 5 * math.cos(math.radians(self.angle)), self.y - 5 * math.sin(math.radians(self.angle)), fill = "black", width = 10)
        canvas.create_line(self.x, self.y, self.endOfArmX, self.endOfArmY, fill = "black", width = 10)

#### Environment ####

class Wall(object):
    def __init__(self, x, y):
        self.cx = x
        self.cy = y
        self.length = 60
        self.x1 = self.cx - (self.length // 2)
        self.y1 = self.cy - (self.length // 2)
        self.x2 = self.cx + (self.length // 2)
        self.y2 = self.cy + (self.length // 2)
        print(self.x1, self.y1, self.x2, self.y2)
    
    def draw(self, canvas, color = "sienna4"):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = color)

#### Bullet Class ####

class Bullet(object):
    def __init__(self, x, y, angle):
        self.angle = angle
        self.speed = 10
        self.x = x
        self.y = y
        self.r = 5
        self.numWallsHit = 0
    
    def moveBullet(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed *math.sin(math.radians(self.angle))
    
    def reactToWallHit(self, screenWidth, screenHeight, margin):
        if self.x + self.r >= screenWidth - margin or self.x - self.r <= margin:
            self.angle = 180 - self.angle
            self.numWallsHit += 1
        elif self.y - self.r <= margin or self.y + self.r >= screenHeight - margin:
            self.angle = -self.angle
            self.numWallsHit += 1
    
    def hitsTank(self, tank):
        if not isinstance(tank, Tank):
            return False
        else:
            dist = math.sqrt((tank.x - self.x) ** 2 + (tank.y - self.y) ** 2)
            return dist < self.r + (tank.width / 2)
    
    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = "white")

#### Graphics Functions ####

from tkinter import *

# initializes the variables
def init(data):
    data.margin = 50
    data.tank = makeTank(400, 300, 0)
    data.gameTank = DumbTank(200, 200, 0)
    data.wall = Wall(500, 300)
    data.gameTanks = [data.gameTank]
    data.playerBullets = []
    data.gameTankBullets = []
    data.walls = [data.wall]
    data.timerCalls = 0

def makeTank(x, y, angle):
    tank = Tank(x, y, angle)
    return tank

def mousePressed(event, data):
    pass

def motion(event, data):
    x = event.x
    y = event.y
    data.tank.moveShooter(x, y)

def makeBullet(data, tank):
    return Bullet(tank.endOfArmX, tank.endOfArmY, tank.angle)

def keyPressed(event, data):
    if event.keysym == "space":
        data.playerBullets.append(makeBullet(data, data.tank))
    # for w in data.walls:
    #     if data.tank.hitsWall(w):
    if event.keysym == "Up":
        data.tank.direction = [0, -1]
    if event.keysym == "Down":
        data.tank.direction = [0, 1]
    if event.keysym == "Left":
        data.tank.direction = [-1, 0]
    if event.keysym == "Right":
        data.tank.direction = [1, 0]
    for wall in data.walls:
        data.tank.move(data.width, data.height, data.margin, wall)

def timerFired(data):
    data.timerCalls += 1
    for b in data.playerBullets:
        b.moveBullet()
        b.reactToWallHit(data.width, data.height, data.margin)
        if b.numWallsHit > 2:
            data.playerBullets.remove(b)
        for tank in data.gameTanks:
            if b.hitsTank(tank):
                data.gameTanks.remove(tank)
                data.playerBullets.remove(b)
    for b in data.gameTankBullets:
        b.moveBullet()
        b.reactToWallHit(data.width, data.height, data.margin)
        if b.numWallsHit > 2:
            data.gameTankBullets.remove(b)
        if b.hitsTank(data.tank):
            data.gameTankBullets.remove(b)
    data.gameTank.moveShooter(data.tank.x, data.tank.y)
    if data.timerCalls % 20 == 0:
        for tank in data.gameTanks:
            data.gameTankBullets.append(makeBullet(data, tank))
    
# draws the window
def redrawAll(canvas, data):
    canvas.create_rectangle(data.margin, data.margin, data.width - data.margin, data.height - data.margin, fill = "grey", width = 0)
    data.wall.draw(canvas)
    data.tank.draw(canvas)
    for tank in data.gameTanks:
        tank.draw(canvas)
    for b in data.playerBullets:
        b.draw(canvas)
    for b in data.gameTankBullets:
        b.draw(canvas)

#################################################################
# run function from class notes
#################################################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='black', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)
    
    def motionWrapper(event, canvas, data):
        motion(event, data)
        redrawAllWrapper(canvas, data)
    
    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind('<Motion>', lambda event:
                                motionWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 600)