from itertools import *

N = int( input() )
S = input().split( ' ' )
K = int( input() )
lst = list( combinations( S , K ) )
count = 0
for sublist in lst:
    if 'a' in sublist:
        count += 1
print( "{0:8.3f}".format( (count / len( lst )) ) )
