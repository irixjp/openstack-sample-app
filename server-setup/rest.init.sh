#!/bin/sh

. /etc/rc.d/init.d/functions

cd $(dirname $0)
cd ../

daemon --user=root "python rest.py >> rest.log &"
