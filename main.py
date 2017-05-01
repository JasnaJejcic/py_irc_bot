# IRC Bot init file

# IMPORTS
import ConfigParser
import socket
import sys
import time
# Functions

# Main
## Initialize
Config = ConfigParser.ConfigParser()
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket

Options={}
Keywords={}

### Read the config file
print "Reading configuration"
Config.read("./config.ini")
CfgOptions = Config.options("main")
for option in CfgOptions:
    try:
        Options[option] = Config.get("main", option)
        if Options[option] == -1:
            DebugPrint("skip: %s" % option)
    except:
        print("exception on %s!" % option)
        Options[option] = None
### Verify config options are sane
### Initialize the keywords list
## Main Loop	
# while True:
	### Create connection, login and join channel
print "connecting to: "+Options["server"]
try:
	connection.connect((Options["server"], int(Options["port"])))
	print "Registering as User: %s" % "USER "+ Options["user"] +" "+ Options["nickname"] +" "+ Options["hostname"] +" :"+Options["comment"]
	connection.send("USER "+ Options["user"] +" "+ Options["nickname"] +" "+ Options["hostname"] +" :"+Options["comment"]+"\n") #user authentication
	print "Setting nickname to: %s" % Options["nickname"]
	connection.send("NICK "+ Options["nickname"] +"\n")                            # set nickname
	# connection.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth
	print "Joining channel: %s" % Options["channel"]
	connection.send("JOIN "+ Options["channel"] +"\n")        #join channel
	while True:
		text=connection.recv(2040)
		print text
		time.sleep(1)
except socket.error, exc:
		print "Caught exception socket.error : %s" % exc
		exit(1)




## Buffer reading block
### Check for keywords
### Reply if keywords

#21:43