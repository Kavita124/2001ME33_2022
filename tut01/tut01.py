import pandas as pd 
import numpy as np

#defining octane  
def oct(x,y,z):
    if x>0:
        if y>0:
            if z>0: 
                return 1 #octane 1
            else :
                return -1 #octane -1
        else:
            if z>0:
                return 4  #octane 4
            else :
                return -4 #octane -4
    else:
        if y>0:
            if z>0:
                return 2 #octane 2
            else :
                return -2 #octane -2
        else:
            if z>0:
                return 3 #octane 3
            else :
                return -3 #octane -3