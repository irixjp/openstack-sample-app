#!/bin/sh

. /etc/rc.d/init.d/functions

retval=0
prog="web.py"
logfile="web.log"

start () {
    echo -n $"Starting $prog"

    daemon --user=root "cd $(dirname $0); cd ../; python $prog >> $logfile 2>&1 &"
    retval=$?
    echo
    return $retval
}

stop () {
    pid=`ps -ef |grep "/usr/bin/python $prog" | grep -v grep | awk '{print $2}'`
    kill $pid
    retval=$?
    echo
    return $retval
}

restart () {
    stop
    sleep 3
    start
}

case "$1" in
    start)
       $1
    ;;
    stop)
       $1
    ;;
    restart)
       $1
    ;;
    *)
       echo $"Usage: $0 {start|stop|restart}"
       exit 2
esac

