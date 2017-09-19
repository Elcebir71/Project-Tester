import re

N = int( input() )
for i in range( N ):
    no = input()
    if re.match( r'^((7|8|9)\d{9}$)' , no ):
        print( 'YES' )
    else:
        print( 'NO' )
