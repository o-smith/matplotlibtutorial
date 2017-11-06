import matplotlib

#Set up plot style
font = {'size'   : 16}
matplotlib.rc('font', **font)
matplotlib.rc('font', serif='Computer Modern Roman') 

#Define some additional colours
#London underground colours:
centralRed = '#DB2420' 
victoriaBlue = '#00A0E2' 
jubileeGrey = '#868F98' 
hammersmithBrown = '#F386A0'  
metroMagenta = '#97015E' 
bakerlooBrown= '#B05F0F' 
districtGreen = '#00843D' 

#Now some more colours that are visually distinct,
#good  for plots with multiple distinct lines
niceRed = "#%02x%02x%02x" %(194, 76, 81)
niceGreen = "#%02x%02x%02x" %(84, 166, 102)
niceBlue = "#%02x%02x%02x" %(76, 112, 176)
nicePurple = "#%02x%02x%02x" %(127, 112, 176) 
niceGold = "#%02x%02x%02x" %(204, 184, 115) 