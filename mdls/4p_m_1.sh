#!/bin/bash
#PBS -l nodes=1:ppn=8
#PBS -l walltime=340:00:00              
#PBS -j oe
#PBS -q bigmem

set echo

cd /usr/users/7/dittrich/data/az_model/mouse_model_4p_50hz_042015/mouse_control_model


./run_all.sh
