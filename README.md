## New-York-Stock-Exchange

# Objectives
Learn how to:

* read and parse simple XML files using the xml.etree.ElementTree module;
* deal with XML nodes and properties.

# Scenario
Download and open the nyse.xml file in your favorite text editor:

It's a small excerpt of the New York Stock Exchange quotes list. Take a look at it and analyze its structure. You need to do this as your task is to write a code which reads the data and presents it in a form similar to this one:

Command prompt -- Stock Exchange
![d5c9d8fdab2a93f7850ba157df246d81c366d647](https://github.com/user-attachments/assets/3edadb2b-9824-4bcc-b9fa-63e58a4cc5a8)


Hints:

1. don't forget to handle at least two possible exceptions: FileNotFoundError and xml.etree.ElementTree.ParseError;
2. feel free to improve and beautify the output — we know perfectly well that ours is not very sophisticated and rather ugly.
object.
