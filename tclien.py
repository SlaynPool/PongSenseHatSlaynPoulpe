from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import socket


hote = "10.202.0.166"
port = 15556

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print( "Connection on {}".format(port))

sense = SenseHat()

def pushed_up(event):
    
    if event.action != ACTION_RELEASED:
        print("dhfkjqsh")
        socket.send("4".encode())        

def pushed_down(event):
    
    if event.action != ACTION_RELEASED:
        print("down")
        socket.send("2".encode())

def pushed_left(event):
   
    if event.action != ACTION_RELEASED:
        print("ldk")
        socket.send("3".encode())

def pushed_right(event):
    if event.action != ACTION_RELEASED:
        print("trze")
        socket.send("1".encode())
    

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right


pause()


print ("Close")
socket.close()

