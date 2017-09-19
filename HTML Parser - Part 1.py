import re
from html.parser import HTMLParser


class MyHTMLParser( HTMLParser ):
    def handle_starttag(self , tag , attrs):
        print( "Start :" , tag )
        if attrs != [ ]:
            for elements in range( len( attrs ) ):
                print( "-> %s > %s" % (attrs[ elements ][ 0 ] , attrs[ elements ][ 1 ]) )

    def handle_endtag(self , tag):
        print( "End   :" , tag )

    def handle_startendtag(self , tag , attrs):
        print( "Empty :" , tag )
        if attrs != [ ]:
            for elements in range( len( attrs ) ):
                print( "-> %s > %s" % (attrs[ elements ][ 0 ] , attrs[ elements ][ 1 ]) )


# instantiate the parser and fed it some HTML
N = int( input() )
parser = MyHTMLParser()
for i in range( N ):
    S = input()
    found = re.findall( "body" , S )
    if found != [ ]:
        parser.feed( S )
    else:
        parser.feed( S )
