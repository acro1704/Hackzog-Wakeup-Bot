# Libary Import
import socket
import urllib
import time

 
# bot config      
server =  # Server
channel = # Channel
botnick = # Botnickname
 
def ping(): # Ping/Pong damit der bot nicht gekickt wird
  ircsock.send("PONG :pingis\n")  
 
def sendmsg(chan , msg): # Funktion Nachrichtsenden
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")
 
def joinchan(chan): # Funktion zum channel beitritt
  ircsock.send("JOIN "+ chan +"\n")
 
def hallo(): # Funktion welche Hello sendet
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")
  
def wakeup(): #Funktion zum aufrufen einer url (zb für musikplay)
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
    
  if ircmsg.find(":!wakeup") != -1: # Ruft die Funktion wakeup auf wenn jemand !wakeup schreibt
    wakeup()
    
  if ircmsg.find("PING :") != -1: # Ruft die Funktion ping auf um dem server zu antworten
    ping()
