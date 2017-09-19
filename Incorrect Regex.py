import re

T = int( input() )
D = 'abcdefg0123456789!^+%&/()=?'
for case in range( T ):
    try:
        S = input()
        compiled = re.compile( S )
    except re.error as e:
        print( "False" )
    else:
        print( "True" )
