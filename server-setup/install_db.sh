#!/bin/sh

setenforce 0
sed -i -e 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
iptables -F
chkconfig iptables off

yum install -y -q mysql-server
cat << EOF > /etc/my.cnf
[mysqld]
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
user=mysql
symbolic-links=0
character-set-server=utf8

innodb_file_per_table
query-cache-size=16M

[mysqld_safe]
log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid

[mysql]
default-character-set=utf8
EOF
service mysqld start
chkconfig mysqld on
mysql -u root -e "create database sample_bbs default character set utf8;"
mysql -u root -e "grant all on sample_bbs.* to user@'%'       identified by 'password'; flush privileges;"
mysql -u root -e "grant all on sample_bbs.* to user@localhost identified by 'password'; flush privileges;"
