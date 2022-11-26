from datetime import datetime
start_time = datetime.now()

import pandas as pd
import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

######------------------------------------------------------------------

try:
    os.mkdir('output')
except FileExistsError:
    print("output folder exists, skipping folder creation\n")

#----###--------------------------------------------------------------

attendance_df = pd.read_csv('input_attendance.csv')
reg_students = pd.read_csv('input_registered_students.csv')

#------------------------------------------------------------------

# class was not taken but these dates are Mon/Thur
no_class = ['15-08-2022', '19-09-2022', '22-09-2022']

# Using the specific dates on which attendance was recorded, distinguish Mondays and Thursdays.
def lecture_dates():

    legit_lecture_dates = []

    # ------------------------------------------------------------------------
    dates = [str(timestamp).split(' ')[0] for timestamp in attendance_df["Timestamp"]]

    dates = [date for date in dates if date not in no_class] # we are only concerned with dates that are not holidays

    # convert to set to obtain distinct components
    dates = sorted((set(dates)), key=lambda date: datetime.strptime(date, "%d-%m-%Y"))

    for date in dates:

        # With the datetime module's "datetime" function, find the day at the given time.
        # split date w.r.t. '-' character and input in datetime function as required
        day = datetime(int(date.split('-')[2]), int(date.split('-')[1]), int(date.split('-')[0])).strftime('%a')
        if day in ["Mon", "Thu"]:
            legit_lecture_dates.append(date)

    return legit_lecture_dates

legit_lecture_dates = lecture_dates()

all_mon_thurs = sorted(legit_lecture_dates + no_class, key=lambda date: datetime.strptime(date, "%d-%m-%Y"))

total_lecture_taken = len(legit_lecture_dates)

#------------------------------------------------------------------

attendance_report_consolidated_df = pd.DataFrame()

#----------------------------------------------------------------

def attendance_report(roll_no, name):

    #To prevent Python from "creating" this dataframe in this method with local scope, you must define this dataframe as global.
    global attendance_report_consolidated_df

    roll_df = pd.DataFrame()

    roll_df.insert(0, "Date", value="")
    roll_df.insert(1, "Roll", value=[roll_no])
    roll_df.insert(2, "Name", value=[name])
    roll_df.insert(3, "Total Attendance Count", value="")
    roll_df.insert(4, "Real", value="")
    roll_df.insert(5, "Duplicate", value="")
    roll_df.insert(6, "Invalid", value="")
    roll_df.insert(7, "Absent", value="")
    
    # a dictionary that stores the dates and corresponding number of attendances marked on that date
    attendance_dates = {date: {'R': 0, 'D': 0, 'I': 0} for date in all_mon_thurs}

    # search for entries of roll_no in the attendance dataframe
    for person, timestamp in zip(attendance_df["Attendance"], attendance_df["Timestamp"]):

        # if match is found
        if person.split(' ')[0] == roll_no:

            curr_date = timestamp.split(' ')[0]
            curr_time = timestamp.split(' ')[1]
            
            if curr_date in legit_lecture_dates: # if attendance is marked on a lecture date
                
                if curr_time.split(':')[0] == '14' or curr_time == "15:00": # if time is 14:(something) or 15:00

                    if attendance_dates[curr_date]['R'] == 1: # if Real attendance has already been marked
                        attendance_dates[curr_date]['D']+=1 # increase duplicate by 1

                    else:
                        attendance_dates[curr_date]['R']+=1 # else record real attendance

                else:
                    attendance_dates[curr_date]['I']+=1 # if attendance is marked outside lecture hrs (but on a lecture day), increment invalid mark
                    
            elif curr_date in no_class: # if attendance is marked on a day which was holiday (class wasn't taken) {no_class are mon/thurs holidays}
                attendance_dates[curr_date]['I']+=1

            # no else statement because we ignore any attendance that was marked on a non-lecture day

    for index,date in enumerate(all_mon_thurs, start=1):

        # start printing dates from 1st row, 0th row contains roll_no and name, hence, start=1 is used
        roll_df.at[index, "Date"] = date
        roll_df.at[index, "Total Attendance Count"] = attendance_dates[date]['R'] + attendance_dates[date]['D'] + attendance_dates[date]['I']
        roll_df.at[index, "Real"] = attendance_dates[date]['R']
        roll_df.at[index, "Duplicate"] = attendance_dates[date]['D']
        roll_df.at[index, "Invalid"] = attendance_dates[date]['I']
        
        # case 1: total attendance count > 0 and real attendance = 1 -> student was present in class
        # case 2: total attendance count > 0 but real attendance = 0 -> duplicates = 0 -> invalids exist -> absent
        # case 3: total attendance count = 0 -> no real, duplicates, invalids -> absent
        if roll_df.at[index, "Total Attendance Count"]>0 and roll_df.at[index, "Real"]==1:
            roll_df.at[index, "Absent"] = 0
        else:
            roll_df.at[index, "Absent"] = 1

    # write evaluated data to roll_no's csv
    roll_df.to_excel(f'output/{roll_no}.xlsx', index=False)

    temp_df = pd.DataFrame(columns=["Roll", "Name"] + all_mon_thurs+ ["Actual Lecture Taken", "Total Real", "% Attendance"])
    temp_df["Roll"] = [roll_no]
    temp_df["Name"] = [name]

    total_real = 0
    for date in attendance_dates:
        if attendance_dates[date]['R'] == 1:
            temp_df[date] = 'P'
            total_real+=1
        else:
            temp_df[date] = 'A'

    temp_df["Actual Lecture Taken"] = total_lecture_taken
    temp_df["Total Real"] = total_real
    temp_df["% Attendance"] = round(total_real/total_lecture_taken*100, 2)

    attendance_report_consolidated_df = pd.concat([attendance_report_consolidated_df, temp_df])

#---------------------------------------------------------------

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

#---------------------------------------------------------------

# iterate through list of registered students
for roll_no, name in zip(reg_students["Roll No"], reg_students["Name"]):
    attendance_report(roll_no, name)

attendance_report_consolidated_df.to_excel(f'output/attendance_report_consolidated.xlsx', index=False)

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))

#---------------------------------------------------------------

def send_mail(fromaddr, frompasswd, toaddr, msg_subject, msg_body, file_path):
    try:
        msg = MIMEMultipart()
        print("[+] Message Object Created")
    except:
        print("[-] Error in Creating Message Object")
        return

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = msg_subject

    body = msg_body

    msg.attach(MIMEText(body, 'plain'))

    filename = file_path
    attachment = open(filename, "rb")

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    try:
        msg.attach(p)
        print("[+] File Attached")
    except:
        print("[-] Error in Attaching file")
        return

    try:
        #s = smtplib.SMTP('smtp.gmail.com', 587)
        s = smtplib.SMTP('mail.iitp.ac.in', 587)
        print("[+] SMTP Session Created")
    except:
        print("[-] Error in creating SMTP session")
        return  

    s.starttls()

    try:
        s.login(fromaddr, frompasswd)
        print("[+] Login Successful")
    except:
        print("[-] Login Failed")

    text = msg.as_string()

    try:
        s.sendmail(fromaddr, toaddr, text)
        print("[+] Mail Sent successfully")
    except:
        print('[-] Mail not sent')

    s.quit()


def isEmail(x):
    if ('@' in x) and ('.' in x):
        return True
    else:
        return False

FROM_ADDR = ""
FROM_PASSWD = ""
TO_ADDR = ""

Subject = "Attendance Report Consolidated"
Body ='''
PFA
'''

file_path = 'output/attendance_report_consolidated.xlsx'

if not FROM_ADDR or not FROM_PASSWD or not TO_ADDR:
    print("Enter FROM_ADDR, FROM_PASSWD and TO_ADDR values to use mail utility.")

elif not isEmail(FROM_ADDR) or not isEmail(TO_ADDR):
    print("Invalid Email")

else:
    send_mail(FROM_ADDR, FROM_PASSWD, TO_ADDR, Subject, Body, file_path)