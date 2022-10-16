import pandas as pd # importing pandas library
df = pd.read_excel(r"C:\Users\kavita Meena\OneDrive\Documents\GitHub\2001ME33_2022\tut04")
x = df.shape[0]
df.head()
 #finding average of x, y and z using mean function
x_avg = df['x'].mean()
y_avg = df['y'].mean()
z_avg = df['z'].mean()

#creating columns(name = x Avg, y Avg, z Avg) to store x_avg  ,y_avg and z_avg values
df['x Avg']=x_avg
df['y Avg']=y_avg
df['z Avg']=z_avg

#taking head(1) means x Avg , y Avg and z Avg will print only one time(at a place)
df['x Avg']=df['x Avg'].head(1)
df['y Avg']=df['y Avg'].head (1)
df['z Avg']=df['z Avg'].head(1)
df.head()
 #defining a,b,c where a=x' , b=y' , c=z'
a = df['x'] - x_avg
b = df['y'] - y_avg
c =df['z'] - z_avg

# creating colums named x', y' and z' to store the a,b and c values resp
df["x'=x - x_avg"] = a
df["y'=y - y_avg"] = b
df["z'=z - z_avg"] = c

df.to_excel('output_octant_longest_subsequence_with_range.xlsx')
df.head()
 #creating the column to store the octant value
df.insert(10, column="Octant", value="")

#using loop
for i in range(0,x):
    X= df["x'=x - x_avg"][i]
    Y= df["y'=y - y_avg"][i]
    Z= df["z'=z - z_avg"][i]
    
    
    if X>0 and Y>0 and Z>0:
        print(1)
        df["Octant"][i] = 1
    elif X>0 and Y>0 and Z<0:
        print(-1)
        df["Octant"][i] =-1
    elif X<0 and Y>0 and Z>0:
        print(2)
        df["Octant"][i] =2
    elif X<0 and Y>0 and Z<0:
        print(-2)
        df["Octant"][i] =-2
    elif X<0 and Y<0 and Z>0:
        print(3)
        df["Octant"][i] =3
    elif X<0 and Y<0 and Z<0:
        print(-3)
        df["Octant"][i] =-3
    elif X>0 and Y<0 and Z>0:
        print(4)
        df["Octant"][i] =4
    elif X>0 and Y<0 and Z<0:
        print(-4)
        df["Octant"][i] =-4
df.to_excel('output_octant_longest_subsequence_with_range.xlsx')
df.head()

df.insert(11, column="  ", value="")
#creating the column to store the count value as column name count_1
df.insert(12, column="Count_1", value="")
#creating the column to store the Longest Subsquence Length value
df.insert(13, column="Longest Subsquence Length", value="")
#creating the column to store the total count value as column name final_count
df.insert(14, column="final_count", value="")

 # storing the for count_1(count column name taken as count_1) column in a list
list=[1,-1, 2, -2, 3,-3, 4,-4]
y=len(list) #finding the list size
# printing the values in the count_1
for i in range (0,y):
    df.at[i,'Count_1'] = list[i]
df.head(10)

 # calculating the longest subsequence length value by defining a funtion name longest_sequence with the parameter n(list value)
def longest_sequence(n):
    lsc_p1_i=0
    lsc_p1=0
    for i in range(0,x):
        if(df["Octant"][i]==n):
            lsc_p1=lsc_p1+1
        if(df["Octant"][i]!=n or i==x-1):
            if(lsc_p1>lsc_p1_i):
                lsc_p1_i=lsc_p1
                lsc_p1=0
            else:
                lsc_p1_i=lsc_p1_i
                lsc_p1=0
    return lsc_p1_i

# creating a array(arr_longest_subs_length)to store the longest sequence length of the count_1 value
arr_longest_subs_length = [0] * y
# using a loop in which we are calling the longest_sequence function. with the help of this function we are printing the values directly in the output file
for i in range(0,y):
    arr_longest_subs_length[i]=longest_sequence(list[i])
    df.at[i,'Longest Subsquence Length'] = arr_longest_subs_length[i]

# calculating the count value by defining a funciton name final_count_no with two paramater m and n which is (longest sequence length value, count_1 value)
def final_count_no(m,n):
    cp1=0
    cp1i=0
    for i in range(0,x):
        if(df["Octant"][i]==n):
            cp1i=cp1i+1
        if(cp1i==m):
            cp1=cp1+1
            cp1i=0  
        if(df["Octant"][i]!=n):
            cp1i=0
    return cp1

# creating a array(name arr_longest_subs_length_count) to store the no. of sequence count value(final_count column) 
arr_longest_subs_length_count = [0] * y
# using a loop in which we are calling the final_count_no function. with the help of this function we are printing the values directly to the final_count column
for i in range(0,y):
    arr_longest_subs_length_count[i]=final_count_no(arr_longest_subs_length[i],list[i])
    df.at[i,'final_count'] = arr_longest_subs_length_count[i]

df.insert(15, column=" b ", value="")
#creating the column to store the count value as column name count_1
df.insert(16, column="Count_2", value="")
#creating the column to store the Longest Subsquence Length value
df.insert(17, column="Longest Subsquence Length1", value="")
#creating the column to store the total count value as column name final_count
df.insert(18, column="final_count1", value="")

# defining a function to print the count , longest sequence length , time ,to ,from 
def time(c,d):
        df.at[c,'Count_2'] = list[d]
        df.at[c,'Longest Subsquence Length1'] = arr_longest_subs_length[d]
        df.at[c,'final_count1'] = arr_longest_subs_length_count[d]
        df.at[c+1,'Count_2'] = 'Time'
        df.at[c+1,'Longest Subsquence Length1'] = 'From'
        df.at[c+1,'final_count1'] = 'To'
        
# defining a function name time_interval to get the time interval of the longest sequence value 
def time_interval(m,n):
    g=c+2
    cp1=0
    cp1i=0
    for i in range(0,x):
            if(df["Octant"][i]==n):
                cp1i=cp1i+1
            if(cp1i==m):
                df.at[g,'Longest Subsquence Length1'] = df["Time"][i-m+1]
                df.at[g,'final_count1'] = df["Time"][i]
                g=g+1
                cp1=cp1+1
                cp1i=0
            if(df["Octant"][i]!=n):
                cp1i=0
            
arr=[0]*y # array(arr) for calling the time function for this loop 
a=[0]*y   # array(arr) for calling the time_interval function for this loop
c=0
for i in range(0,y):
    arr[i]=time(c,i)
    a[i]=time_interval(arr_longest_subs_length[i],list[i])
    c=c+arr_longest_subs_length_count[i]+2

df.to_excel('output_octant_longest_subsequence_with_range.xlsx')
df.head(30)