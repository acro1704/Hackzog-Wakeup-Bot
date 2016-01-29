# Libary Import
import socket
import urllib
import time
import sys
import random, string

# bot config      
server = server = # Server
channel = # Channel
botnick= # Botnickname
  
def sendmsg(chan , msg): # Funktion Nachricht senden
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")
 
def joinchan(chan): # Funktion zum channel beitritt
  ircsock.send("JOIN "+ chan +"\n")
 
def LED():
	#Some LED change stuff ask if you want kenw more about
  
def wakeup():
		
		#Soundboard starte sound
		urllib.urlopen('#Link zur Sound Steuerung')
	
		#Sleep falls boxen aus
		time.sleep(10)
		
		#LED Flackern
		LED()
	
		#Erneut WakeUpSound
		urllib.urlopen('#Link zur Sound Steuerung')

def connect():
	global ircsock
	ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ircsock.connect((server, 6667)) # Zum server verbinden mit dem port: 6667
	ircsock.send("USER guest 0 * :test\n") # bot initialisieren
	ircsock.send("NICK "+ botnick +"\n") # dem bot einen nick geben
	joinchan(channel) # den channel beitreten  	
	
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
ircsock.setblocking(0)
connect()

while 1: # Vorsicht damit evt endlos schleife 	
			ircsock.settimeout(300)
			ircmsg = ircsock.recv(1024)
			ircsock.settimeout(None) 
			
			if ircmsg.find ( 'Nickname is already in use' ) != -1:
        			botnick = botnick + str(time.time())
        			connect()

			if len(ircmsg) == 0:
				print "Disconnected!"
        			connect()
			
			ircmsg = ircmsg.strip('\n\r') 
			print(ircmsg)
			 	
			print("jetzt")
			
			if ircmsg.find(":!led") != -1 & ircmsg.find("hackzog") == -1: # Ruft die Funktion Hallo auf wenn jemand Hallo botnick schreibt
				LED()

			if ircmsg.find(":!wakeup") != -1 & ircmsg.find("hackzog") == -1: # Ruft die Funktion wakeup auf wenn jemand !wakeup schreibt
				wakeup()
		
			if ircmsg.find ( 'PING' ) != -1: #Ping/Pong um nicht gekickt zu werden
				ircsock.send ( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' )
				print ( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' )
				last_ping = time.time()
