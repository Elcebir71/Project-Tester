#!/bin/python3

if __name__ == '__main__':
    N = int( input() )
    list = [ ]
    for i in range( N ):
        str = input().strip().split( " " )
        if str[ 0 ] == 'insert':
            list.insert( int( str[ 1 ] ) , int( str[ 2 ] ) )
        elif str[ 0 ] == 'print':
            print( list )
        elif str[ 0 ] == 'remove':
            list.remove( int( str[ 1 ] ) )
        elif str[ 0 ] == 'append':
            list.append( int( str[ 1 ] ) )
        elif str[ 0 ] == 'sort':
            list.sort
        elif str[ 0 ] == 'pop':
            list.pop
        elif str[ 0 ] == 'reverse':
            list.reverse
