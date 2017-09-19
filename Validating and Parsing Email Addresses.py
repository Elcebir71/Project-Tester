import email.utils
import re

N = int( input() )
for i in range( N ):
    [ name , mail ] = input().strip( ">" ).split()
    mail = mail.strip( "<" )
    if re.match( r'^[^.-_][\w.-]+\@[a-zA-Z]+\.[a-z]{1,3}$' , mail ):
        print( email.utils.formataddr( (name , mail) ) )
