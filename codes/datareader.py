"""
An example script to read in data files called file_1, file_2 etc from
a directory called data/ and then plot them and save them each
as image files to a directory call frames/

This script is only meant as a template. Replace the file names 
and plotting commands as you require. 
"""


#These modules give your script the ability to navigate around your computer
import glob, os
import numpy as np 
import maplotlib.pyplot as plt 

#Location of the files to read in
searchDirectory = "data/"

#Now read the file names. If they are named as above you could 
#use the following command to read them in order
files = filter(os.path.isfile, glob.glob(searchDirectory + "file_*"))

#If their names are arbitrary and you don't care about their order, then
#use the following command instead (which I've commented out):
# files = filter(os.path.isfile, glob.glob(searchDirectory + "*"))

#If you want the files to be sorted according to modification date,
# then include the following command
files.sort(key=lambda x: os.path.getmtime(x))

#Plot all of these files as frames 
#This is the directory in which they'll be saved
targetDirectory = "frames/"
counter = 0
for f in files:

    #Name the file in which to save the plot
    fname = targetDirectory + "frame_%i.png" %counter
    
    try:
        #Now plot the contents of the file
        #These next two commands can be modified to plot the 
        #data in whichever way you want
        u = np.genfromtxt(f)
        plt.imshow(u, cmap='viridis') 
        plt.savefig(fname)
        
    #If any of the files are unreadble or unplottable
    #for some reason, then an error message will be 
    #spat out and the script will move onto the next file
    except Exception:
        print "\nError plotting file named %s" %f 
        continue
    
    counter += 1
