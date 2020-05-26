'''
import paramiko
ip = "192.168.43.89"
user_name="Manoj"
password="319319319"
print ("please wait creating ssh client")
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print ("please wait , connecting with remote server")
ssh_client.connect(hostname=ip, username=user_name, password=password)
cmd = "C:\\Users\\Manoj\\Desktop\\Selenium"
print ("please wait executing command on remote server")
stdin, stdout, stderr = ssh_client.exec_command(cmd)
print ("successfully executed on remote server")
stdout=stdout.readlines()
print (stdout)
'''

import paramiko
print (dir(paramiko))
