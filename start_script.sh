#!/bin/bash
#!/bin/python
python /home/pi/Documents/intruder_detection/send_to_server.py >> /tmp/clientlogs.txt &
echo "Started streaming" >> /tmp/notif.txt