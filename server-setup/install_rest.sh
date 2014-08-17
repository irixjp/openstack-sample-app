#!/bin/sh

setenforce 0
sed -i -e 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
iptables -F
chkconfig iptables off

cd $(dirname $0)

yum install -y -q gcc python-devel python-crypto python-pip mysql-devel \
libxml2 libxml2-devel libxslt libxslt-devel \
libffi libffi-devel openssl-devel libyaml libyaml-devel
pip install -q -r requirements.txt

