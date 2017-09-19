from datetime import timedelta , datetime

N = int( input() )
for case in range( N ):
    time1 = datetime.strptime( ''.join( input().rsplit( ':' , 0 ) ) , '%a %d %b %Y %H:%M:%S %z' )
    time2 = datetime.strptime( ''.join( input().rsplit( ':' , 0 ) ) , '%a %d %b %Y %H:%M:%S %z' )
    print( "%d" % abs( timedelta.total_seconds( time1 - time2 ) ) )
