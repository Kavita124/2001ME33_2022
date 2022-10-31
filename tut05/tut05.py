import pandas as pd
df = pd.read_excel(r"C:\Users\kavita Meena\OneDrive\Documents\GitHub\2001ME33_2022\tut05")
x = df.shape[0]
df.head(15)
#finding mean for average a,b and c value
a_avg = df['a'].mean()
b_avg = df['b'].mean()
c_avg = df['c'].mean()

#making columns to store average value of a,b,c
df['a Avg']=a_avg
#and here I have given only 1st place of line to a avg otherwise average value will print in whole column
df['a Avg']=df['a Avg'].head(1)

#similarly for b and c,doing the same thing
df['b Avg']=b_avg
df['b Avg']=df['b Avg'].head(1)

df['c Avg']=c_avg
df['c Avg']=df['c Avg'].head(1)

df.head()
X = df['a'] - a_avg
Y = df['b'] - b_avg
Z = df['c'] - c_avg

#made column for storing X and named the column as a'=a - a_avg,similarily Y for b'=b - b_avg and Z for c'=c - c_avg.
df["a'=a - a_avg"] = X
df["b'=b - b_avg"] = Y
df["c'=c - c_avg"] = Z
df.head()
df.insert(10, column="Octant", value="")

#using loop 
for i in range(0,x):
    M= df["a'=a - a_avg"][i]
    N= df["b'=b - b_avg"][i]
    O= df["c'=c - c_avg"][i]

#using loop
for i in range(0,x):
    M= df["a'=a - a_avg"][i]
    N= df["b'=b - b_avg"][i]
    O= df["c'=c - c_avg"][i]
    
    
    if M>0 and N>0 and O>0:
        print(1)
        df["Octant"][i] = 1
    elif M>0 and N>0 and O<0:
        print(-1)
        df["Octant"][i] =-1
    elif M<0 and N>0 and O>0:
        print(2)
        df["Octant"][i] =2
    elif M<0 and N>0 and O<0:
        print(-2)
        df["Octant"][i] =-2
    elif M<0 and N<0 and O>0:
        print(3)
        df["Octant"][i] =3
    elif M<0 and N<0 and O<0:
        print(-3)
        df["Octant"][i] =-3
    elif M>0 and N<0 and O>0:
        print(4)
        df["Octant"][i] =4
    elif M>0 and N<0 and O<0:
        print(-4)
        df["Octant"][i] =-4
df.at[1,''] = 'User Input'

df.at[0,'Octant ID'] = 'Overall Count'
df.at[1,''] = 'User Input'
mod_max_value=30000
n=mod_max_value//mod
q_list=[]
for k in range(0,n+2):
    if(k==0):
        df.at[k,'Octant ID'] = 'Overall Count'
    elif(k==1):
        df.at[k,'Octant ID'] ="mod"+ " " +str(mod)
    elif(k==2):
        df.at[k,'Octant ID'] = str((k-2)*mod) +"-"+str((k-1)*mod-1)
    else:
        df.at[k,'Octant ID'] = str((k-2)*mod+1) +"-"+str((k-1)*mod-1)
range_value = int(2 + (mod_max_value/mod))
q_list = [1,-1,2,-2,3,-3,4,-4]
for j in q_list:
    df.at[0,j] = list(df['Octant']).count(j)
    for i in range(0,n):
        if(i==0):
            df.at[i+2,j] = list(df['Octant'][i*mod:(i+1)*mod-1]).count(j) 
        else :
            df.at[i+2,j] = list(df['Octant'][i*mod-1:(i+1)*mod-1]).count(j) 
for j in range(0,range_value):
    octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}
    octant_count = []
    for i in q_list:
        octant_count.append(df.loc[j,i]) 
    octant_count.sort(reverse=True)

    for i in q_list:
        for x in range(0,8):
            if(octant_count[x]==df.loc[j,i]):
                df.loc[j,"Rank("+str(i)+")"] = x+1
    
    for k in q_list:
        if(df.loc[j,"Rank("+str(k)+")"]==1):
            df.loc[j,"Rank1 Octant ID"] = k
            df.loc[j,"Rank1 Octant Name"]=octant_name_id_mapping[str(k)]
df = pd.concat([df.columns.to_frame().T, df], ignore_index=True)
df.to_excel("octant_output_ranking_excel.xlsx",index=False,header=None)