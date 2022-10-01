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
