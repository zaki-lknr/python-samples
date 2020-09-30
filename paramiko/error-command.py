import paramiko

# 接続
client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect("192.168.0.20", username='zaki', key_filename="/home/zaki/.ssh/id_rsa_nopass")

stdin, stdout, stderr = client.exec_command("ls /not-found")
for line in stdout:
    print(line)

# stat = client.recv_exit_status()
# print(stat)
## ^^^ AttributeError: SSHClientにはrecv_exit_status()は無い

ch = stdout.channel
status = ch.recv_exit_status()
print("stdout status: " + str(status))

ech = stderr.channel
status = ech.recv_exit_status()
print("stderr status: " + str(status))


client.close()