# Libary Import
import socket
import urllib
import time
import sys
import random, string
import os
 
# bot config      
server = "irc.freenode.net"
channel = "#test"
botnick =  "testbot12345"
sicherung = 0
  
def tryconnect():
	hostname = "www.google.de" #example
	x=1

	while x==1:
		response = os.system("ping -c 1 " + hostname)
		#and then check the response...
		if response == 0:
			if x == 1:
				connect()
				x = 0
		time.sleep(500)	

def sendmsg(chan , msg): # Funktion Nachricht senden
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")
 
def joinchan(chan): # Funktion zum channel beitritt
  ircsock.send("JOIN "+ chan +"\n")
 
def hallo(): # Funktion welche Hello sendet
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")
  
def wakeup():
		print "test"
		urllib.urlopen('test.mp3')

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
	try:	
			ircsock.settimeout(300)
			ircmsg = ircsock.recv(1024)
			ircsock.settimeout(None) 
			
			if ircmsg.find ( 'Nickname is already in use' ) != -1:
        			botnick = botnick + str(time.time())
        			connect()
			
			ircmsg = ircmsg.strip('\n\r') 
			print(ircmsg)
			
			if ircmsg.find(":!hallo") != -1 & ircmsg.find("hackzog") == -1:
				hallo()

			if ircmsg.find(":!wakeup") != -1 & ircmsg.find("hackzog") == -1:
				if sicherung == 0:
					wakeup()
					sicherung = 1
				else:
					ircsock.send("PRIVMSG "+ channel +" :Einmal reicht doch du Schlingel!\n")
					sicherung = 0
				
		
			if ircmsg.find ( 'PING' ) != -1: #Ping/Pong um nicht gekickt zu werden
				ircsock.send ( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' )
				print ( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' )
				last_ping = time.time()
				
	except socket.timeout:
		print "timeout"
		tryconnect()
