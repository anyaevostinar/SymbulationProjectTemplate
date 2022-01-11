#a script to run several replicates of several treatments locally
#You should create a directory for your result files and run this script from within that directory

seeds = range(21, 41)
verts = [0.3]
h_mut_rate = [0.1, 0.5, 1.0]

import subprocess

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

for a in seeds:
    for b in verts:
        for c in h_mut_rate:
            command_str = './symbulation -UPDATES 10001 -SYNERGY 3 -MUTATION_RATE 0.1 -SEED '+str(a)+ ' -VERTICAL_TRANSMISSION ' +str(b)+ ' -EFFICIENCY_MUT_RATE -1'+' -HORIZ_MUTATION_RATE '+ str(c) +' -FILE_NAME _Seed'+str(a)+'_VT'+str(b)+'_MR'+str(c) +' -GRID_X 100 -GRID_Y 100'
            print(command_str)
            cmd(command_str)
