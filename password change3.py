import paramiko
import re

def sshconnect():
 ssh = paramiko.SSHClient()
 ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 ssh.connect("192.168.1.22", username="root", password="nutanix/4u")
 return ssh

def sendread(commandline, prmt):
    X=1
    chan.send(commandline)
    resp=""""""
    buff=""""""
    buffprint=""""""

    while X == 1:
        resp1 = chan.recv(9999).decode()
        # ansi_escape = re.compile(r'\x1b[^m]*m')
        # resp1 = ansi_escape.sub('', resp)

        X = 2
        if resp1.find(prmt) == -1:

            X = 1
        buff += resp1
        buffprint=resp1
        if buffprint =="":
            pass
        else:

            print(buffprint,end="")
            buffprint=""
    return buff
ssh = sshconnect()
chan = ssh.invoke_shell()
txt = sendread("", "#")
txt = sendread("\n", "#")
txt = sendread("echo 1\n", "#")
# print(txt)
txt = sendread("echo 2\n", "#")
# print(txt)