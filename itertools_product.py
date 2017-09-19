from itertools import product

A = list( map( int , (input().split()) ) )
B = list( map( int , (input().split()) ) )
W = list( product( A , B ) )
for i in range( len( A ) * len( B ) ):
    print( W.__getitem__( i ) , end='' )
