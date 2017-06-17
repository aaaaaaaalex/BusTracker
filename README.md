# BusTracker
A Python script that monitors buses in Chicago using publicly-available data.

This was my first attempt at creating something useful using Python. The work is derived from an online lecture which outlines
how XML files could be taken from the web, and parsed for useful data.
This project contains a hardcoded x and y coordinate, representing the poosition of the user.
On a regular interval, the script refreshes the bus coordinates which it finds in an XML document on the web.
If a bus is approaching the user, it will prompt them as such. It will also print the coordinates of other related buses.
