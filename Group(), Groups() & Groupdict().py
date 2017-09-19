import re

S = input().strip( ".,  _" )
res = (re.search( r"(\w)\1+" , S ))
if res is None:
    print( -1 )
else:
    print( res.group( 1 ) )
