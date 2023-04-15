from functions import ssh, server, address, token, checksum

octetos = ['119']

cmd = '''
sudo docker run -d --privileged --restart=unless-stopped --net=host -v /etc/kubernetes:/etc/kubernetes -v /var/run:/var/run  rancher/rancher-agent:v2.6.6 --server {} --token {} --worker
'''.format(server(), token())

for octeto in octetos:
    ssh(octeto, cmd)