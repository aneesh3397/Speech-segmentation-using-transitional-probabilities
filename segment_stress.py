import sys
from collections import defaultdict


#The first part of this model inserts word boundaries according to transitional probabilities just like segment.py

textname = sys.argv[1]

textfile = open(textname,'r')

corpus = textfile.read()
corpus = corpus.replace("#","+")
corpus = '/ + '+corpus
lines = corpus.split('\n')
final = (" + /"+'\n'+'/ + ').join(lines)
final_lines = final.split('\n')

d = defaultdict(int)
d2 = defaultdict(int)
p = defaultdict(int)

for line in final_lines:
	syl = line.split('+')
	for i in range(0, len(syl)-1):
		d[syl[i]]+=1
		bi = syl[i]+'|'+syl[i+1]
		d2[bi]+=1


for key in d2:
	bi_1 = ""
	copy = key
	for unit in copy:
		if(unit!='|'):
			bi_1 = bi_1+unit
		if(unit=='|'):
			break
	p[key] = (d2[key])/(d[bi_1])

result = ""

for line in final_lines:
        syl = line.split('+')
        probs = []
        for i in range(0,len(syl)-1):
                probs.append(p[syl[i]+'|'+syl[i+1]])

        grid = []
        for i in range(0,len(probs)-2):
                if((probs[i+1]<probs[i]) and (probs[i+1]<probs[i+2])):
                        grid.append(i+2)

        melt = line.split(' ')

        plus_count = 0
        
        for i in range (0, len(melt)):
                if(melt[i] == '+'):
                        plus_count+=1
                if(plus_count in grid):
                        melt[i] = '#'
                        grid.remove(plus_count)
        
        line = ' '.join(melt)
        cut_line = ""
        
        for i in range(4,len(line)-4):
                cut_line = cut_line+line[i]
                
        result = result + cut_line + '\n'

#the following part inserts word boundaries in accordance to the second stress prinicple:
#Words in English tend not to end on a stressed syllable (vowel with a ‘1’ or ‘2’)

#General formatting:
result = '/ + '+result
lines = result.split('\n')        
final = (" + /"+'\n'+'/ + ').join(lines)
final_lines = final.split('\n')

del final_lines[-1]

del final_lines[-1]

result_2 = ""

#the following code implements the stress principle by looking for a boundary (+) and backtracking to the previous character. If it is not a 1 or a 2, the + is changed to a word boundary

for line in final_lines:
    melt = line.split(' ')
    for i in range (0,len(melt)):
        if(melt[i]=='+'):
            if((melt[i-1][len(melt[i-1])-1])!='1' and (melt[i-1][len(melt[i-1])-1])!='2'):
                melt[i] = '#'
            

    line = ' '.join(melt)
    cut_line = ""
        
    for i in range(4,len(line)-4):
                cut_line = cut_line+line[i]
    #final output:               
    result_2 = result_2 + cut_line + '\n'

print(result_2)



        

        
        
        
        
        
        

