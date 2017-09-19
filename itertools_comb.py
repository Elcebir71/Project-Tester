from itertools import combinations_with_replacement

S , k = input().strip().split( ' ' )
lst = [ ]
lst = list( combinations_with_replacement( sorted( S ) , int( k ) ) )
lst = sorted( lst )
for i in range( len( lst ) ):
    print( ''.join( lst.__getitem__( i ) ) , end='\n' )
