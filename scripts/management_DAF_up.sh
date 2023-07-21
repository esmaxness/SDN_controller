#!/bin/bash

echo '----------------------------'

echo '---- VLAN ---'

modprobe 8021q
#ip link add link eno1 name eno1.10 type vlan id 10
#ip link set dev eno1 up
#ip link set dev eno1.10 up
ip link add link eno1 name eno1.100 type vlan id 100
ip link set dev eno1 up
ip link set dev eno1.100 up

echo '--- Loading Irati Modules ----'

modprobe rina-irati-core irati_verbosity=8
modprobe rina-default-plugin
modprobe normal-ipcp
modprobe shim-eth
modprobe shim-tcp-udp

/etc/init.d/ssh start

echo '------------------------------'
echo '---- Running Management DAF ----'
ipcm -c /etc/ipcm-management.conf -a "console, scripting, mad" -l DEBUG &> log &
sleep 30

echo '---- Running RINA Manager ---- '
net_manager -d management --manager-apn terminet.manager -t /tmp/DifTemplates &> management_log &
sleep 10

echo '---- Running Console ----'
irati-ctl list-ipcps
