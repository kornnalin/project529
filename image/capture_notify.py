#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from picamera import PiCamera
from time import sleep 
import datetime as dt
import base64
import requests
from github import Github
#import cv2
import subprocess
from pexpect import popen_spawn

status = False
dateTime = dt.datetime.now()
dates = str(dateTime)[0:10]
times = str(dateTime)[11:19]
filename = dates+'_'+times+'.jpg'
filepath = '/home/pi/Desktop/project529/image/'+filename
print(filepath)

g = Github("7474ef783e5527b8fef335629f37dfe506897abb")
repo = g.get_repo("kornnalin/project529")
#print(repo.name) #project529

def snap():
    print('start snap')
    camera = PiCamera()
    camera.rotation = 180
#    camera.resolution=(330,240)
    camera.resolution=(640,480)
    camera.start_preview()
    sleep(2)
    camera.capture(filepath)
    camera.stop_preview()
    status = True
    
    subprocess()
    line_notify_message(dates+' '+times)
    line_notify_picture("https://project529.herokuapp.com/"+filename)
 
def subprocess():
    user = 'kornnalin'
    password = 'Ff012426484'

    cmd = "cd /home/pi/Desktop/project529/image"
    returned_value = subprocess.call(cmd, shell=True)
    #cmd = "ls" 
    #subprocess.call(cmd, shell=True)
    cmd = 'git add '+filename
    subprocess.call(cmd, shell=True)
    cmd = 'git commit -m "img firn"'
    subprocess.call(cmd, shell=True)
    cmd = "git push -u origin master"
    subprocess.call(cmd, shell=True)
    #cmd = "kornnalin"
    #subprocess.call(cmd, shell=True)
    #cmd = "Ff012426484"
    #subprocess.call(cmd, shell=True)
#    child_process = popen_spawn.PopenSpawn(cmd)
#    child_process.expect('User')
#    child_process.sendline(user)
#    child_process.expect('Password')
#    child_process.sendline(password)
#    print('returned value:', returned_value)
    
def line_notify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'gptIH3kH8p4vTqohn1sded6uPOcRU907NQoZ13HFuPd'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)

def line_notify_message(message):
    payload = {'message':message}
    return line_notify(payload)

def line_notify_picture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return line_notify(payload)

def line_notify_sticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return line_notify(payload)
    
word = input()
print(word)

if(word == str("snap")):
    snap()
else:
    print("error")

try :
 while (status==False):
  pass
except KeyboardInterrupt :
 status = True
 
