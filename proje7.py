if __name__ == '__main__':
    lst = [ ]
    names , scores = [ ] , [ ]
    for i in range( int( input() ) ):
        name = input()
        score = float( input() )
        scores.append( score )
        lst.append( [ name , score ] )
    count = scores.count( min( scores ) )
    print( count )
    while count > 0:
        lst.remove( min( lst , key=lambda t: (t[ 1 ] , t[ 0 ]) ) )
        count -= 1
        print( lst )
        print( count )

    for a , b in lst:
        names.append( a )
        scores.append( b )
    found = lambda x: scores[ x ] == min( scores )
    loind = [ x for x in range( len( scores ) ) if found( x ) ]
    print( loind )
    nms = [ ]
    print( names )
    for i in loind:
        nms.append( names[ i ] )

    nms.sort()
    print( *nms , sep='\n' )
