import speech_recognition as sr
import os
import time
from Tkinter import *
import shutil
import getpass 
import datetime
import smtplib
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

quiz_oneA = ""
quiz_twoA = ""
quiz_threeA = ""

r = sr.Recognizer()
with sr.Microphone() as source:               
    audio = r.listen(source)   
command = r.recognize_google(audio).lower()

def lacolleResponse(audio):
  print(audio)
  for line in audio.splitlines():
      os.system(audio)

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

lacolleResponse("Tu a 10 seconde pour dire ton reponse")
print("Tu a 10 seconde pour dire ton reponse".center(columns))

def quiz1():
  lacolleResponse(quiz_one)
  contdown_timer(x)
  if quiz_oneA in command:
    lacolleResponse("Correcet")
    os.system('clear')
    right+1
    left-1
    SRW()
  else:
    lacolleResponse("Wong, the answer is " + quiz_oneA)
    os.system('clear')
    wrong+1
    left-1
    SRW()

def quiz2():
  contdown_timer(x)
  lacolleResponse(quiz_two)
  time.sleep(5) 
  if quiz_twoA in command:
    lacolleResponse("Correcet")
    os.system('clear')
    right+1
    left-1
    SRW()
  else:
    lacolleResponse("Wong, the answer is "+ quiz_twoA)
    os.system('clear')
    wrong+1
    left-1
    SRW()

def quiz3():
  contdown_timer(x)
  lacolleResponse(quiz_three) 
  if quiz_threeA in command:
    lacolleResponse("Correcet")
    print("Tu a 5 seconde pour dire ton reponse".center(columns))
    os.system('clear')
    right+1
    left-1
    SRW()
  else:
    lacolleResponse("Wong, the answer is "+ quiz_threeA)
    print("Tu a 5 seconde pour dire ton reponse".center(columns))
    os.system('clear')
    wrong+1
    left-1
    SRW()

if pa == 1:
  b_one = Button(center, text= "Quiz", command = os.system('clear') and quiz1())

if left == 2 or x == 0:
  b_two = Button(center, text= "Question 2", command = os.system('clear') and quiz2())

if left == 1 or x == 0:
  b_three = Button(center, text= "Question 3", command =  os.system('clear') and quiz3())

if left == 0:
  SRW()
  sender = 'passynkovsteven@gmail.com'
  receivers = ['passynkovsteven@gmail.com']

  message = SRW()

  try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)         
  except SMTPException:
    print "Error: unable to send email"
    lacolleResponse("Error: unable to send email")