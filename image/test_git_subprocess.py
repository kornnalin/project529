import subprocess
from pexpect import popen_spawn


user = 'kornnalin'
password = 'Ff012426484'

cmd = "cd /home/pi/Desktop/project529/image"
returned_value = subprocess.call(cmd, shell=True)

cmd = "ls" 
subprocess.call(cmd, shell=True)

cmd = 'git add "firn2.jpg"'
subprocess.call(cmd, shell=True)

cmd = 'git commit -m "img firn"'
subprocess.call(cmd, shell=True)

cmd = "git push -u origin master"
subprocess.call(cmd, shell=True)

#cmd = "kornnalin"
#subprocess.call(cmd, shell=True)
#
#cmd = "Ff012426484"
#subprocess.call(cmd, shell=True)

#child_process = popen_spawn.PopenSpawn(cmd)
#child_process.expect('User')
#child_process.sendline(user)
#child_process.expect('Password')
#child_process.sendline(password)
#print('returned value:', returned_value)

