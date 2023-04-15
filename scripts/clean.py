from paramiko import SSHClient, AutoAddPolicy

octetos = [119]
rede = '172.20.100.'
username = 'root'
password = 'Sup0rt3!'

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())

print('Stop and prepare Redis...')
for octeto in octetos:
    ip = rede + str(octeto)
    print(ip)
    ssh.connect(ip, username=username, password=password)
    commands = '''
    sudo docker rm -f $(docker ps -qa)
    sudo docker volume rm $(docker volume ls -q)
    sudo rm -rf /etc/ceph \
       /etc/cni \
       /etc/kubernetes \
       /opt/cni \
       /opt/rke \
       /run/secrets/kubernetes.io \
       /run/calico \
       /run/flannel \
       /var/lib/calico \
       /var/lib/etcd \
       /var/lib/cni \
       /var/lib/kubelet \
       /var/lib/rancher/rke/log \
       /var/log/containers \
       /var/log/kube-audit \
       /var/log/pods \
       /var/run/calico
    '''
    stdin, stdout, stderr = ssh.exec_command(commands)
    print(stdout.read().decode("utf-8"), stderr.read().decode("utf-8"))
    stdin.close()
