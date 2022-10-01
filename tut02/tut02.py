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
U_avg = df['U'].mean()

# Mean of V
V_avg = df['V'].mean()

# Mean of W
W_avg = df['W'].mean()
