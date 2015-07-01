Character attribute customizer
==============================
In Processing Python
--------------------

* * *

I was experimenting with a platform that we could hipothetically use in our game.


# How to run this:

You have two options:

* Using the PDE:
    1. Download the PDE at [processing.org](https://processing.org/download/?processing)
    2. Unzip the file, do whatever you want with it, and run the `processing` executable
    3. Click on that rectangle that says "*Java*", and then click "*Add mode*"
    4. In the window that appears, click on the "*Install*" button of the Python mode
    5. When the installation finishes, close the PDE and open this file. Check if the PDE opens in the Python mode and try running this sketch by pressing that circular "Play" button
    6. You can also try File > Export Application (Ctrl+E) to see how the application looks like when delivered to the final user.

* Using the command line:
    1. You can download the command line utility here:  
       https://github.com/jdf/processing.py#processingpy
    2. Basically, the command that you'll end up writting in a Unix-y shell will be something like this (in this case, assuming that the *processing-py* folder was inside this sketch's folder and that our current working directory is inside the *processing-py* folder):  
    `$ ./processing-py.sh ../sketch_3relogios_Character_Attributes_python_pyde.py`

* * *

Now, talking about the advantages and disadvantages of using Processing Python for this project...

### The advantages:
 * It's Python
 * Processing is a library that makes drawing stuff and making things move *really* easy!
 * *Jycessing* = Python + Java + Processing
 * It allows us to export our programs to Windows, Mac OS and Linux

### What's not bat at all:
 * You're not stuck to the basic Processing PDE editor. They have a command line utility so that you can use the editor of your choice

### The disadvantages:
 * It uses the Java implementation of Python 2.7
 * Processing is a *Creative programming* library, not a *game development* one. That means that we'll have to implement ourselves a lot of the basic features that most game engines should provide, like Sprite classes, collision detection, game world entity management, scene handling, simple GUIs and all that stuff
 * It doesn't export to Android. For that we would have to code our sketches in the original Processing language (i.e. Java). But that is still quite easy to learn
 * The exported executable weights more than 40 MB and it takes years to start up, because it has to load and initialize the Jython library. But at least it displays a nice splash screen while it's loading that we can customize ourselves!


Although this is cool for making simulations with some tabs (i.e., files that are glued together in a big one when it is compiled)quickly, it doesn't seem to be the best solution to create complex projects with an intricate organization of modules and packages, something that we may need for this game.  
Alternatively, we could use the Java mode to create the graphical client for this game, as that allows us to create a pure Java project that uses the core.jar file which contains the Processing library. But that would require all of us to master this language decently so that we could use this platform confidently.
A big plus that we would get by using Java with the Processing library is that we could easily export our game to the Android platform. In the PDE, you just need to install the Android mode (and if I'm not wrong, the Android mode can download the Android SDK for you), plug in your phone, have good luck with the installation process of your smartphone's ADB driver, and then just press that Play button and the sketch will start runnning automatically in your phone. If it is a Java project, I think it is relatively easy to create an Android Project with the [Android Studio](https://developer.android.com/sdk/index.html) that is able to compile our project to an Android app without altering the code much and without much knowledge about Android app development with the official Android SDK.
