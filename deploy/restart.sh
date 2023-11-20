#!/bin/sh
# Add your startup script

# DO NOT DELETE
# sleep 5
# cp /flag.txt /home/ctf
/etc/init.d/xinetd start;
service ssh start;
sleep infinity;
