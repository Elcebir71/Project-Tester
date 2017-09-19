class complex:
    def __init__(self , r=0 , i=0):
        self.real = r
        self.img = i

    def __add__(C1 , C2):
        real = C1.real + C2.real
        img = C1.img + C2.img
        return print( "{0:.2f}+{1:.2f}i".format( real , img ) )

    def __mul__(C1 , C2):
        real = C1.real * C2.real - C1.img * C2.img
        img = C2.real * C1.img + C2.img * C1.real
        return print( "{0:.2f}+{1:.2f}i".format( real , img ) )

    def __sub__(C1 , C2):
        real = C1.real - C2.real
        img = C1.img - C2.img
        return print( "{0:.2f}-{1:.2f}i".format( real , abs( img ) ) )

    def __truediv__(C1 , C2):
        real = (C1.real * C2.real + C1.img * C2.img) / (C2.real ** 2 + C2.img ** 2)
        img = (C1.img * C2.real - C1.real * C2.img) / (C2.real ** 2 + C2.img ** 2)
        return print( "{0:.2f}+{1:.2f}i".format( real , img ) )

    def __mod__(C1):
        real = (C1.real ** 2 + C1.img ** 2) ** (1 / 2)
        img = 0
        return print( "{0:.2f}+{1:.2f}i".format( real , img ) )


[ a , b ] = list( map( int , input().split( " " ) ) )
[ c , d ] = list( map( int , input().split( " " ) ) )
C1 = complex( a , b )
C2 = complex( c , d )
C1 + C2
C1 - C2
C1 * C2
C1 / C2
complex.__mod__( C1 )
complex.__mod__( C2 )

---------------------------------------------


class Complex( object ):
    def __init__(self , real , imaginary):

    def __add__(self , no):

    def __sub__(self , no):

    def __mul__(self , no):

    def __truediv__(self , no):

    def mod(self):

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs( self.imaginary ))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real , self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real , abs( self.imaginary ))
        return result


if __name__ == '__main__':
    c = map( float , input().split() )
    d = map( float , input().split() )
    x = Complex( *c )
    y = Complex( *d )
    print( *map( str , [ x + y , x - y , x * y , x / y , x.mod() , y.mod() ] ) , sep='\n' )
