import numpy as np
import tools as tl

def read_1st_guess():
    tab= np.loadtxt('words_ranked.txt',dtype='str')
    print(tab[:,0], tab[:,1].astype(np.float))
    return True

# read_1st_guess()

# d = {}
# d['g'] = 2
# print(('g' in d))
# print(d)
tab= np.loadtxt('words_ranked.txt',dtype='str')
# a = ['a','b','c','i','j']
words = tab[:,0]

words_split = tl.split_in_array(words)

# Truth = 0
# for el in a:
#     Truth +=  (words_split == el)
# Truth = np.sum(Truth,axis = 1)
# print(words[Truth==0])
# print(words_split[Truth==0])

# a = {}
# a['o'] = 1
# a['s'] = 2


# Truth = 1
# for el in a:
#     print(el)
#     Truth = np.logical_and(Truth,words_split[:,a[el]] == el)
# print(words[Truth])
# # print(words_split[Truth])

# a = {}
# a['e']=[1,2]
# a['o'] = [1,2]
# a['s'] = [1,2]

# Truth = 1
# for letter in a:
#     cols = list(set(range(0,5))-set(a[letter]))
#     auxTruth = (words_split[:,cols] == letter)
#     Or = np.sum(auxTruth, axis = 1)
#     auxTruth = (Or > 0)

#     auxTruth2 = 1
#     for col in a[letter]:
#         auxTruth2 = np.logical_and(auxTruth2, 1-(words_split[:,col]==letter))
    
#     Truth = np.logical_and(Truth, auxTruth)
#     Truth = np.logical_and(Truth, auxTruth2)

# print(words[Truth])
print([1,2]+[3,4])