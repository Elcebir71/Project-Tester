import re

N = int( input() )
for i in range( N ):
    line = input()
    first = re.sub( '(?<=\s)\&{2}(?=\s)' , ' and ' , line )
    second = re.sub( r'(?<=\s)\|{2}(?<=\s)' , ' or ' , first )
    print( second )
