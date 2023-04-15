import re
import paramiko

def server():
    return 'https://rancher-dev.unifor.br'

def address(octeto):
    return '172.20.100.' + octeto

def token():
    return 'kg85x8mjchb466mfs2mfg2x8gj25s724fl4tx64ftcbng5slm66jbz'

def checksum():
    return 'ced137660910ef28ceb37c35b185cea614ec7155182fd822e1833cfac720eca6'

def ssh(octeto, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('172.20.100.' + octeto, username='root', password='Sup0rt3!')
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode("utf-8"), stderr.read().decode("utf-8"))
    stdin.close()
