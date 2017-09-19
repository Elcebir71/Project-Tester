import re
from html.parser import HTMLParser


class MyHTMLParser( HTMLParser ):
    def handle_comment(self , data):
        if bool( re.search( '[\n]' , data ) ):

            print( ">>> Multi-line Comment" )
            print( data.lstrip( ' ' ) )
        else:
            print( ">>> Single-line Comment" )
            print( data.lstrip( ' ' ) )

    def handle_data(self , data):
        if data != '\n':
            print( ">>Data" )
            print( data.lstrip( ' ' ) )


html = ""
for i in range( int( input() ) ):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed( html )
parser.close()
