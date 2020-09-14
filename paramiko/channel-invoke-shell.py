import paramiko

# 接続
client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect("192.168.0.20", username='zaki', key_filename="/home/zaki/.ssh/id_rsa_nopass")

# channel = client.invoke_shell()
# channel.exec_command("hostname") ## paramiko.ssh_exception.SSHException: Channel closed.

channel = client.invoke_shell()
channel.send("hostname")
result = channel.recv(1024)           # buf size: 適当
print(result)                         # b'Last login: Mon Sep 14 23:17:21 2020 from 192.168.0.18\r\r\n'
result = channel.exit_status_ready()  # 使いどころわからん
print(result)                         # False


client.close()
