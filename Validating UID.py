import re

N = int( input() )
for k in range( N ):
    S = input()
    uid = re.compile(
        r"^(?=(?:[^a-zA-Z]*[a-zA-Z]){2,7}[^a-zA-Z]*$)(?=(?:\D*\d){3,8}\D*$)(?:([a-zA-Z0-9])(?!.*\1)){10}$" )
    if bool( uid.match( S ) ):
        print( "Valid" )
    else:
        print( "Invalid" )
