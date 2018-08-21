# Speech-segmentation-using-transitional-probabilities

(This project was done for LING 692c taught by Gaja Jarosz) 

The purpose of this code is to see if transitional probabilites can be used to accurately model speech segmentation. Speech as it is experienced by humans, is a continuous stream of sound with no explicit markers that can be used to determine where a word begins and ends. This poses a (significant) challenge to children attempting to aquire a given language. 

Transitional probability is simply the probability of one sound following another. Within a language, the
transitional probability from one sound to the next will generally be highest when the two sounds follow one another within a
word, whereas transitional probabilities spanning a word boundary will be relatively low (Saffran et al. (1996)). 

The data used was obtained from the BRENT child-directed speech corpus and was modified to include stress markers according to the format of the CMU pronouncing dictionary by the instructor (BRENT_CMU.txt). 

segment.py trains a bigram model on BRENT_CMU.txt and inserts word boundaries where ever a local minimum is encountered, in accordance to the idea of transitional probability mentioned above. 

segment_stress.py makes use of transitional probabilites as well as the fact that that words in English tend not to end on
stressed syllables. The models performance was imporved when stress was taken into account. 

evaluate.py is a script provided by the instructor to evaluate the performance of the model. 

Performance of segment.py was as follows: 
Precision: 0.955
Recall: 0.401
F-score: 0.565
Accuracy: 0.500

Performance of segment_stress.py was as follows:
Precision: 0.932
Recall: 0.875
F-score: 0.902
Accuracy: 0.847




