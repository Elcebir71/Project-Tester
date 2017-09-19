[ N , X ] = list( map( int , input().split( " " ) ) )
subject = [ ]
for case in range( X ):
    subject.append( list( map( float , input().split( " " ) ) ) )

subjects = list( zip( *subject ) )
ave = [ sum( x ) / X for x in subjects ]
for i in range( N ):
    print( "%4.1f" % ave[ i ] )
