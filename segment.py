import sys
from collections import defaultdict


name = sys.argv[1]

f = open(name,'r')

corpus = f.read()

# Removing word boundaries and stress marks:

corpus = corpus.replace("#","+") 
corpus = corpus.replace("0","")
corpus = corpus.replace("1","")
corpus = corpus.replace("2","")

# Inserting utterance boundaries:
corpus = '/ + '+corpus
lines = corpus.split('\n')
final = (" + /"+'\n'+'/ + ').join(lines)
final_lines = final.split('\n')

d = defaultdict(int) #keeps track of syllable counts 
d2 = defaultdict(int) #keeps track of bigram counts
p = defaultdict(int) #keeps track of bigram probabilites 

# Finding syllable and bigram counts:
for line in final_lines:
	syl = line.split('+') #getting individual syllables in a list by splitting on '+'
	for i in range(0, len(syl)-1):
		d[syl[i]]+=1 
		bi = syl[i]+'|'+syl[i+1] #constructing bigrams 
		d2[bi]+=1


# Finding bigram probabilites:
for key in d2:
	bi_1 = ""
	copy = key
	#extracting first element of bigram pair:
	for unit in copy:
		if(unit!='|'):
			bi_1 = bi_1+unit
		if(unit=='|'):
			break
	#calculating probability:
	p[key] = (d2[key])/(d[bi_1])


result = ""

# Inserting word boundaries:
for line in final_lines:
        syl = line.split('+') #getting syllables in each line
        probs = [] #list that keeps track of bigram probabilites for current line
        for i in range(0,len(syl)-1):
                probs.append(p[syl[i]+'|'+syl[i+1]]) #adding probabilites to list

        grid = [] #grid to keep track of positions to insert word boundaires
        for i in range(0,len(probs)-2):
                if((probs[i+1]<probs[i]) and (probs[i+1]<probs[i+2])):#checking for local minimum
                        grid.append(i+2)# i+2 here will be the position of a boundary, if the local minimum condition is satisfied, this position is stored

        melt = line.split(' ')#get individual elements of the line and make it mutable

        plus_count = 0

        # the following part works by matching the positions saved in 'grid' to the plus signs in each line and inserting word boundaries accordingly. 
        for i in range (0, len(melt)):
                if(melt[i] == '+'):
                        plus_count+=1
                if(plus_count in grid):
                        melt[i] = '#'
                        grid.remove(plus_count)
        
        line = ' '.join(melt)
        cut_line = ""

        #trimming utternace boundaries to match BRENT_CMU format:
        for i in range(4,len(line)-4):
                cut_line = cut_line+line[i]
        #final result:             
        result = result + cut_line + '\n'


print(result)



        

        
        
        
        
        
        

