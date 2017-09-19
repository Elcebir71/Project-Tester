#!/bin/python3

Q = int( input().strip() )


def Sum(x):
    if (x % 8 == 0) | (x % 8 == 1):
        return x
    elif (x % 8 == 2) | (x % 8 == 3):
        return 2
    elif (x % 8 == 4) | (x % 8 == 5):
        return x + 2
    elif (x % 8 == 6) | (x % 8 == 7):
        return 0


for a0 in range( Q ):
    L , R = input().strip().split( ' ' )
    L , R = [ int( L ) , int( R ) ]
    result = Sum( R ) ^ Sum( L - 1 )
    print( result )
