import re

S = input().strip( " +-" )
res = (re.findall( r"([aeiouAEIOU]{2,})[^aeiouAEIOU]" , S ))
if res == [ ]:
    print( -1 )
else:
    print( *res , sep="\n" )
