# Hackzog-Wakeup-Bot

A simple ircbot in python wich starts a sound when someone writes !wakeup

# Install

- You need to install the package for `urllib`
- Start the bot with:   `python /path/to/bot.py`

# Setting it up

- Change the variables in the Code at the "Bot-config"
- Server is the IRC server you want to reach
- Channel ist the Channel you want to join
- Botnick is simply the name of the bot

server = "irc.freenode.net"
channel = "#test"
botnick =  "testbot12345"

# Fetures

- If the bot has no Connection he tests the internetconnection every 5minutes. If he can reach the network he starts to go online again.
- If the name of the bot ist already in use he start to set up his name with the timestamp at the end.
