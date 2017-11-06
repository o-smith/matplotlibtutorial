# matplotlib tutorial 

This is a short matplotlib tutorial, presented as a Jupyter notebook.

## To view the tutorial

* Just click on ```tutorial.ipynb``` in this repository!
* Alternatively, open up the html verion of the tutorial in your browser.

## To view this tutorial in interactive mode

* First, download Jupyter. In mac/linux, just type: ```pip install jupyter --user```.
* With Jupyter installed, download ```tutorial.ipynb``` from this Github repository, navigate to where you have saved in and type ```jupyter notebook``` in the command line.

## Included codes

In the ```codes``` folder, you'll find some of the code from the tutorial.

* ```stylemodule.py``` sets some parameters for you to make plots look better, as well as defining some custom colours that you can use in your plots. To inclue this in your plots, just put ```import stylemodule``` at the beginning of any of your scripts.
* ```bifurcation.py``` is a script to plot bifurcation plots. It is just meant as a template. It's usage is examplained in the tutorial.
* ```datareader.py``` will read files in a directory, open them up one by on, plot them and then save the resulting image files in another directory. Again, just meant as a template -- replace relevant filenames with whatever you need etc.

## A note on using Python on a mac

 You may have problems installing things with pip in mac. This is because OSX is partially built with Python, and therefore the version of Python that macs ship with is heavily system protected in order to prevent people bricking their computers.

What you should do is install your own version of python along side the system's default version. To do this, install brew and do ```brew install python```. Once installed, type ```which -a python``` to see where your new version of python lives on your computer, as well as where the system's version lives. Once you've identified the location of your new version, place this location in your path ahead of the system's version. Then restart the terminal. Now when you use python in the command line, it will be your version and you can install whatever you like to it, including Jupyter. 
