rpi_monitoring
==============

Basic Python/CGI chart of performance on a cluster.

## Overview
This is an elementary approach to real-time monitoring of performance in a Raspberry Pi cluster. A C pi calculation program is submitted to each of a group of RPi processors via MPICH statements. The response time to complete the calculation, for each processor is written to the rpimon.log file. This file is input to the rpimon.py CGI 
program, executed through the browser.

## Program descriptions
### perfchart.py program
#### Command line
`sudo pico /usr/lib/cgi-bin/perfchart.py
sudo chmod +x /usr/lib/cgi-bin/perfchart.py
sudo service apache2 reload
sudo pico -c  /var/www/rpimon.log`
#### Description
* Executes Google Charts
* Executed in Midori browser (http://192.168.1.5/cgi-bin/perfchart.oy) using auto refresh.
* Input: /var/www/rpimon.log and is sorted by processor.
* Can contain IP with 0ms
* If 0. it means that mpi/anythingis not running on that computer

### start_mon script
#### Command line
`export PATH=$PATH:/home/rpimpi/mpich-install/bin
pico start_mon
 (./start_mon '192.168.1' 5 6)`

* Parm 1: First 3 digits of ip group.
* Parm 2: Starting processor (last ip digit)
* Parm 3: Ending processor (last ip digit)

#### Description

* Either manual or Cron initiated.
* Pings all IPs 
* Write  IPs with 0 response to  /var/www/rpimon.log
* Write IPs for a response to machinefile. 
* The machfile is input to rpimon.c indicating the responding IPs.

### rpimon.c
#### Command line  
`cd ~/myapps/rpi_monitoring/
mpicc -g -o rpimon rpimon.c
mpiexec -f machinefile -n 2 ~/myapps/rpi_monitoring/rpimon`
#### Description
* Utilizing MPICH because: MPI is the basis of the parallel cluster
* Uses the example cpi.c 
* Reseponse times are appended to var/www/rpimon.log
