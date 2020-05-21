import paramiko
p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
p.connect("192.168.1.22", username="root", password="nutanix/4u")
stdin, stdout, stderr = p.exec_command("ls")
opt = stdout.readlines()
opt2 = stderr.readlines()
# opt ="".join(opt)
print(opt2)