#!/bin/sh

setenforce 0
sed -i -e 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
iptables -F
chkconfig iptables off

cd $(dirname $0)

yum install -y gcc python-devel python-crypto python-pip mysql-devel
pip install -r requirements.txt

