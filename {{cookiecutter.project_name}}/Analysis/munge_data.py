import os.path
import gzip

folder = ''

#treatment_postfixes = ["VT0.3_MR0.1", "VT0.3_MR0.2", "VT0.3_MR0.3", "VT0.3_MR0.4", "VT0.3_MR0.5", "VT0.3_MR0.6", "VT0.3_MR0.7", "VT0.3_MR0.8", "VT0.3_MR0.9", "VT0.3_MR1.0"]
treatment_postfixes = ["VT0.3_MR0.1", "VT0.3_MR0.5", "VT0.3_MR1.0"]
partners = ["Host", "Sym"]
reps = range(21,41)
#reps = range(1001, 1021)
final_update = 100
header = "uid treatment rep update donate partner\n"

outputFileName = "munged_basic.dat"

outFile = open(outputFileName, 'w')
outFile.write(header)

for t in treatment_postfixes:
    for r in reps:
        for p in partners:
            fname = folder +p+"Vals_Seed" + str(r) + "_" + t + ".data"
            uid = t + "_" + str(r)
            curFile = open(fname, 'r')
            for line in curFile:
                if (line[0] != "u"):
                    splitline = line.split(',')
                    #if int(splitline[0]) == final_update:
                    outstring1 = "{} {} {} {} {} {}\n".format(uid, t, r, splitline[0], splitline[1], p)
                    outFile.write(outstring1)
            curFile.close()
outFile.close()
