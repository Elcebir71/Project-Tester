from html.parser import HTMLParser


class MyHTMLParser( HTMLParser ):
    def handle_starttag(self , tag , attrs):
        print( tag )
        if attrs != [ ]:
            for elements in range( len( attrs ) ):
                print( "-> %s > %s" % (attrs[ elements ][ 0 ] , attrs[ elements ][ 1 ]) )

    def handle_startendtag(self , tag , attrs):
        print( tag )
        if attrs != [ ]:
            for elements in range( len( attrs ) ):
                print( "-> %s > %s" % (attrs[ elements ][ 0 ] , attrs[ elements ][ 1 ]) )


# instantiate the parser and fed it some HTML
N = int( input() )
parser = MyHTMLParser()
for i in range( N ):
    S = input()
    parser.feed( S )
