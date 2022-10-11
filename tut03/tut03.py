import pandas as pd

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")
mod=5000

df = pd.read_csv("octant_input.csv")

#-----------------------------------------------------
# Average of a
a_avg = df['a'].mean()

# Average of b
b_avg = df['b'].mean()

# Average of c
c_avg = df['c'].mean()

#-----------------------------------------------------

# defining columns
df["a_avg"] = a_avg
# this extra line is there to print U_avg once, else it would have filled all the rows with the same value(U_avg)
df["a_avg"] = df["a_avg"].head(1)

df["b_avg"] = b_avg
df["b_avg"] = df["b_avg"].head(1)

df["c_avg"] = c_avg
df["c_avg"] = df["c_avg"].head(1)

#-----------------------------------------------------

a_minus_a_avg = (df['a'] - a_avg)
b_minus_b_avg = (df['b'] - a_avg)
c_minus_c_avg = (df['c'] - c_avg)

df["a' = a - a_avg"] = a_minus_a_avg
df["b' = b - b_avg"] = b_minus_b_avg
df["c' = c - c_avg"] = c_minus_c_avg

#-----------------------------------------------------

# defining an array that will store the octant values of the points
octant = []

for i in range(len(df)):

    # if a is +ve
    if df.loc[i, "a' = a - a_avg"]>0:
        #if b is +ve
        if df.loc[i, "b' = b - b_avg"]>0:
            # perform for c
            if df.loc[i, "c' = c - c_avg"]>0:
                octant.append(int(1))
            else:
                octant.append(int(-1))

        # if b is -ve
        else:
            if df.loc[i, "c' = c - c_avg"]>0:
                octant.append(int(4))
            else:
                octant.append(int(-4))

    #if a is -ve
    else:
        #if b is +ve
        if df.loc[i, "b' = b - b_avg"]>0:
            # perform for c
            if df.loc[i, "c' = c - c_avg"]>0:
                octant.append(int(2))
            else:
                octant.append(int(-2))

        # if b is -ve
        else:
            if df.loc[i, "c' = c - c_avg"]>0:
                octant.append(int(3))
            else:
              
                octant.append(int(-3))


# defining new column Octant and assigning it values of octant array
df["Octant"] = octant

#--------------------------------------------------

# Printing and tabulating overall octant data
top_row = ["", "Octant ID", "1", "-1", "2", "-2", "3", "-3", "4", "-4"]
for i in range(len(top_row)):
    df.insert(i+11, top_row[i], value="")

df.iloc[0, 12] = "Overall count"

for i in range(8):
    df.iloc[0, i+13] = octant.count(int(top_row[2+i]))

#--------------------------------------------------

df.iloc[1, 11] = "User input"
df.iloc[1, 12] = "Mod " + str(mod)

i=0
k=3
df.iloc[2,12] = f"{i}-{i+mod-1}"
i+=mod

while i<len(df):
    # printing ranges
    df.iloc[k, 12] = f"{i}-{min(i+mod-1, len(df))}"
    # move to next row k+=1
    k+=1
    i+=mod


# defining chunk size to split the octant array
chunk_size = mod
chunked_list = []

# chunked_list is and array of arrays, whose length is chunk_size(mod)
for i in range(0, len(octant), chunk_size):
    chunked_list.append(octant[i:i+chunk_size])

# printing the counts at their positions
for m in range(len(chunked_list)):
    for j in range(8):
        df.iloc[m+2, j+13] = chunked_list[m].count(int(top_row[2+j]))

# finally writing output to file
df.to_csv('octant_output.csv', index=False)
