import socket
from sense_hat import SenseHat
sense= SenseHat()
sense.clear()

def setupled():
    pos = [4,4]
    sense.set_pixel(pos[0],pos[1], 255,0,0)
    return pos

def moveled( action , pos ):
    print( "hello"+ str(action) +" " +str(pos[0])+":"+str(pos[1]))
    if int(action) == 1: # droite
        pos[0]+=1
        return pos
    elif int(action) == 2:#bas
        pos[1] -= 1
        return pos
    elif int(action) == 3: #gauche 
        pos[0]-=1
        return pos
    elif int(action) == 4: #haut
        pos[1]+=1
        return pos
    else: 
        return pos
def do(pos):
    sense.clear()
    sense.set_pixel(pos[0],pos[1],255,0,0)


#Creationb du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15556))
pos = setupled()
socket.listen(5)
client, address = socket.accept()
while True:
        socket.listen(5)
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

