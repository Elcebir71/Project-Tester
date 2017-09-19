class Difference:
    def __init__(self , a):
        self.__elements = a

    @property
    def computeDifference(self):
        self.maximumDifference = 0
        diff = [ ]
        comb = [ ]
        abs_max_dif = 0
        maximumDifference = 0
        for x , y in enumerate( a ):
            for j in range( x + 1 , len( a ) ):
                comb.append( [ y , a[ j ] ] )
        for i in comb:
            diff.append( abs( i[ 0 ] - i[ 1 ] ) )
            self.maximumDifference = max( diff )
        return self.maximumDifference


e = input()
a = [ int( e ) for e in input().split( ' ' ) ]
d = Difference( a )
d.computeDifference

print( d.maximumDifference )
