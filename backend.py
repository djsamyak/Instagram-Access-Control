import pandas as pd
import random
import string
import smtplib

def GET_old_passcode():
    try:
        data = pd.read_csv('old_code.txt',header=None)
        return data[0][0]
    except:
        return data["password"][0]

def POST_new_passcode(password):
    f = open("old_code.txt", "w")
    f.seek(0) 
    f.write(password)
    f.close()

def APPEND_password(password):
    f = open("list.txt", "a")
    f.write(password)
    f.write("\n")
    f.close()


def generate_passcode(length):
    # Random string with the combination of lower and upper case
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    POST_new_passcode(result_str + "\n")
    APPEND_password(result_str + "\n")
    return result_str

def send_Mail(data):
    conn = smtplib.SMTP("smtp.gmail.com",587)

    userID = data["BOT_ID"][0]
    password = data["BOT_PASSWORD"][0]

    conn.ehlo()
    conn.starttls()
    conn.login(userID,password)

    message = f'''Subject: Updated Password for {data["username"][0]} \r\n
Dear User,
The updated password for {data["username"][0]} is {GET_old_passcode()}.'''
    print(message)

    conn.sendmail("NODATA",data["NOTIF_ID"],message)
    conn.quit()