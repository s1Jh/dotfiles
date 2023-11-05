#!/bin/bash 

BATSTAT=$(acpi -b | grep -E -o '[0-9][0-9]?%') 
BAT=$(acpi -b | cut -c 12-)

# Full and short texts 
echo "$BAT" 
echo "$BAT" 

# Set urgent flag below 5% or use orange below 20% 
[ ${BATSTAT%?} -le 10 ] && dunstfy -u critical "LOW BATTERY" && exit 0
[ ${BATSTAT%?} -le 20 ] && echo "#FF8000" exit 0

