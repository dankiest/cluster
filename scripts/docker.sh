#!/bin/bash
# sudo su
# apk add docker
# addgroup vagrant docker
# rc-update add docker boot
# service docker start
# modprobe ip_tables
# echo 'ip_tables' >> /etc/modules

sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-commom --yes
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt install docker-ce --yes

modprobe ip_tables
echo 'ip_tables' >> /etc/modules
sudo ufw disable