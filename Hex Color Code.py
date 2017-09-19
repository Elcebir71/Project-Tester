import re

N = int( input() )

for i in range( N ):
    S = input()
    hex = re.findall( '[\s:](#[\da-fA-F]{6}|#[\da-fA-F]{3})' , S , re.I )
    if hex != [ ]:
        print( *hex , sep="\n" )
