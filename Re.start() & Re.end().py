import re

S = input()
k = input()
starts = [ match.start() for match in re.finditer( '(?={0})'.format( re.escape( k ) ) , S ) ]
if starts == [ ]:
    print( "(-1, -1)" )
else:
    for i in range( len( starts ) ):
        print( "(%d, %d)" % (starts[ i ] , starts[ i ] + len( k ) - 1) )
