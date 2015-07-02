Character attribute customizer
==============================
In Processing (Java mode)
---

* * *

I was experimenting with a platform that we could hipothetically use in our game.  
  
UPDATE: If you want to see how this looks like,
download and extract the folder from one of these two links and execute the "*Character_Attributes_Java*" executable.
* [For Windows 32bits](https://www.dropbox.com/sh/tkz7b00o4rbk8t7/AAC-qcTTtfyCmQsysvQ8d8W5a?dl=0)
* [For Linux 32bits](https://www.dropbox.com/sh/uczxnt9zz0prd0x/AACW-BFsIzyD8fhHOqKgC4NOa?dl=0)



# How to run this from the source:

You have two options:

* Using the PDE:
    1. Download the PDE at [processing.org](https://processing.org/download/?processing)
    2. Unzip the file, do whatever you want with it, and run the `processing` executable
    3. Try running this sketch by pressing that circular "Play" button
    4. You can also try File > Export Application (Ctrl+E) to see how the application looks like when delivered to the final user.

* Using the command line:
    1. Download and extract the PDE folder at [processing.org](https://processing.org/download/?processing)
    2. :  put the "*processing-java*" executable where you prefer, and try to execute it from the command line like this (not sure if this works):
    `$ processing-java --sketch=Character_Attributes_java --output=OUTPUT_FOLDER_NAME_HERE --force --run`  
The output folder is where the compiled sketch will be put. --force deletes that folder if it already exists so that you can run your sketch again with the same command. You can also export the final application by passing --export to the command.  
This article (http://www.dsfcode.com/using-processing-via-the-command-line/) has two useful bash functions to make developing with processing easier if you're using the terminal in Linux to run your sketches
