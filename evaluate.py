import sys
import math
import re
import random
from collections import defaultdict

def readFile(fn):
    """Given a filename, opens the file, and stores the file as a list of formatted lines"""
    f = open(fn, "r")
    utts = []
    for line in f:
        line = line.strip()
        line = re.sub('[0-9]','',line)
        symbs = line.split()
        utts.append(symbs)
    return utts

def getCounts(correct, output):
    (TP,TN, FP, FN) = (0.0, 0.0, 0.0, 0.0)

    for cline, oline in zip(correct, output):
        if (len(cline) != len(oline)):
            print ("Cannot evaluate segmentation because output does not have the same number of symbols as the corpus")
            print ("CORPUS LINE:\t" + " ".join(cline))
            print ("OUTPUT LINE:\t" + " ".join(oline))
            sys.exit(0)
        else:
            for c, o in zip(cline,oline):
                #both lines should have boundaries in the same places, exit otherwise
                if not (((c=='#' or c=='+') and (o=='#' or o=='+')) or (c!='#' and c!='+' and o!='#' and o!='+')):
                    print ("FORMAT ERROR: Boundary symbols don't match up")
                    print ("CORPUS LINE:\t" + " ".join(cline))
                    print ("OUTPUT LINE:\t" + " ".join(oline))
                    sys.exit(0)
                #if there should be a word boundary here
                if (c == '#'):
                    if (o == '#'): TP += 1
                    else: FN +=1
                # this is not supposed to be a boundary
                elif (c == '+'):
                    if (o == '#'): FP += 1
                    else: TN +=1
    return (TP, TN, FP, FN)

Corpus = readFile(sys.argv[1])
Output = readFile(sys.argv[2])

(TP, TN, FP, FN) = getCounts(Corpus, Output)

P = TP/(TP+FP)
R = TP/(TP+FN)
F = (2*P*R)/(P+R)
A = (TP+TN)/(TP+TN+FP+FN)
HR = TP/(TP+FN)
FR = FP/(FP+TN)
    
print ("(TP, TN, FP, FN) are (%i, %i, %i, %i)" % (TP, TN, FP, FN))
print ("Precision:\t%.3f" % (P))
print ("Recall:  \t%.3f" % (R))
print ("F-score:\t%.3f" % (F))
print ("Accuracy:\t%.3f" % (A))
print ("Hit Rate:\t%.3f" % (HR))
print ("False Alarm Rate:\t%.3f" % (FR))

 

