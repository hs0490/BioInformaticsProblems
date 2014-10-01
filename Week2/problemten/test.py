__author__ = 'hs0490'
import itertools
with open('problemten.txt') as f:
    data_list=[s.replace('\n','') for s in f]
len=int(data_list[1])
data_list=data_list[0].split()
for each_product in itertools.product(data_list, repeat=len):
            print ''.join(each_product)
