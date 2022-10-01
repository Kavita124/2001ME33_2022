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

# Mean of U
U_mean = df['U'].mean()

# Mean of V
V_mean = df['V'].mean()

# Mean of W
W_mean = df['W'].mean()

# defining columns
df["U_mean"] = U_mean
# this line is there to print U_mean once, else it would have filled all the rows with the same value(U_mean)
df["U_mean"] = df["U_mean"].head(1)

df["V_mean"] = V_mean
df["V_mean"] = df["V_mean"].head(1)

df["W_mean"] = W_mean
df["W_mean"] = df["W_mean"].head(1)

#-----------------------------------------------------

U_minus_U_mean = (df['U'] - U_mean)
V_minus_V_mean = (df['V'] - V_mean)
W_minus_W_mean = (df['W'] - W_mean)

df["U' = U - U_mean"] = U_minus_U_mean
df["V' = V - V_mean"] = V_minus_V_mean
df["W' = W - W_mean"] = W_minus_W_mean

#-----------------------------------------------------

# defining an array that will store the octant values of the points
octant = []

for i in range(len(df)):

    # if U is +ve
    if df.loc[i, "U' = U - U_mean"]>0:
        #if V is +ve
        if df.loc[i, "V' = V - V_mean"]>0:
            # perform for W
            if df.loc[i, "W' = W - W_mean"]>0:
                octant.append(int(1))
            else:
                octant.append(int(-1))

        # if V is -ve
        else:
            if df.loc[i, "W' = W - W_mean"]>0:
                octant.append(int(4))
            else:
                octant.append(int(-4))

    #if U is -ve
    else:
        #if V is +ve
        if df.loc[i, "V' = V - V_mean"]>0:
            # now for W
            if df.loc[i, "W' = W - W_mean"]>0:
                octant.append(int(2))
            else:
                octant.append(int(-2))

        # if V is -ve
        else:
            if df.loc[i, "W' = W - W_mean"]>0:
                octant.append(int(3))
            else:
                octant.append(int(-3))

#now defining new column Octant and assign it values of octant array
df["Octant"] = octant

#--------------------------------------------------

# Printing and tabulating overall octant data
top_row = ["", "Octant ID", "1", "-1", "2", "-2", "3", "-3", "4", "-4"]
for i in range(len(top_row)):
    df.insert(i+11, top_row[i], value="")

df.iloc[0, 12] = "Overall count"

for i in range(8):
    df.iloc[0, i+13] = octant.count(int(top_row[2+i]))