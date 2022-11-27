import configparser

ini = configparser.ConfigParser()
ini.read('sample.ini')
interpreter = ini.get('defaults', 'interpreter_python')
ssh_config = ini.get('ssh_connection', 'ssh_args')

print(interpreter)
print(ssh_config)
