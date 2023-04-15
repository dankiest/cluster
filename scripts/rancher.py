from functions import ssh

cmd = '''
sudo docker run --privileged -d --restart=unless-stopped --name=rancher -p 80:80 -p 443:443 -v /etc/ssl/rancher/certificado_unifor_completo.pem:/etc/rancher/ssl/cert.pem -v /etc/ssl/rancher/certificado_unifor-key.pem:/etc/rancher/ssl/key.pem rancher/rancher --no-cacerts
while ! curl -k https://localhost/ping; do sleep 3; done
'''

ssh('117', cmd)