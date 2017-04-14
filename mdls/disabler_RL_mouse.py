#!/usr/bin/env python
#randomly disables a given number of channels in the 48 channel mouse system
#seed value is given by run_*.sh file


import sys
import random
import os
import numpy as np

# list of available channels in the form [row, column] for each channel
#available_channels = ['A01','A04','A09','A13','A17','A21','A25','A29','A33','A38','A42','A46','A49','D01','D04','D09','D13','D17','D21','D25','D29','D33','D37','D42','D46','D49']
#available_channels = ['1_1_3','1_1_8','1_2_3','1_2_8','1_3_3','1_3_8','1_4_3','1_4_8','2_1_3','2_1_8','2_2_3',\
#'2_2_8','2_3_3','2_3_8','2_4_3','2_4_8','3_1_3','3_1_8','3_2_3','3_2_8','3_3_3','3_3_8',\
#'3_4_3','3_4_8','4_1_3','4_1_8','4_2_3','4_2_8','4_3_3','4_3_8','4_4_3','4_4_8','5_1_3','5_1_8',\
#'5_2_3','5_2_8','5_3_3','5_3_8','5_4_3','5_4_8','6_1_3','6_1_8','6_2_3','6_2_8',\
#'6_3_3','6_3_8','6_4_3','6_4_8'] 

available_channels = ['1_2_3','1_2_8','1_3_3','1_3_8','2_2_3','2_2_8','2_3_3','2_3_8','3_2_3','3_2_8','3_3_3','3_3_8',\
'4_2_3','4_2_8','4_3_3','4_3_8','5_2_3','5_2_8','5_3_3','5_3_8','6_2_3','6_2_8','6_3_3','6_3_8']

# number of available AZ
num_AZ = 24

num_channels = int(sys.argv[1])
seed = sys.argv[2]

disabled = []
commands = []
channels = []

#all channel addresses
##for x in range(1,num_AZ+1):
##    for ch in available_channels:
##        channels.append(str(x)+'_'+str(ch[0])+'_'+str(ch[1]))

#writes sed command arguments for each channel to disable
i = 1
line2 = '\\"k3_control_short_1.8_1.txt\\"'
line3 = '\\"k3_control_short_1.8_2.txt\\"'
line4 = '\\"k3_control_short_1.8_3.txt\\"'
line5 = '\\"k3_control_short_1.8_4.txt\\"'

while i <= num_channels:
    #  RL  #j = random.randint(0,len(channels)-1)
    j = random.choice(available_channels)
    if j in disabled:
        continue
    else:
        line1 = 'open_channel_'+j+'\'+ca_'+j
        comm1 = '-e \"/'+line1+'/ s/'+line2+'/0.0/g\"'
        comm2 = '-e \"/'+line1+'/ s/'+line3+'/0.0/g\"'
        comm3 = '-e \"/'+line1+'/ s/'+line4+'/0.0/g\"'
        comm4 = '-e \"/'+line1+'/ s/'+line5+'/0.0/g\"'
        commands.append(comm1)
        commands.append(comm2)
        commands.append(comm3)
        commands.append(comm4)
        disabled.append(j)
        i += 1

#run sed command in shell
if len(commands)>0:
    sed_com = 'sed'
    for each in commands:
        sed_com += ' '+each
    sed_com += ' reactions_template.mdl > reactions.mdl'
    #print "blabla", sed_com
    os.system(sed_com)
else:
    com = 'cp reactions_template.mdl reactions.mdl'
    os.system(com)

#write information to output file
vfile = open('disabled_channels.txt','a')
vfile.write("seed "+seed+': ')
for every in disabled:
    if disabled.index(every)==len(disabled)-1:
        vfile.write(every)
    else: vfile.write(every+' ')
vfile.write('\n')
vfile.close()

