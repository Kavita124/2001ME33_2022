from ast import Str
from cmath import nan
from lib2to3.pytree import type_repr
import os
from csv import writer
from csv import reader
from traceback import print_tb
import pandas as pd

# from tut03.tut03 import octant
os.system('cls')
# os.system('clear')


df = pd.read_excel(r'/content/input_octant_transition_identify.xlsx')  
# adding the values for avarage
x1average=df['x'].mean()
y1average=df['y'].mean()
z1average=df['z'].mean()

df.at[0,'xaverage']=x1average
df.at[0,'yaverage']=y1average
df.at[0,'zaverage']=z1average
n=len(df.axes[0])
print(n,type(n))
#  finding the values of "y'=y - y avg" and insert in outfile using" db.at" function
for i in range(0,n):
    df.at[i,'xaverage=x - x avg']=df['x'][i]-x1average
for i in range(0,n):
    df.at[i,'yaverage=y - y avg']=df['y'][i]-y1average
for i in range(0,n):
    df.at[i,'zaverage=z - z avg']=df['z'][i]-z1average


octant=[]



# finding the value of octant ans insert in output file
try:
    for i in range(0,n):
        if(df.at[i,'xaverage=x - x avg']>0 and df.at[i,'yaverage=y - y avg']>0 and df.at[i,'zaverage=z - z avg']>0):
            df.at[i,"Octant"]=1
            octant.append(df.at[i,'Octant'])
            
        if(df.at[i,'xaverage=x - x avg']>0 and df.at[i,'yaverage=y - y avg']>0 and df.at[i,'zaverage=z - z avg']<0):
            df.at[i,'Octant']=-1
            octant.append(df.at[i,'Octant'])
            
        if(df.at[i,'xaverage=x - x avg']<0 and df.at[i,'yaverage=y - y avg']>0 and df.at[i,'zaverage=z - z avg']>0):
            df.at[i,'Octant']=2
            octant.append(df.at[i,'Octant'])
            
        if(df.at[i,'xaverage=x - x avg']<0 and df.at[i,'yaverage=y - y avg']>0 and df.at[i,'zaverage=z - z avg']<0):
            df.at[i,'Octant']=-2
            octant.append(df.at[i,'Octant'])
            
        if(df.at[i,'xaverage=x - x avg']<0 and df.at[i,'yaverage=y - y avg']<0 and df.at[i,'zaverage=z - z avg']>0):
            df.at[i,'Octant']=3
            octant.append(df.at[i,'Octant'])
            
        if(df.at[i,'xaverage=x - x avg']<0 and df.at[i,'yaverage=y - y avg']<0 and df.at[i,'zaverage=z - z avg']<0):
                df.at[i,'Octant']=-3
                octant.append(df.at[i,'Octant'])
            
        if(df.at[i,'xaverage=x - x avg']>0 and df.at[i,'yaverage=y - y avg']<0 and df.at[i,'zaverage=z - z avg']>0):
            df.at[i,'Octant']=4
            octant.append(df.at[i,'Octant'])
            
        if(df.at[i,'xaverage=x - x avg']>0 and df.at[i,'yaverage=y - y avg']<0 and df.at[i,'zaverage=z - z avg']<0):
                df.at[i,'Octant']=-4
                octant.append(df.at[i,'Octant'])
except:
    print("octant not found")    


  
df.at[2,' '] ='User input'      
df.at[0,'Octant ID']='Overall Count'   

         
#   inserting the  data
df.at[0,'1']=octant.count(1)
df.at[0,'-1']=octant.count(-1)
df.at[0,'2']=octant.count(2)
df.at[0,'-2']=octant.count(-2)
df.at[0,'3']=octant.count(3)
df.at[0,'-3']=octant.count(-3)
df.at[0,'4']=octant.count(4)
df.at[0,'-4']=octant.count(-4)





# This is the split the list into equal parts
def list_split(list1, n):
    for a in range(0, len(list1), n):
        every_chunk = list1[a: n+a]

        if len(every_chunk) < n:
            every_chunk = every_chunk + \
                [None for b in range(n-len(every_chunk))]
        yield every_chunk
        
mod=5000   
start=0
i=3
df.at[2,'Octant ID']="Mod "+str(mod)
try:
 lis=list(list_split(octant, mod))
except:
    print(" not found")


lis_size=len(lis)
        
for a in lis:     
    print("a")   
    if(i-2==lis_size):       
      df.at[i,'Octant ID']=str(start)+"-"+str(30000)
    else:
      df.at[i,'Octant ID']=str(start)+"-"+str(start+mod-1)
    df.at[i,'1']=a.count(1)
    df.at[i,'-1']=a.count(-1)
    df.at[i,'2']=a.count(2)
    df.at[i,'-2']=a.count(-2)
    df.at[i,'3']=a.count(3)
    df.at[i,'-3']=a.count(-3)
    df.at[i,'4']=a.count(4)
    df.at[i,'-4']=a.count(-4)
    i+=1
    start=start+mod


df.at[i,'Octant ID']='Verified' 
df.at[i,'1']=octant.count(1)
df.at[i,'-1']=octant.count(-1)
df.at[i,'2']=octant.count(2)
df.at[i,'-2']=octant.count(-2)
df.at[i,'3']=octant.count(3)
df.at[i,'-3']=octant.count(-3)
df.at[i,'4']=octant.count(4)
df.at[i,'-4']=octant.count(-4)


df2=pd.DataFrame(columns=['1','-1','2','-2','3','-3','4','-4'],index=['1','-1','2','-2','3','-3','4','-4'])
df2=df2.fillna(0)
print(df2)

# print(df2['1']['1'])
for j in range(0,n-1):
    ro=str(int(octant[j]))
    co=str(int(octant[j+1]))
    df2.loc[ro,co]+=1
i=i+3  
df.at[i,'Octant ID']="Overall Transition Count"
df.at[i+2,'Octant ID']="Count"
i=i+1
# df.at[i,'1']="To"
# df.at[i+2,' '] ='From'
i=i+1
df.at[i,'1']='1'
df.at[i,'-1']='-1'
df.at[i,'2']='2'
df.at[i,'-2']='-2'
df.at[i,'3']='3'
df.at[i,'-3']='-3'
df.at[i,'4']='4'
df.at[i,'-4']='-4'
df.at[i+1,'Octant ID']='1'
df.at[i+2,'Octant ID']='-1'
df.at[i+3,'Octant ID']='2'
df.at[i+4,'Octant ID']='-2'
df.at[i+5,'Octant ID']='3'
df.at[i+6,'Octant ID']='-3'
df.at[i+7,'Octant ID']='4'
df.at[i+8,'Octant ID']='-4'
i=i+1
col_index=13
for k in range(0,8):
    for l in range(0,8):
        df.iloc[i+k,col_index+l]=df2.iloc[k,l]


i=i+16
st=0
# lis2=np.array_split(octant, mod)     
lis2 = [octant[i * mod:(i + 1) * mod] for i in range((len(octant) + mod - 1) // mod )] 
for a in lis2:
    df2=pd.DataFrame(columns=['1','-1','2','-2','3','-3','4','-4'],index=['1','-1','2','-2','3','-3','4','-4'])
    df2=df2.fillna(0)
   
    print(len(a),end='  ')
    for j in range(0,len(a)-1):
        ro=str(int(a[j]))
        co=str(int(a[j+1]))
        df2.loc[ro,co]+=1
    i=i+3  
    df.at[i,'Octant ID']="Mod Transition Count"
    df.at[i+2,'Octant ID']="Count"
    df.at[i+1,'Octant ID']=str(st+1)+"-"+str(st+mod)
    st=st+mod
    
    i=i+1
   
    i=i+1
    df.at[i,'1']='1'
    df.at[i,'-1']='-1'
    df.at[i,'2']='2'
    df.at[i,'-2']='-2'
    df.at[i,'3']='3'
    df.at[i,'-3']='-3'
    df.at[i,'4']='4'
    df.at[i,'-4']='-4'
    df.at[i+1,'Octant ID']='1'
    df.at[i+2,'Octant ID']='-1'
    df.at[i+3,'Octant ID']='2'
    df.at[i+4,'Octant ID']='-2'
    df.at[i+5,'Octant ID']='3'
    df.at[i+6,'Octant ID']='-3'
    df.at[i+7,'Octant ID']='4'
    df.at[i+8,'Octant ID']='-4'
    i=i+1
    col_index=13
    for k in range(0,8):
        for l in range(0,8):
            df.iloc[i+k,col_index+l]=df2.iloc[k,l]
    # print(df2)
    # print(df2.iloc[1][0])

    i=i+16
        
df.to_excel(r'out_octant_transition_identify.xlsx',index=False)