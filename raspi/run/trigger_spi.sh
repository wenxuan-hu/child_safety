#!/bin/bash
rm  /home/pi/Workspaces/prj/run/spi_rx
cd /home/pi/Workspaces/prj/spi/cpp_source
./spi_single > /home/pi/Workspaces/prj/run/spi_rx
