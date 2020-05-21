import paramiko



p = paramiko.SSHClient()



file = open("c:\servers.txt","r")
username = "root"
password = "CDC@nutanix/4u1"
new_password = "CDC@nutanix/4u2@@"

for i in file.readlines():
    # try:
        line=i.strip()
        ls =line.split()
        print(ls)
        p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        p.connect(ls[0],port =22, username = username , password=password)
        stdin, stdout, stderr = p.exec_command("passwd")



        # stdin, stdout, stderr = p.exec_command(new_password)
        opt = stdout.readlines()
        # opt ="".join(opt)
        print(opt)
    # except:
    #     error = stderr.readlines()
    #     print(error)
    # temp=open("%s.txt"%ls[0],"w")
    # temp.write(opt)
    # temp.close()
stdin, stdout, stderr = p.exec_command(new_password)
file.close()