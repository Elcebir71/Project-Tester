import collections

N = int( input() )
S = collections.OrderedDict()
for i in range( N ):
    word = input().strip( "\n" )
    if word in S:
        S[ word ] += 1
    else:
        S[ word ] = 1
print( S.__len__() )
for k in S.keys():
    print( S.__getitem__( k ) , sep=" " , end=" " )
