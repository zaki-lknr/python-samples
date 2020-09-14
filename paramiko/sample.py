import paramiko

# 接続
client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect("192.168.0.20", username='zaki', key_filename="/home/zaki/.ssh/id_rsa_nopass")

stdin, stdout, stderr = client.exec_command("hostname")
for line in stdout:
    print(line)
stdin, stdout, stderr = client.exec_command("/sbin/ip a")
for line in stdout:
    print(line.rstrip())

client.close()
