n = int( input() )
A = set( map( int , input().split() ) )
for i in range( int( input() ) ):
    s = input().split()
    B = set( map( int , input().split() ) )

    eval( 'A.{0}(B)'.format( *s ) )

print( sum( A ) )
