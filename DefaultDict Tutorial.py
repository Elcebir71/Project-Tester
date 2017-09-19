from collections import defaultdict

n , m = list( map( int , input().split() ) )
inpt = defaultdict( list )
for i in range( n ):
    inpt[ 'A' ].append( input() )
for j in range( m ):
    inpt[ 'B' ].append( input() )
for k in range( m ):
    col1 = [ str( i ) for i , j in enumerate( inpt[ 'A' ] , start=1 ) if j == inpt[ 'B' ][ k ] ]
    if col1 == [ ]:
        print( '-1' , end="\n" )
    else:
        for i in range( len( col1 ) ):
            print( ''.join( col1.__getitem__( i ) ) , sep=" " , end="" )
        print( '' )
