#!/bin/sh

. /etc/rc.d/init.d/functions

retval=0
prog="rest.py"
logfile="rest.log"
pidfile="/var/run/sample-app/rest.pid"

start () {
    echo -n $"Starting $prog"

    if [ ! -d /var/run/sample-app ]; then
         mkdir -p /var/run/sample-app
    fi 

    daemon --pidfile ${pidfile} --user=root "cd $(dirname $0); cd ../; python $prog >> $logfile"
    RETVAL=$?
    echo

    return $retval
}

case "$1" in
    start)
       start
       $1
    ;;
    stop)
       rh_status_q || exit 0
       $1
    ;;
    restart)
       $1
    ;;
    status)
       rh_status
    ;;
    *)
       echo $"Usage: $0 {start|stop|status|restart}"
       exit 2
esac

