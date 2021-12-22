"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"]=10
    data["cols"]=10
    data["boardsize"]=500
    data["cellsize"]=data["boardsize"]/data["rows"]
    data["userboard"]=emptyGrid(data["rows"],data["cols"])
    data["computerboard"]=emptyGrid(data["rows"],data["cols"])
    data["numberofships"] = 5
    data["computerboard"]=addShips(data["computerboard"] ,data["numberofships"])
    data["temporarygrid"]= test.testShip()
    return data



'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawShip(data, userCanvas, data["temporarygrid"])
    drawGrid(data, compCanvas, data["computerboard"], False)
    print(data["computerboard"])
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid = []
    for row in range(rows):
        grid.append([EMPTY_UNCLICKED]*cols)
    return grid


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    r = random.randint(1,8)
    c = random.randint(1,8)
    h_v = random.randint(0,1)
    if h_v == 0:
        ship = [[r-1,c],[r,c],[r+1,c]]
    else:
        ship = [[r,c-1],[r,c],[r,c+1]]
    return ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for i in ship:
        if grid[i[0]][i[1]] != EMPTY_UNCLICKED:
            return False
    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count = 0
    while count<numShips*3:
        x = createShip()
        y = checkShip(grid, x)
        if y :
            for i in x:
                grid[i[0]][i[1]] = SHIP_UNCLICKED
                count = count+1
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for i in range(10):
        for j in range(10):
            if grid[i][j]==2:
               canvas.create_rectangle(j*data["cellsize"], i*data["cellsize"], (j+1)*data["cellsize"], (i+1)*data["cellsize"],fill="yellow")
            else:
               canvas.create_rectangle(j*data["cellsize"], i*data["cellsize"], (j+1)*data["cellsize"], (i+1)*data["cellsize"],fill="blue")  
    return


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    ship.sort()
    for i in ship:        
        x = i[1]
        for j in ship:
            y = j[1]
            if i[0] == j[0] or i[0]== j[0]-1 or i[0] == j[0]-2:
                if x != y:           
                    return False
            else:
                return False
        return True


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    ship.sort()
    for i in ship:        
        x = i[0]
        for j in ship:
            y = j[0]
            if i[1] == j[1] or i[1]== j[1]-1 or i[1] == j[1]-2:
                if x != y:           
                    return False
            else:
                return False
        return True


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event): #[1,2] [1,3] [1,4]
    z=int(data["cellsize"])
    return [int(event.y/z),int(event.x/z)]


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    grid = data["userboard"]
    for i in ship:
        grid[i[0]][i[1]] = SHIP_CLICKED
    
    for i in range(10):
        for j in range(10):
            if grid[i][j]==SHIP_CLICKED:
                canvas.create_rectangle(j*data["cellsize"], i*data["cellsize"], (j+1)*data["cellsize"], (i+1)*data["cellsize"],fill="white")
            else:
                canvas.create_rectangle(j*data["cellsize"], i*data["cellsize"], (j+1)*data["cellsize"], (i+1)*data["cellsize"],fill="blue")
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    return


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    test.testDrawGrid()


    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
