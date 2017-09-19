from collections import OrderedDict

S = input()
l = {}
count = 0
for letter in S:
    if letter not in l.keys():
        l.__setitem__( letter , count + 1 )
    else:
        l[ letter ] += 1
new = OrderedDict( sorted( l.items() ) )
mx = 0
lst = [ ]
for case in range( 3 ):
    m = 0
    for each in (new.items()):
        if m < each[ 1 ]:
            big = each
            m = each[ 1 ]
    lst.append( big )
    new.pop( big[ 0 ] )
for case in range( 3 ):
    print( "%s %d" % (lst[ case ][ 0 ] , lst[ case ][ 1 ]) )
