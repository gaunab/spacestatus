#! env python


### 
#  Spacestatus.py
#  This Script gives the current State of your hackerspace
#  Returns 0 if space is open, 1 if space is closed
#  Ver. 0.1 First Version without any error-Handling


import json
import urllib2
import optparse
import sys

DEBUG = False

def getSpaceName():                      # Decode Program Params
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    name = args[0]
    return name

def main():
    spaceapi = urllib2.urlopen("http://spaceapi.net/directory.json").read() # Fetch th url of the spaceapi.json file
    spaceurl = json.loads(spaceapi)[getSpaceName()]                         # provided by the hackerspaces
    if DEBUG:
        print("Found URL for Hackerspace: %s") %(spaceurl)

    spacestate = urllib2.urlopen(spaceurl).read()                           # Fetch Data from the Space
    api = json.loads(spacestate)['api']
    if DEBUG:
        print("Space has API-Version %s") %(api)
    if api == "0.12":
        state = json.loads(spacestate)['open']
    if api == "0.13":
        state = json.loads(spacestate)['state']['open']                           # Return the current State
    
    if DEBUG:
        print ("Found current open state: %s") %(state)

    if state == False:
        return 1
    else: 
        return 0

if __name__ == "__main__" :
    parser = optparse.OptionParser("usage: %prog <SpaceName>")
    parser.add_option("-d","--debug",help="show debug information",dest="debugging",default=False,action="store_true")
    (options, args) = parser.parse_args()
    DEBUG = options.debugging
    
    sys.exit(main())
