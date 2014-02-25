Spacestatus
===========

This program returns the current state of your hackerspace by using the [space.api](http://spaceapi.net). 

Usage
-----

    ./spacestatus.py <YourSpaceName>

Example:

    ./spacestatus.py turmlabor

This will give return-status 0 if your Space is open, if your space is closed it will return 1.

Optional Parameters:

- `-d` or `--debug` print debugging informations

ToDo
----

1. error handling
-  implement older spaceapi-Versions
-  make spacenames case insensitive


Example in using
----------------

**As indicator for i3status**
in i3wm I use this script to indicate the status of my hackerspace:
 
    #! /bin/sh
    i3status | (read line && echo $line && read line && echo $line && while :
    do
      read line
      color="#FF0000"
      python $HOME/bin/spacestatus.py turmlabor &> /dev/null
      if [ $? -eq "0" ]; then
	  color="#00FF00"
      fi
      dat="[{ \"color\": \"${color}\", \"full_text\": \"Turmlabor\" },"
      echo "${line/[/$dat}" || exit 1
    done)

Place this script into your `$HOME/bin` and in your i3config set the `status_command` to this script.
