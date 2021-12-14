import os.path
import gzip

folder = 'vt_1.0/'

#treatment_postfixes = ['000000_0.000000', '000000_0.100000', '000000_0.300000', '000000_0.400000', '000000_0.500000']
treatment_postfixes = ['0.002', '0.06', '0.14', '1.0']
vt = ['0.1', '0.3', '0.7']
partners = ["Host", "Sym"]
reps = range(10, 21)
#reps = range(1001, 1021)
final_update = 1000
header = "uid treatment rep update donate partner\n"

outputFileName = "munged_basic.dat"

outFile = open(outputFileName, 'w')
outFile.write(header)

for t in treatment_postfixes:
    for r in reps:
        for p in partners:
            fname = p + "Vals" + "_Seed" + str(r) + "_VT" + "0.1" + "_MS" + t + ".data" 
            uid = t + "_" + str(r)
            curFile = open(fname, 'r')
            for line in curFile:
                if (line[0] != "u"):
                    splitline = line.split(',')
                    if int(splitline[0]) == final_update:
                        outstring1 = "{} {} {} {} {} {}\n".format(uid, t, r, splitline[0], splitline[1], p)
                        outFile.write(outstring1)
            curFile.close()
outFile.close()
