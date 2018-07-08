import clientprogram


def sshCommand(hostname, port, username, password, command):
    sshClient = clientprogram.SSHClient()

    sshClient.set_missing_host_key_policy(clientprogram.AutoAddPolicy())
    sshClient.load_system_host_keys()
    sshClient.connect(hostname, port, username, password)
    stdin, stdout, stderr = sshClient.exec_command(command)
    print(stdout.read())

if __name__ == '__main__':
    sshCommand('localhost', 22, 'user', 'password', 'ls -l mydir')