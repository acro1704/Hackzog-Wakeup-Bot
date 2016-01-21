# This bot is a result of a tutorial covered on http://shellium.org/wiki.\n
# Importiere die socket libary
import socket
import urllib
import time

 
# bot config      
server =  # Server
channel = # Channel
botnick = # Your bots nick
 
def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send("PONG :pingis\n")  
 
def sendmsg(chan , msg): # Eine Funktion um zb eine Nachricht zu senden
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")
 
def joinchan(chan): # Funktion zum channel beitritt
  ircsock.send("JOIN "+ chan +"\n")
 
def hallo(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")
  
def wakeup():
	urllib.urlopen('*Here URL for Musik launch*')
                 
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Zum server verbinden mit dem port: 6667
ircsock.send("USER guest 0 * :test\n") # bot initialisieren
ircsock.send("NICK "+ botnick +"\n") # dem bot einen nick geben
 
joinchan(channel) # den channel beitreten
 
while 1: # Vorsicht damit evt endlos schleife
  ircmsg = ircsock.recv(2048) # server daten bekommen
  ircmsg = ircmsg.strip('\n\r') # loesche leerzeilen
  print(ircmsg) # ausgeben was vom server kommt
 
  if ircmsg.find(":Hallo "+ botnick) != -1: # Ruft die Funktion Hallo auf wenn jemand Hallo botnick schreibt
    hallo()
    
  if ircmsg.find(":!wakeup") != -1: # Ruft die Funktion Hallo auf wenn jemand Hallo botnick schreibt
    wakeup()
    
  if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
    ping()
