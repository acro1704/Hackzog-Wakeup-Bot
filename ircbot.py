# Libary Import
import socket
import urllib
import time
import sys
import random, string

last_ping = time.time()
threshold = 5 * 60 # five minutes, make this whatever you want
 
# bot config      
server = # Server
channel = # Channel
botnick= # Botnickname
  
def sendmsg(chan , msg): # Funktion Nachricht senden
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")
 
def joinchan(chan): # Funktion zum channel beitritt
  ircsock.send("JOIN "+ chan +"\n")

def ledstart():
	#a script to blink led lights in space
 
def led(): # Funktion welche Hello sendet
  ledstart()
  
def wakeup():
		#starte sound vom Soundboard
		urllib.urlopen(#was aufgerufen werden soll)
		#sleep und wiederholung falls Boxen aus
		time.sleep(10)
		ledstart()
		urllib.urlopen(#was aufgerufen werden soll)

def connect():
	global ircsock
	ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ircsock.connect((server, 6667)) # Zum server verbinden mit dem port: 6667
	ircsock.send("USER guest 0 * :test\n") # bot initialisieren
	ircsock.send("NICK "+ botnick +"\n") # dem bot einen nick geben
	joinchan(channel) # den channel beitreten 
	ircsock.settimeout(300) # Timeout if connection get lost
	
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #open the socket	
connect() # connect function start

while 1: # Main While loop 
		try:	
			ircmsg = ircsock.recv(4096) #read a buffer of 4096 letters
			ircmsg = ircmsg.strip('\n\r')
						
			# If nickname is in use
			if ircmsg.find ( 'Nickname is already in use' ) != -1:
        			botnick = botnick + str(time.time())
        			connect()
			
			#If ircmsg doesent recive something (maybe offline)
			if len(ircmsg) == 0:
				print "Disconnected!"
        			connect() # reconnect
			
			#Another "offline-check"
			if (time.time() - last_ping) > threshold:
        			break
			
			#some debug prints
			print(ircmsg) 	
			print("jetzt")
			
			
			if ircmsg.find(":!led") != -1: # Ruft die Funktion led auf wenn jemand !led tippt
				led()

			if ircmsg.find(":!wakeup") != -1: # Ruft die Funktion wakeup auf wenn jemand !wakeup schreibt
				wakeup()
		
			if ircmsg.find ( 'PING' ) != -1: #Ping/Pong um nicht gekickt zu werden
				ircsock.send ( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' )
				print ( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' )
		
		#except versuch gegen timouts und errors		
		except socket.timeout:
			print("Timeout")
			connect()
		except socket.error:
			print("Timeout")
			connect()		
