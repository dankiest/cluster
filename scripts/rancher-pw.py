from functions import ssh

cmd = '''
sudo docker logs rancher 2>&1 | grep "Bootstrap Password:"
'''

ssh('117', cmd)