#!/usr/bin/python

import cgi,sys,os,time,socket

form = cgi.FieldStorage()
sys.path.insert(0,"/usr/lib/python2.7/bridge/")
from bridgeclient import BridgeClient

# connection console socket #
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.settimeout(5)
#try:
#	s.connect(("localhost", 6571))
#except:
#	print "Unable to connect to the Arduino Console."
#	exit()
#print "Connected."
#############################

temps = float(form.getvalue("tempp"))
#s.send(temps+"\n")
client = BridgeClient()

# loop to store most recent 20 temp/humid values 
max_str = 20
ttt = client.get("temp")

# check whether "temp" exist #
try:
	k = len(ttt)		# if "temp" not exists, create "jjj" manually
except:
	ttt = [0]		# only for the first time when "temp" is not exist 	
	
jjj = ttt[0:len(ttt)-2]
if (len(jjj) < max_str):
	for num in range(len(jjj),20):	
		jjj.append(0)

jjj.insert(0,temps)			
ttt = jjj
client.put("temp",ttt);	# store the recent value
hhh = client.get("temp")

print "Content-type: text/plain"
print
try:
	for num in range(20):
		if (num < len(hhh)):
			print hhh[num]
##	print ttt
except:
	print "Error" 

#s.close()