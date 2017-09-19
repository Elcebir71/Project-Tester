T = int( input() )
for case in range( T ):
    try:
        [ a , b ] = list( map( int , input().split() ) )
        print( a // b )
    except ZeroDivisionError as e:
        print( "Error Code: %s" % e )
    except ValueError as g:
        print( "Error Code: %s" % g )
