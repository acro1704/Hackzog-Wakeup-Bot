# Libary Import
import socket
import urllib
import time
import sys
import random, string

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))
 
# bot config      
server = # Server
channel = # Channel
botnick1= #Name
botnick2 = randomword(5)
botnick= botnick1+botnick2	# Botnickname
  
def sendmsg(chan , msg): # Funktion Nachricht senden
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")
 
def joinchan(chan): # Funktion zum channel beitritt
  ircsock.send("JOIN "+ chan +"\n")
 
def hallo(): # Funktion welche Hello sendet
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")
  
def wakeup():
		#starte sound vom Soundboard
		urllib.urlopen(#was aufgerufen werden soll)
		#sleep und wiederholung falls Boxen aus
		time.sleep(10)
		urllib.urlopen(#was aufgerufen werden soll)

def connect():
	global ircsock
	ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ircsock.connect((server, 6667)) # Zum server verbinden mit dem port: 6667
	ircsock.send("USER guest 0 * :test\n") # bot initialisieren
	ircsock.send("NICK "+ botnick +"\n") # dem bot einen nick geben
	joinchan(channel) # den channel beitreten  	
	
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
connect()

while 1: # Vorsicht damit evt endlos schleife 
		try:	
			ircmsg = ircsock.recv(4096) 
			ircmsg = ircmsg.strip('\n\r') 
			print(ircmsg) 	
			print("jetzt")
			if ircmsg.find(":Hallo "+ botnick) != -1: # Ruft die Funktion Hallo auf wenn jemand Hallo botnick schreibt
				hallo()

			if ircmsg.find(":!wakeup") != -1: # Ruft die Funktion wakeup auf wenn jemand !wakeup schreibt
				wakeup()
		
			if ircmsg.find ( 'PING' ) != -1: #Ping/Pong um nicht gekickt zu werden
				ircsock.send ( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' )
				print ( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' )
				
		except socket.timeout:
			print("Timeout")
			connect()
		except socket.error:
			print("Timeout")
			connect()		
