# matplotlib tutorial 
---

This is a short matplotlib tutorial, presented as a Jupyter notebook.

## To view the tutorial

* Just click on ```tutorial.ipynb``` in this repository!

## To view this tutorial in interactive mode

* First, download Jupyter. In mac/linux, just type: ```pip install jupyter --user```.
* You may have to install pip first. 
* With Jupyter installed, download ```tutorial.ipynb``` from this Github repository, navigate to where you have saved in and type ```jupyter notebook``` in the command line.

## A note on using Python on Macs

 You may have problems installing things with pip in mac. This is because OSX is partially built with Python, and therefore the version of Python that Macs ship with is heavily system protected to prevent people bricking their computers.

What you should do is install your own version of python along side the systems default version. To do this, install brew and do ```brew install python```. Then type ```which -a python```. This should show you where the two versions of python live on your computer: the system's version, and your version. Once you've identified your version, place this in your path ahead of the system's version of python. Then restart the terminal. Now when you use python in the command line, it will be your version and you can install whatever you like to it including Jupyter. 
