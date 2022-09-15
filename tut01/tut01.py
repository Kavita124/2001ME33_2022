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

#reading the input file
df = pd.read_csv("octant_input.csv") 

#editing excel file
df.at[0,'u_avg']=df['U'].mean() 
df.at[0,'v_avg']=df['V'].mean()
df.at[0,'w_avg']=df['W'].mean()

df['U-u_avg']=df['U']-df.at[0,'u_avg']
df['V-v_avg']=df['V']-df.at[0,'v_avg']
df['W-w_avg']=df['W']-df.at[0,'w_avg']

#making coloums
df['octant'] = df.apply(lambda x: oct(x['U-u_avg'], x['V-v_avg'], x['W-w_avg']),axis=1)

#one empty cell
df[' '] = ''
df.at[1,' '] = 'user input'

#counting octant in each row
df.at[0,'octant ID'] = 'overall count'
df.at[0,'1']  = df['octant'].value_counts()[1]
df.at[0,'-1'] = df['octant'].value_counts()[-1]
df.at[0,'2']  = df['octant'].value_counts()[2]
df.at[0,'-2'] = df['octant'].value_counts()[-2]
df.at[0,'3'] = df['octant'].value_counts()[3]
df.at[0,'-3'] = df['octant'].value_counts()[-3]
df.at[0,'4'] = df['octant'].value_counts()[4]
df.at[0,'-4'] = df['octant'].value_counts()[-4]