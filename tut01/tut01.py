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
#asking user for input
mod = int(input("Enter a value: "))
df.at[1,'octant ID']=mod

size = len(df['octant'])
t=0
#using a while loop to split the data in the given range
while(size>0):
    temp = mod
    if t == 0: #starting from value 0
        x = 0
    else:
        x = t*temp + 1 

    y = t*temp+mod
    if size<mod:
        mod = size
        size = 0
#inserting range and their corresponding data
t1 = str(x)
t2= str(y)
df.at[t+2,'octant ID'] = t1 +'-'+t2 
df1 = df.loc[x:y] 
df.at[t+2,'-1'] = df1['octant'].value_counts()[-1]
df.at[t+2,'1']  = df1['octant'].value_counts()[1]
df.at[t+2,'-2'] = df1['octant'].value_counts()[-2]
df.at[t+2,'2']  = df1['octant'].value_counts()[2]
df.at[t+2,'-3'] = df1['octant'].value_counts()[-3]
df.at[t+2,'3'] = df1['octant'].value_counts()[3]
df.at[t+2,'-4'] = df1['octant'].value_counts()[-4]
df.at[t+2,'4'] = df1['octant'].value_counts()[4]

 t = t + 1
size = size - mod

df.to_csv("octant_output.csv") #saving the file as output