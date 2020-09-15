import configparser
import argparse
import paramiko
import re


ini = configparser.SafeConfigParser()
ini.read('authenticate.conf')
esxihost = ini.get('esxi', 'host')
username = ini.get('esxi', 'username')
password = ini.get('esxi', 'password')

# print(username)
# print(password)

parser = argparse.ArgumentParser()
parser.add_argument("vm", help="vmname")
args = parser.parse_args()
# print(args.vm)
vmname = args.vm
vmlist = {}

pattern = '(\d+)\s+(.+?)\s+\[(.+)\] (.+\.vmx)\s+(\S+)\s+(\S+)'

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect(esxihost, username=username, password=password)

stdin, stdout, stderr = client.exec_command("vim-cmd vmsvc/getallvms")
for line in stdout:
    # print(line.rstrip())
    result = re.match(pattern, line)
    if result:
        vmlist[result.group(2)] = {
            "vmid": result.group(1),
            "ds": result.group(3),
            "file": result.group(4),
            "guest": result.group(5),
            "version": result.group(6)
        }
# print("\n")

vmid = vmlist[vmname]["vmid"]
power_state_on = True
stdin, stdout, stderr = client.exec_command("vim-cmd vmsvc/power.getstate " + vmid)
for line in stdout:
    #print(line.rstrip())
    result = re.match("^Powered (.+)", line)
    if result:
        if result.group(1) == "on":
            power_state_on = True
        elif result.group(1) == "off":
            power_state_on = False
        else:
            raise Exception("unknown state: '" + result.group(1) + "'")

print("state: " + str(power_state_on))

stdin.close()
stdout.close()
stderr.close()

client.close()

# print(vmlist)
# print(vmlist[vmname]["vmid"])
