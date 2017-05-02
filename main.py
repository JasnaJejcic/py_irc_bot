# IRC Bot init file

# IMPORTS
import ConfigParser
import socket
import sys
import time
# Functions

def check_for_keywords(text):
	pass
def system_output(msg):
	print time.strftime("%Y-%b-%d-%H:%M:%S", time.gmtime())+ " " + msg
# Main
## Initialize
Config = ConfigParser.ConfigParser()
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket

Options={}
Keywords={}

### Read the config file
system_output( "Reading configuration")
Config.read("./config.ini")
CfgOptions = Config.options("main")
for option in CfgOptions:
    try:
        Options[option] = Config.get("main", option)
        if Options[option] == -1:
            system_output("skip: %s" % option)
    except:
        system_output("exception on %s!" % option)
        Options[option] = None
### Verify config options are sane
### Initialize the keywords list
## Main Loop	
while True:
	### Create connection, login and join channel
	system_output( "connecting to: "+Options["server"])
	try:
		connection.connect((Options["server"], int(Options["port"])))
		system_output( "Registering as User: %s" % "USER "+ Options["user"] +" "+ Options["nickname"] +" "+ Options["hostname"] +" :"+Options["comment"])
		connection.send("USER "+ Options["user"] +" "+ Options["nickname"] +" "+ Options["hostname"] +" :"+Options["comment"]+"\n") #user authentication
		system_output( "Setting nickname to: %s" % Options["nickname"])
		connection.send("NICK "+ Options["nickname"] +"\n")                            # set nickname
		# connection.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth
		system_output( "Joining channel: %s" % Options["channel"])
		connection.send("JOIN "+ Options["channel"] +"\n")        #join channel
		# Connection established, begin checking for keywords
		while True:
			## Buffer reading block
			text=connection.recv(2040).split('\n')
			for line in text:
				system_output(line)
				### Check for keywords
				### Reply if keywords
				if line.startswith("PING"):
					system_output("PONG " + line.split()[1])
					connection.send("PONG " + line.split()[1] + "\n")
				# time.sleep(1)
	except socket.error, exc:
			system_output("Caught exception socket.error : %s" % exc)
			exit(1)
