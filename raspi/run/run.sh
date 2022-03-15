#!/bin/bash
rm  /home/pi/Workspaces/prj/run/result
cd /home/pi/Workspaces/prj/darknet
./darknet  detect cfg/yolov3.cfg  cfg/yolov3.weights  /home/pi/test/image0.jpg > /home/pi/Workspaces/prj/run/run.log
#rm  /home/pi/Workspaces/prj/run/result
cat /home/pi/Workspaces/prj/run/run.log | grep -i "dog" >> /home/pi/Workspaces/prj/run/result
cat /home/pi/Workspaces/prj/run/run.log | grep -i "person" >> /home/pi/Workspaces/prj/run/result
cat /home/pi/Workspaces/prj/run/run.log | grep -i "cat" >> /home/pi/Workspaces/prj/run/result
