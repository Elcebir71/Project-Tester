import re


def fun(f):
    return bool( re.search( r"^[-+]?\d*\.\d+$" , f ) )


if __name__ == '__main__':
    n = int( input() )
    flt = [ ]
    for _ in range( n ):
        flt.append( input() )

filtred = [ ]
for i in range( n ):
    filtred.append( fun( flt[ i ] ) )
    print( filtred[ i ] )
