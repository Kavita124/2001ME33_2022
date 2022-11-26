from datetime import datetime
start_time = datetime.now()

#Help
def scorecard():
	pass


###Code
with open("teams.txt") as f:
    content_list = f.readlines()

# print the list
print(content_list)

#---------------------
content_list = [x.strip() for x in content_list]
file1 = open("score.txt","w")
team_1=[]
team_1.append(content_list[0])
team_2=[]
team_2.append(content_list[2])
team1=team_1[0].split(',')  
li=team1[0].split(':')
li[1]=li[1][1:-3]
team1[0]=li[1]
li=team1[1].split(':')
team2=team_2[0].split(',')  
li=team2[0].split(':')
li[1]=li[1][1:-3]
team2[0]=li[1]
li=team1[2].split(':')


#team1[1]=team1[1][1:-3]
for i in range(0,len(team1)):
    if team1[i][-3:]=='(c)':
        team1[i]=team1[i][0:-3]
    elif team1[i][-3:]=='(w)':
        team1[i]=team1[i][0:-3]     
    team1[i]=team1[i][0:]
for i in range(0,len(team2)):
    if team2[i][-3:]=='(c)':
        team2[i]=team2[i][0:-3]
    elif team2[i][-3:]=='(w)':
        team2[i]=team2[i][0:-3]     
    team2[i]=team2[i][0:]
dic_runs={}
for i in range(11):
    dic_runs[team1[i]]=0
dic_balls={}
for i in range(11):
    dic_balls[team1[i]]=0
dic_4s={}
for i in range(11):
    dic_4s[team1[i]]=0
dic_6s={}
for i in range(11):
    dic_6s[team1[i]]=0
dic_SR={}
for i in range(11):
    dic_SR[team1[i]]=0
dic_out={}
for i in range(11):
    dic_runs[team1[i]]=""
for i in range(11):
    dic_runs[team2[i]]=0
for i in range(11):
    dic_balls[team2[i]]=0
for i in range(11):
    dic_4s[team2[i]]=0
for i in range(11):
    dic_6s[team2[i]]=0
for i in range(11):
    dic_SR[team2[i]]=0
for i in range(11):
    dic_runs[team2[i]]=""
# Displaying result
dic_run={}
curr_sum=0
dic_ball={}
dic_over={}
dic_bowl_run={}
dic_wide={}
dic_nb={}
dic_wickets={}
dic_out={}
wickets_1=0
wickets_2=0
fall_wickets_team1=""
fall_wickets_team2=""
curr_balls=0
with open("pak_inns1.txt") as f:
    pak_list = f.readlines()

# ---------------------------------

# remove new line characters
pak_list = [x.strip() for x in pak_list]
curr_runs=0

for i in range(len(pak_list)):
    if pak_list[i]=="":
        continue;
    li=pak_list[i].split(',')
    li1=li[0].split('to')
    li1[1]=li1[1][1:]
    bats=li1[1]
    bowler=li1[0][0:-1].split(' ')[1]
    str=li[1];
    if ".1" in li1[0]:
        if dic_over.get(bowler)==None:
            dic_over[bowler]=1
        else:
            dic_over[bowler]+=1
    if  'out'  in str:
        wickets_1+=1
        if dic_run.get(bats)==None:
            dic_run[bats]=0
        else:
            dic_run[bats]+=0
        if dic_wickets.get(bowler)==None:
            dic_wickets[bowler]=1
        else:
            dic_wickets[bowler]+=1
        curr_runs+=0
        rem=curr_balls%6
        q=int(curr_balls/6)
        st=f"{q}.{rem}"
        fall_wickets_team1+=f"{curr_runs} - {wickets_1} ({bats},{st})  "
        if "lbw" in str:
            dic_out[bats]=f"lbw {bowler}"
        elif "Caught" in str:
            s=str.split("by")[0].split(" ")
            dic_out[bats]=f"c {s}b {bowler}"
        elif "bowled" in str:
            dic_out[bats]=f"b {bowler}"
    elif  '1'  in str:
        if dic_run.get(bats)==None:
            dic_run[bats]=1
        else:
            dic_run[bats]+=1
        if dic_bowl_run.get(bowler)==None:
            dic_bowl_run[bowler]=1
        else:
            dic_bowl_run[bowler]+=1
        curr_runs+=1
    elif "2" in str:
        if dic_run.get(bats)==None:
            dic_run[bats]=2
        else:
            dic_run[bats]+=2
        if dic_bowl_run.get(bowler)==None:
            dic_bowl_run[bowler]=2
        else:
            dic_bowl_run[bowler]+=2
        curr_runs+=2
    elif "3" in str:
        if dic_run.get(bats)==None:
            dic_run[bats]=3
        else:
            dic_run[bats]+=3
        if dic_bowl_run.get(bowler)==None:
            dic_bowl_run[bowler]=3
        else:
            dic_bowl_run[bowler]+=3
        curr_runs+=3
    elif "FOUR" in str:
        if dic_run.get(bats)==None:
            dic_run[bats]=4
        else:
            dic_run[bats]+=4
        if dic_4s.get(bats)==None:
            dic_4s[bats]=1
        else:
            dic_4s[bats]+=1
        if dic_bowl_run.get(bowler)==None:
            dic_bowl_run[bowler]=4
        else:
            dic_bowl_run[bowler]+=4
        curr_runs+=4
    elif "SIX" in str:
        if dic_run.get(bats)==None:
            dic_ball[bats]=6
        else:
            dic_run[bats]+=6
        if dic_6s.get(bats)==None:
            dic_6s[bats]=1
        else:
            dic_6s[bats]+=1
        if dic_bowl_run.get(bowler)==None:
            dic_bowl_run[bowler]=6
        else:
            dic_bowl_run[bowler]+=6
        curr_sum+=6
    elif "wide" in str:
        curr_sum+=1
        if dic_bowl_run.get(bowler)==None:
            dic_bowl_run[bowler]=1
        else:
            dic_bowl_run[bowler]+=1
    elif "no ball" in str:
        curr_sum+=1
        if dic_bowl_run.get(bowler)==None:
            dic_bowl_run[bowler]=1
        else:
            dic_bowl_run[bowler]+=1
        if dic_nb(bowler)==None:
            dic_nb[bowler]=1
        else:
            dic_nb[bowler]+=1
    if "wide" not in str and "no ball" not in str:
        if dic_ball.get(bats)==None:
            dic_ball[bats]=1
        else:
            dic_ball[bats]+=1
    curr_balls+=1
dic1_run={}
curr_sum1=0
dic1_ball={}
dic1_over={}
dic1_bowl_run={}
dic1_wide={}
dic1_nb={}
dic1_wickets={}
dic1_4s={}
dic1_6s={}
wickets_2=0
curr_balls_2=0
with open("india_inns2.txt") as f:
    ind_list = f.readlines()

ind_list = [x.strip() for x in ind_list]
curr_runs1=0

for i in range(len(ind_list)):
    if ind_list[i]=="":
        continue;
    li=ind_list[i].split(',')
    li1=li[0].split('to')
    li1[1]=li1[1][1:]
    bats=li1[1]
    bowler=li1[0][0:-1].split(' ')[1]
    str=li[1];
    if ".5" in li1[0]:
        if dic1_over.get(bowler)==None:
            dic1_over[bowler]=1
        else:
            dic1_over[bowler]+=1
    if  'out'  in str:
        if dic1_run.get(bats)==None:
            dic1_run[bats]=0
        else:
            dic1_run[bats]+=0
        if dic1_wickets.get(bowler)==None:
            dic1_wickets[bowler]=1
        else:
            dic1_wickets[bowler]+=1
        curr_runs1+=0
        wickets_2+=1
        rem=curr_balls_2%6
        q=int(curr_balls_2/6)
        st=f"{q}.{rem}"
        fall_wickets_team2+=f"{curr_runs1} - {wickets_2} ({bats},{st})  "
    elif  '1'  in str:
        if dic1_run.get(bats)==None:
            dic1_run[bats]=1
        else:
            dic1_run[bats]+=1
        if dic1_bowl_run.get(bowler)==None:
            dic1_bowl_run[bowler]=1
        else:
            dic1_bowl_run[bowler]+=1
        curr_runs1+=1
    elif "2" in str:
        if dic1_run.get(bats)==None:
            dic1_run[bats]=2
        else:
            dic1_run[bats]+=2
        if dic1_bowl_run.get(bowler)==None:
            dic1_bowl_run[bowler]=2
        else:
            dic1_bowl_run[bowler]+=2
        curr_runs1+=2
    elif "3" in str:
        if dic1_run.get(bats)==None:
            dic1_run[bats]=3
        else:
            dic1_run[bats]+=3
        if dic1_bowl_run.get(bowler)==None:
            dic1_bowl_run[bowler]=3
        else:
            dic1_bowl_run[bowler]+=3
        curr_runs1+=3
    elif "FOUR" in str:
        if dic1_run.get(bats)==None:
            dic1_run[bats]=4
        else:
            dic1_run[bats]+=4
        if dic1_4s.get(bats)==None:
            dic1_4s[bats]=1
        else:
            dic1_4s[bats]+=1
        if dic1_bowl_run.get(bowler)==None:
            dic1_bowl_run[bowler]=4
        else:
            dic1_bowl_run[bowler]+=4
        curr_runs1+=4
    elif "SIX" in str:
        if dic1_run.get(bats)==None:
            dic1_run[bats]=1
        else:
            dic1_run[bats]+=6
        if dic1_6s.get(bats)==None:
            dic1_6s[bats]=1
        else:
            dic1_6s[bats]+=1
        if dic1_bowl_run.get(bowler)==None:
            dic1_bowl_run[bowler]=6
        else:
            dic1_bowl_run[bowler]+=6
        curr_runs1+=6
    elif "wide" in str:
        curr_runs1+=1
        if dic1_bowl_run.get(bowler)==None:
            dic1_bowl_run[bowler]=1
        else:
            dic1_bowl_run[bowler]+=1
        if dic1_wide.get(bowler)==None:
            dic1_wide[bowler]=1
        else:
            dic1_wide[bowler]+=1
    elif "no ball" in str:
        curr_runs1+=1
        if dic1_bowl_run.get(bowler)==None:
            dic1_bowl_run[bowler]=1
        else:
            dic1_bowl_run[bowler]+=1
        if dic1_nb(bowler)==None:
            dic1_nb[bowler]=1
        else:
            dic1_nb[bowler]+=1
    if "wide" not in str and "no ball" not in str:
        if dic1_ball.get(bats)==None:
            dic1_ball[bats]=1
        else:
            dic1_ball[bats]+=1
    curr_balls_2+=1
batter_team1= list(dic_run.keys())
batter_team2=list(dic1_run.keys())
bowler_team1= list(dic_over.keys())
bowler_team2=list(dic1_over.keys())
over_team1=list(dic_over.keys())
bowl_run_team1=list(dic_bowl_run.keys())
eco_bowl_team1=[]
powerplay_run1=43
powerplay_run2=38

for i in range(len(bowler_team1)):
    eco_bowl_team1.append(dic_bowl_run[bowl_run_team1[i]]/dic_over[over_team1[i]])
eco_bowl_team2=[]
for i in range(len(bowler_team2)):
    eco_bowl_team2.append(dic1_bowl_run[bowler_team2[i]]/dic1_over[bowler_team2[i]])
fours_team1=list()
runs_team1=[]
runs_team2=[]
balls_team1=[]
balls_team2=[]
fs_team1=[]
ss_teams1=[]
fs_team2=[]
ss_team2=[]
for i in range(len(bowler_team1)):
    if dic_nb.get(bowler_team1[i])==None:
            dic_nb[bowler_team1[i]]=0
for i in range(len(bowler_team2)):
    if dic1_nb.get(bowler_team2[i])==None:
            dic_nb[bowler_team2[i]]=0
for i in range(len(batter_team1)):
    if dic_4s.get(batter_team1[i])==None:
            dic_4s[batter_team1[i]]=0
for i in range(len(batter_team2)):
    if dic1_4s.get(batter_team2[i])==None:
            dic1_4s[batter_team2[i]]=0
for i in range(len(batter_team1)):
    if dic_6s.get(batter_team1[i])==None:
            dic_6s[batter_team1[i]]=0
for i in range(len(batter_team2)):
    if dic1_6s.get(batter_team2[i])==None:
            dic1_6s[batter_team2[i]]=0
for i in range(len(bowler_team1)):
    if dic_wickets.get(bowler_team1[i])==None:
            dic_wickets[bowler_team1[i]]=0
for i in range(len(bowler_team2)):
    if dic1_wickets.get(bowler_team2[i])==None:
            dic1_wickets[bowler_team2[i]]=0
for i in range(len(bowler_team1)):
    if dic_wide.get(bowler_team1[i])==None:
            dic_wide[bowler_team1[i]]=0
for i in range(len(bowler_team2)):
    if dic1_wide.get(bowler_team2[i])==None:
            dic1_wide[bowler_team2[i]]=0
for i in range(len(bowler_team2)):
    if dic1_nb.get(bowler_team2[i])==None:
            dic1_nb[bowler_team2[i]]=0
for i in range(len(bowler_team2)):
    if dic1_wide.get(bowler_team2[i])==None:
            dic1_wide[bowler_team2[i]]=0
for i in range(len(batter_team1)):
    runs_team1.append(dic_run[batter_team1[i]])
for i in range(len(batter_team2)):
    runs_team2.append(dic1_run[batter_team2[i]])
'''
for i in range(len(bowler_team1)):
    balls_team1.append(dic_ball[bowler_team1[i]])
for i in range(len(bowler_team2)):
    balls_team2.append(dic1_ball[bowler_team2[i]])

for i in range(len(batter_team1)):
    fs_team1.append(dic_4s[batter_team1[i]])
for i in range(len(batter_team2)):
    ss_team1.append(dic_6s_balls[batter_team1[i]])
for i in range(len(batter_team1)):
    fs_team2.append(dic1_4s[batter_team2[i]])
for i in range(len(batter_team2)):
    ss_team2.append(dic1_6sballs[batter_team2[i]])
'''
eco_team1=[]
powerplay_run=43
for i in range(len(batter_team1)):
    runs=dic_run[batter_team1[i]]
    balls=dic_ball[batter_team1[i]]
    ans=(dic_run[batter_team1[i]]/dic_ball[batter_team1[i]])*100
    answer =round(ans, 3)
    eco_team1.append(answer)
SR_team2=[]
for i in range(len(batter_team2)):
    runs=dic1_run[batter_team2[i]]
    balls=dic1_ball[batter_team2[i]]
    ans=(dic1_run[batter_team2[i]]/dic1_ball[batter_team2[i]])*100
    answer = round(ans, 3)
    SR_team2.append(answer)
file1 = open(r"C:\Users\kavita Meena\OneDrive\Documents\GitHub\2001ME33_2022\tut08","w+")
L=[]
L=["Batters                R     B    4s  6s    SR\n"]
file1.writelines(L)
space=6
for i in range(len(batter_team1)):
    L=[]
    L.append(f"{batter_team1[i]} ")
    s=space-len(batter_team1[i])
    for p in range (s):
        L.append(" ")
    if dic_run.get(batter_team1[i])!=None:
        L.append(f"  {dic_run[batter_team1[i]]} ")
    if dic_ball.get(batter_team1[i])!=None:
        L.append(f"  {dic_ball[batter_team1[i]]} ")
    if dic_4s.get(batter_team1[i])!=None:
        L.append(f"  {dic_4s[batter_team1[i]]} ")
    if dic_6s.get(batter_team1[i])!=None:
        L.append(f"  {dic_6s[batter_team1[i]]} ")
    L.append(f" {eco_team1[i]} ")
    L.append("\n")
    file1.writelines(L)
    
L.append(f"ftotal    {curr_runs}-{wickets_1}\n")
L.append("Fall of wickets\n")
L.append(fall_wickets_team1)
L.append("\n")
L.append("bowlers       O    R    W    NB    Wide   Eco\n")
file1.writelines(L)
space=13

for i in range(len(bowler_team1)):
    L=[]
    L.append(f"{bowler_team1[i]}  ")
    s=space-len(bowler_team1[i])
    for p in range (s):
        L.append(" ")
    if dic_over.get(bowler_team1[i])!=None:
        L.append(f"{dic_over[bowler_team1[i]]}  ")
    #s=space-len(dic_over[bowler_team1[i]])
    if dic_bowl_run.get(bowler_team1[i])!=None:
        L.append(f"{dic_bowl_run[bowler_team1[i]]} ")
    if dic_wickets.get(bowler_team1[i])!=None:
        L.append(f"   {dic_wickets[bowler_team1[i]]} ")
    if dic_nb.get(bowler_team1[i])!=None:
        L.append(f"   {dic_nb[bowler_team1[i]]}  ")
    if dic_wide.get(bowler_team1[i])!=None:
        L.append(f"   {dic_wide[bowler_team1[i]]}     ")
    L.append(f"    {eco_bowl_team1[i]} ")
    L.append("\n")
    file1.writelines(L)
L.append("powerplays    overs    runs\n")
L.append(f"Mandatory     0.1-6    {powerplay_run1}")
file1.writelines(L)    
L.append("India Innings\n")
L=["\nBatters            R     B     4s     6s       SR\n"]
file1.writelines(L)
for i in range(len(batter_team2)):
    L=[]
    L.append(f"{batter_team2[i]} ")
    s=space-len(batter_team2[i])
    for p in range (s):
        L.append(" ")
    if dic1_run.get(batter_team2[i])!=None:
        L.append(f"    {dic1_run[batter_team2[i]]} ")
    if dic1_ball.get(batter_team2[i])!=None:
        L.append(f"    {dic1_ball[batter_team2[i]]} ")
    if dic1_4s.get(batter_team2[i])!=None:
        L.append(f"   {dic1_4s[batter_team2[i]]} ")
    if dic1_6s.get(batter_team2[i])!=None:
        L.append(f"    {dic1_6s[batter_team2[i]]} ")
    L.append(f"      {eco_team1[i]} ")
    L.append("\n")
    file1.writelines(L)
    
L.append(f"ftotal    {curr_runs1}-{wickets_2}\n")
L.append("Fall of wickets\n")
L.append(fall_wickets_team2)
L.append("\n")
L.append("bowlers       O    R    W    NB    Wide   Eco\n")
file1.writelines(L)
space=20

for i in range(len(bowler_team2)):
    L=[]
    L.append(f"{bowler_team2[i]}  ")
    s=space-len(bowler_team2[i])
    for p in range (s):
        L.append(" ")
    if dic1_over.get(bowler_team2[i])!=None:
        L.append(f"{dic1_over[bowler_team2[i]]}  ")
    #s=space-len(dic_over[bowler_team1[i]])
    if dic1_bowl_run.get(bowler_team2[i])!=None:
        L.append(f"{dic1_bowl_run[bowler_team2[i]]} ")
    if dic1_wickets.get(bowler_team2[i])!=None:
        L.append(f"   {dic1_wickets[bowler_team2[i]]} ")
    if dic1_nb.get(bowler_team2[i])!=None:
        L.append(f"   {dic1_nb[bowler_team2[i]]}  ")
    if dic1_wide.get(bowler_team2[i])!=None:
        L.append(f"   {dic1_wide[bowler_team2[i]]}     ")
    L.append(f" {eco_bowl_team2[i]} ")
    L.append("\n")
    file1.writelines(L)
L.append("powerplays    overs    runs\n")
L.append(f"Mandatory     0.1-6    {powerplay_run2}")
file1.writelines(L)  


from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


scorecard()






#---------------------
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))