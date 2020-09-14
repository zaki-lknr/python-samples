import configparser
import paramiko

ini = configparser.SafeConfigParser()
ini.read('authenticate.conf')
esxihost = ini.get('esxi', 'host')
username = ini.get('esxi', 'username')
password = ini.get('esxi', 'password')

# print(username)
# print(password)

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect(esxihost, username=username, password=password)

stdin, stdout, stderr = client.exec_command("vim-cmd vmsvc/getallvms")
for line in stdout:
    print(line.rstrip())
print("\n")

stdin.close()
stdout.close()
stderr.close()

client.close()
