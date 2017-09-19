import re

S = input().strip( ".," )
res = list( re.split( "\W+" , S ) )
print( *res , sep="\n" )
