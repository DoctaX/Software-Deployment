import paramiko
from creds import User
from args import env_args

user = User()
creds = user.authenticate()

local_software_path = env_args[0]
remote_host_path = env_args[1]

host_file = open(".\hosts.txt", "r")

ssh_client = paramiko.SSHClient
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for host in host_file:
  ssh_client.connect(hostname=host, username=creds[0], password=creds[1])
  ftp_client = ssh_client.open_sftp()
  ftp_client.put(local_software_path, remote_host_path)
  ftp_client.close()
  ssh_client.close()