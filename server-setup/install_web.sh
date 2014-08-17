#!/bin/sh

setenforce 0
sed -i -e 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
iptables -F
chkconfig iptables off

mkdir -p /tmp/flask

cd $(dirname $0)

yum install -y -q gcc python-devel python-crypto python-pip mysql-devel
pip install -q -r requirements.txt
