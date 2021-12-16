#a script to run several replicates of several treatments locally
#You should create a directory for your result files and run this script from within that directory

seeds = range(21, 41)
#start_mois = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 40, 60, 80, 100]
#start_mois = [1]
#slrs = [15]
#verts = [0.1, 0.3, 0.7]
verts = [0.3]
#sym_ints = [-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0]
#h_mut_rate = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
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

print("Copying SymSettings.cfg and executable to current directory")
cmd("cp ../../SymSettings.cfg .")
cmd("cp ../../symbulation .")

for a in seeds:
    for b in verts:
        for c in h_mut_rate:
            command_str = './symbulation -UPDATES 10001 -SYNERGY 3 -MUTATION_RATE 0.1 -SEED '+str(a)+ ' -VERTICAL_TRANSMISSION ' +str(b)+ ' -EFFICIENCY_MUT_RATE -1'+' -HORIZ_MUTATION_RATE '+ str(c) +' -FILE_NAME _Seed'+str(a)+'_VT'+str(b)+'_MR'+str(c) +' -GRID_X 100 -GRID_Y 100'
    #            command_str = './symbulation -SEED '+str(a)+' -VERTICAL_TRANSMISSION '+str(b)+' -FILE_PATH '+directory+' -FILE_NAME _Seed'+str(a)+'_VT'+str(b)+'_MR'+str(c)
    #            command_str = './symbulation -SEED '+str(a)+' -START_MOI '+str(b)+' -FILE_PATH '+directory+' -FILE_NAME SM'+str(b)+'_Seed'+str(a)+'_SLR'+str(c)+' -SYM_LYSIS_RES '+str(c)
    #            command_str = './symbulation -SEED '+str(a)+' -START_MOI '+str(b)+' -FILE_PATH '+directory+' -FILE_NAME SM'+str(b)+'_Seed'+str(a)+'_VT'+str(c)+' -VERTICAL_TRANSMISSION '+str(c)
    #            command_str = './symbulation -SEED '+str(a)+' -START_MOI '+str(b)+' -FILE_PATH '+directory+' -FILE_NAME SM'+str(b)+'_Seed'+str(a)+'_SINT'+str(c)+' -SYM_INT '+str(c)
    #        command_str = './symbulation -SEED '+str(a)+' -VERTICAL_TRANSMISSION '+str(b)+' -FILE_NAME _VT'+str(b)+'_Seed'+str(a) + " -FILE_PATH "+directory
            
            print(command_str)
            cmd(command_str)
