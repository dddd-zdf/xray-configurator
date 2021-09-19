import os
import paramiko
def ssh():
    #ssh server and authentication
    f = open("server", "r")
    server = f.readline()[:-1]
    username = f.readline()[:-1]
    password = f.readline()
    f.close()
    #login and update config.json
    ssh = paramiko.SSHClient() 
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(hostname = server, username = username, password = password)
    sftp = ssh.open_sftp()
    sftp.put("config.json", "/usr/local/etc/xray/config.json")
    sftp.close()
    ssh.close()