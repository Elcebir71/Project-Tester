import itertools

K , M = map( int , input().split( ' ' ) )
S = [ ]
for i in range( int( K ) ):
    R = list( map( int , input().split( ' ' ) ) )
    Rsqr = [ ((x ** 2) % M) for x in R[ 1:len( R ) + 1 ] ]
    S.append( Rsqr )
Scom = list( itertools.product( *S ) )
Sm = (list( map( sum , Scom ) ))
Smax = [ item % M for item in Sm ]
print( Smax )
