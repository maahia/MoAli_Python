# import tkinter library
from tkinter import *
# for colors
from tkinter import ttk
# for combo box
from tkinter.ttk import *
# for button shape
import tkinter
import paramiko

# create main window
window = Tk()
window.title('CHANGING CLUSTER ACROPOLIS HOST PASSWORD ')
window.geometry("1024x512+20+20")

########################## Building GUI MAIN WINDOW######################################################
# Empty Line 1
L1 = Label(window, text="", font=("Arial Bold", 12))
L1.grid(row=0, column=0)
# Empty Line 2
L2 = Label(window, text="", font=("Arial Bold", 12))
L2.grid(row=1, column=0)
# Empty Line 3
L3 = Label(window, text="", font=("Arial Bold", 12))
L3.grid(row=2, column=0)
# Empty Line 4
L4 = Label(window, text="", font=("Arial Bold", 12))
L4.grid(row=3, column=0)

# UserName Line 5
L10 = Label(window, text="User Name", font=("Arial Bold", 14))
L10.grid(row=5, column=0)

user = StringVar()
txt10 = Entry(window, width=100, textvariable=user)
txt10.grid(row=5, column=1)

# password Line 6
L11 = Label(window, text="Password", font=("Arial Bold", 14))
L11.grid(row=6, column=0)

passwrd = StringVar()
txt11 = Entry(window, width=100, textvariable=passwrd)
txt11.grid(row=6, column=1)

# IpAddress Line 7
L12 = Label(window, text="Host IPs", font=("Arial Bold", 14))
L12.grid(row=7, column=0)

addr = StringVar()
txt12 = Entry(window, width=100, textvariable=addr)
txt12.grid(row=7, column=1)


########################## END OF GUI MAIN WINDOW######################################################


###################### The Function that will be used to change the password#############################
def changePasswdTriger():
    # read the string variables after user input in the GUI window
    username = user.get()
    passwd = passwrd.get()
    serveradd = addr.get()
    serveraddlist = serveradd.split(',')
    print("Changing The Passwords For The Following Hosts", serveraddlist)
    for serverIP in serveraddlist:
        print("Changing The Passwords For", serverIP)
        sshconnect(serverIP, username, passwd)

    ####This is the part you need to edit it to complete your target function###############


def sshconnect(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password)
    return ssh


def sendread(commandline, prmt):
    X = 1
    chan.send(commandline)
    resp = """"""
    buff = """"""
    buffprint = """"""

    while X == 1:
        resp1 = chan.recv(9999).decode()
        # ansi_escape = re.compile(r'\x1b[^m]*m')
        # resp1 = ansi_escape.sub('', resp)

        X = 2
        if resp1.find(prmt) == -1:
            X = 1
        buff += resp1
        buffprint = resp1
        if buffprint == "":
            pass
        else:

            print(buffprint, end="")
            buffprint = ""
    return buff

    # ssh = sshconnect()
    # chan = ssh.invoke_shell()
    # txt = sendread("", "#")
    # txt = sendread("\n", "#")
    # txt = sendread("passwd\n", ":")
    # # print(txt)
    # txt = sendread(new_pass, ":")
    # txt = sendread(new_pass, ":")
    # txt = sendread("\n", "#")
    # txt = sendread("\n", "#")
    # ssh.close()


# for serverIP in serveraddlist:
#     print(serverIP)
    # ssh=sshconnect(serverIP)
    # chan = ssh.invoke_shell()

###################### END of The Function that will be used to change the password#############################


#################### Define the Button that will be used to call the changePasswd Function#########################################
DUS = tkinter.Button(window, text="APPLY CHANGE PASSWORD ON ALL NODES IN CLUSTER", command=changePasswdTriger, fg="black",
                     width="50",
                     font=("Arial Bold", 10), bd='6', height="2")
DUS.grid(row=40, column=1)

window.mainloop()
