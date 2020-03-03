import speech_recognition as sr
from os import system
import time
from Tkinter import *
import shutil
import getpass 
import datetime
import smtplib
from selenium import webdriver
from sys import platform
columns = shutil.get_terminal_size().columns

score = 0
right = 0
wrong = 0
left = 3
pa = 0
word = "memeibigbrain"
seconds = 10

quiz_one = ""
quiz_two = ""
quiz_three = ""
quiz_four = ""
quiz_five = ""
quiz_six = ""
quiz_seven = ""
quiz_eight = ""
quiz_nine = ""
quiz_ten = ""

quiz_oneA = ""
quiz_twoA = ""
quiz_threeA = ""
quiz_fourA = ""
quiz_fiveA = ""
quiz_sixA = ""
quiz_sevenA = ""
quiz_eightA = ""
quiz_nineA = ""
quiz_tenA = ""

r = sr.Recognizer()
with sr.Microphone() as source:               
    audio = r.listen(source)   
command = r.recognize_google(audio).lower()

def screen_clear():
   if platform == "linux":
      os.system('cls')
   # for mac and linux(here, os.name is 'posix')
   else:
      os.system('clear')

def lacolleResponse(audio):
  print(audio)
  for line in audio.splitlines():
      os,system(audio)

def SRW():
  lacolleResponse("You'r score is " + score + ". The amount of question answered right is "+ right + ". The amount of question answered wrong is "+ wrong + ". You have " "more question's left")

  def password():
    p = getpass.getpass(hidden ,prompt = word) 
  
    if p.lower() == word: 
        pa = 1 
    else: 
        print('The answer entered by you is incorrect')
        pa = 0

def countdown_timer(x):
    while x > 0:
        x -= 1
        print("{} remaining".format(str(datetime.timedelta(seconds=x))))
        print("\n")
        time.sleep(1)
    if x == 10 or x == 9:
        score + 5
    if x == 8 or x == 7:
        score + 4
    if x == 6 or x == 5:
        score + 3
    if x == 4 or x == 3:
        score + 2
    if x == 2 or x == 1:
        score + 1
password()

def quiz1():
  lacolleResponse(quiz_one)
  contdown_timer(x)
  if quiz_oneA in command:
    lacolleResponse("Correcet")
    screen_clear()
    right+1
    left-1
    SRW()
  else:
    lacolleResponse("Wong, the answer is " + quiz_oneA)
    screen_clear()
    wrong+1
    left-1
    SRW()

def quiz2():
  contdown_timer(x)
  lacolleResponse(quiz_two)
  time.sleep(5) 
  if quiz_twoA in command:
    lacolleResponse("Correcet")
    screen_clear()
    right+1
    left-1
    SRW()
  else:
    lacolleResponse("Wong, the answer is "+ quiz_twoA)
    screen_clear()
    wrong+1
    left-1
    SRW()

def quiz3():
  contdown_timer(x)
  lacolleResponse(quiz_three) 
  if quiz_threeA in command:
    lacolleResponse("Correcet")
    print("Tu a 5 seconde pour dire ton reponse".center(columns))
    screen_clear()
    right+1
    left-1
    SRW()
  else:
    lacolleResponse("Wong, the answer is "+ quiz_threeA)
    print("Tu a 5 seconde pour dire ton reponse".center(columns))
    screen_clear()
    wrong+1
    left-1
    SRW()
    
def quiz4():
  contdown_timer(x)
  lacolleResponse(quiz_four)
  time.sleep(5) 
  if quiz_fourA in command:
    lacolleResponse("Correcet")
    screen_clear()
    right+1
    left-1
    SRW()
  else:
    lacolleResponse("Wong, the answer is "+ quiz_fourA)
    screen_clear()
    wrong+1
    left-1
    SRW()

def quiz5():
  contdown_timer(x)
  lacolleResponse(quiz_five)
  time.sleep(5) 
  if quiz_fiveA in command:
    lacolleResponse("Correcet")
    screen_clear()
    right+1
    left-1
    SRW()
  else:
    lacolleResponse("Wong, the answer is "+ quiz_fiveA)
    screen_clear()
    wrong+1
    left-1
    SRW()
    
def quiz6():
  contdown_timer(x)
  lacolleResponse(quiz_six)
  time.sleep(5) 
  if quiz_sixA in command:
    lacolleResponse("Correcet")
    screen_clear()
    right+1
    left-1
    SRW()
  else:
    lacolleResponse("Wong, the answer is "+ quiz_sixA)
    screen_clear()
    wrong+1
    left-1
    SRW()

def quiz7():
  contdown_timer(x)
  lacolleResponse(quiz_seven)
  time.sleep(5) 
  if quiz_sevenA in command:
    lacolleResponse("Correcet")
    screen_clear()
    right+1
    left-1
    SRW()
  else:
    lacolleResponse("Wong, the answer is "+ quiz_sevenA)
    screen_clear()
    wrong+1
    left-1
    SRW()
    
def quiz8():
  contdown_timer(x)
  lacolleResponse(quiz_eight)
  time.sleep(5) 
  if quiz_eightA in command:
    lacolleResponse("Correcet")
    screen_clear()
    right+1
    left-1
    SRW()
  else:
    lacolleResponse("Wong, the answer is "+ quiz_eightA)
    screen_clear()
    wrong+1
    left-1
    SRW()
    
def quiz9():
  contdown_timer(x)
  lacolleResponse(quiz_nine)
  time.sleep(5) 
  if quiz_nineA in command:
    lacolleResponse("Correcet")
    screen_clear()
    right+1
    left-1
    SRW()
  else:
    lacolleResponse("Wong, the answer is "+ quiz_nineA)
    screen_clear()
    wrong+1
    left-1
    SRW()
    
def quiz10():
  contdown_timer(x)
  lacolleResponse(quiz_ten)
  time.sleep(5) 
  if quiz_tenA in command:
    lacolleResponse("Correcet")
    screen_clear()
    right+1
    left-1
    SRW()
  else:
    lacolleResponse("Wong, the answer is "+ quiz_tenA)
    screen_clear()
    wrong+1
    left-1
    SRW()
if pa == 1:
  b_one = Button(center, text= "Quiz", command = screen_clear() and quiz1())
else:
    password()

if left == 9 or x == 0:
  b_two = Button(center, text= "Question 2", command = screen_clear() and quiz2())

if left == 8 or x == 0:
  b_two = Button(center, text= "Question 3", command = screen_clear() and quiz3())
 
if left == 7 or x == 0:
  b_three = Button(center, text= "Question 4", command =  screen_clear() and quiz4())

if left == 6 or x == 0:
  b_three = Button(center, text= "Question 5", command = screen_clear() and quiz5())

if left == 5 or x == 0:
  b_three = Button(center, text= "Question 6", command =  screen_clear() and quiz6())

if left == 4 or x == 0:
  b_three = Button(center, text= "Question 7", command =  screen_clear() and quiz7())

if left == 3 or x == 0:
  b_three = Button(center, text= "Question 8", command =  screen_clear() and quiz8())

if left == 2 or x == 0:
  b_three = Button(center, text= "Question 9", command =  screen_clear() and quiz9())

if left == 1 or x == 0:
  b_three = Button(center, text= "Question 10", command = screen_clear() and quiz10())

if left == 0:
  SRW()
  sender = 'passynkovsteven@gmail.com'
  receivers = ['passynkovsteven@gmail.com']
  name = raw_input("Enter your full name or be disqualified: ".center(columns))
  screen_clear()

  message = SRW() and name
  driver.refresh()
  try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    time.sleep(10)
    driver.refresh()
  except SMTPException:
    print("Error: unable to send email".top(columns))
    lacolleResponse("Error: unable to send email")
    print("Get Steven to help and retrieve your score".center(columns))
    lacolleResponse("Get Steven to help and retrieve your score")
    print("I am going to lock get help".bottom(columns))
    lacolleResponse("I am going to lock get help")
    pa = 0
    
