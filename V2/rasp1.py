from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import socket
import time
sense = SenseHat()



hote = "10.202.0.51"
port = 15556

def setupled():
    pos = [4,4]
    sense.clear()
    sense.set_pixel(3,0, 0,255,0)
    sense.set_pixel(4,0, 0,255,0)
    sense.set_pixel(2,1, 0,255,0)
    sense.set_pixel(5,1, 0,255,0)
    sense.set_pixel(2,2, 0,255,0)
    sense.set_pixel(5,2, 0,255,0)
    sense.set_pixel(2,3, 0,255,0)
    sense.set_pixel(5,3, 0,255,0)
    sense.set_pixel(1,4, 0,255,0)
    sense.set_pixel(2,4, 0,255,0)
    sense.set_pixel(5,4, 0,255,0)
    sense.set_pixel(6,4, 0,255,0)
    sense.set_pixel(0,5, 0,255,0)
    sense.set_pixel(7,5, 0,255,0)
    sense.set_pixel(0,6, 0,255,0)
    sense.set_pixel(7,6, 0,255,0)
    sense.set_pixel(1,7, 0,255,0)
    sense.set_pixel(2,7, 0,255,0)
    sense.set_pixel(5,7, 0,255,0)
    sense.set_pixel(6,7, 0,255,0)

    return pos


#Creationb du socket
socketTX = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketTX.bind(('', 15557))
pos = setupled()
print(" a")
socketTX.listen(5)
print("b")
client, address = socketTX.accept()
print("c")
time.sleep(2)


socketRX = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketRX.connect((hote, port))
print( "Connection on {}".format(port))
def pushed_up(event):
    
    if event.action != ACTION_RELEASED:
        socketRX.send("4".encode())        

def pushed_down(event):
    
    if event.action != ACTION_RELEASED:
        socketRX.send("2".encode())

def pushed_left(event):
   
    if event.action != ACTION_RELEASED:
        socketRX.send("3".encode())

def pushed_right(event):
    if event.action != ACTION_RELEASED:
        socketRX.send("1".encode())
def pushed_middle(event):
    if event.action == ACTION_PRESSED:
        socketRX.send("0".encode())    

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle
#----------------------------------------------------------------------#
def moveled( action , pos ):
    print( "hello"+ str(action) +" " +str(pos[0])+":"+str(pos[1]))
    if int(action) == 1: # droite
        if pos[0]+1 > 7:
            pos[0] = 0
        else:
            pos[0]+=1
        return pos
    elif int(action) == 2:#bas
        if pos[1]-1 < 0:
            pos[1] = 7
        else :
            pos[1] -= 1
        return pos
    elif int(action) == 3: #gauche 
        if pos[0]-1 < 0:
            pos[0] = 7
        else:
            pos[0]-=1
        return pos
    elif int(action) == 4: #haut
        if pos[1]+1>7:
            pos[1] = 0
        else:
            pos[1]+=1
        return pos
    elif int(action) == 0:
        pos[0] = 4
        pos[1] = 4
        sense.clear()
        sense.set_pixel(3,0, 0,255,0)
        sense.set_pixel(4,0, 0,255,0)
        sense.set_pixel(2,1, 0,255,0)
        sense.set_pixel(5,1, 0,255,0)
        sense.set_pixel(2,2, 0,255,0)
        sense.set_pixel(5,2, 0,255,0)
        sense.set_pixel(2,3, 0,255,0)
        sense.set_pixel(5,3, 0,255,0)
        sense.set_pixel(1,4, 0,255,0)
        sense.set_pixel(2,4, 0,255,0)
        sense.set_pixel(5,4, 0,255,0)
        sense.set_pixel(6,4, 0,255,0)
        sense.set_pixel(0,5, 0,255,0)
        sense.set_pixel(7,5, 0,255,0)
        sense.set_pixel(0,6, 0,255,0)
        sense.set_pixel(7,6, 0,255,0)
        sense.set_pixel(1,7, 0,255,0)
        sense.set_pixel(2,7, 0,255,0)
        sense.set_pixel(5,7, 0,255,0)
        sense.set_pixel(6,7, 0,255,0)
        time.sleep(2)

        return pos
    else: 
        return pos
def do(pos):
    sense.clear()
    sense.set_pixel(pos[0],pos[1],255,0,0)


while True:
        socketTX.listen(5)
        #print ("{} connected".format( address ))

        response = client.recv(255)
        if response != "":
            print("bite")
            print(response.decode())
            pos = moveled( response.decode(), pos)        
            do(pos)

        print(pos)

print ("Close")
client.close()
stock.close()

pause()


