S = input().strip()
try:
    S = int( S )
except TypeError:
    print( "Bad String" )
else:
    print( S )
