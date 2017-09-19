from itertools import permutations

S , k = input().strip().split( ' ' )
lst = set( permutations( S , int( k ) ) )
lst = sorted( lst )
for i in range( len( lst ) ):
    print( ''.join( lst.__getitem__( i ) ) , end='\n' )
