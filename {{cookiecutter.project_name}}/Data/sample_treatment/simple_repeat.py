#a script to run several replicates of several treatments locally
#You should create a directory for your result files and run this script from within that directory
# usage: python3 simple_repeat.py <start_seed> <end_seed>
# Assumes that symbulation executable and SymSettings.cfg already in the folder

import subprocess
import sys

verts = [0.0, 1.0]

def cmd(command):
    '''This wait causes all executions to run in sieries.                          
    For parralelization, remove .wait() and instead delay the                      
    R script calls unitl all neccesary data is created.'''
    return subprocess.Popen(command, shell=True).wait()

def silent_cmd(command):
    '''This wait causes all executions to run in sieries.                          
    For parralelization, remove .wait() and instead delay the                      
    R script calls unitl all neccesary data is created.'''
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).wait()

start_range = 10
end_range = 21

if(len(sys.argv) > 1):
    start_range = int(sys.argv[1])
    if(len(sys.argv) > 2):
        end_range = int(sys.argv[2]) + 1
    else:
        end_range = start_range + 1

seeds = range(start_range, end_range)

print("Using seeds", start_range, "through", end_range-1)

for a in seeds:
    for b in verts:
        command_str = './symbulation -SEED '+str(a)+ ' -VERTICAL_TRANSMISSION ' +str(b)+ ' -FILE_NAME _VT'+str(b)
        settings_filename = "Output_VT"+str(b)+"_SEED"+str(a)+".data"

        print(command_str)
        cmd(command_str+" > "+settings_filename)
