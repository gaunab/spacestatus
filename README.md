Spacestatus
===========

This program returns the current state of your hackerspace by using the [space.api](http://spaceapi.net). It is meant to be included into 

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
