from collections import deque, Counter
case = int( input() )
printout = [ ]
for i in range( case ):
    plist = [ ]
    N = int( input() )
    K = list( map( int,input().strip( " " ).split( " " ) ) )
    d = deque( K )
    while N > 0:
        values = [ d[ 0 ] , d[ N - 1 ] ]
        (mx , ind) = max( (v , h) for h , v in enumerate( values ) )
        if plist == [ ]:
            plist.append(values[ind])
            if ind == 0:
                d.popleft()
                N=len(d)
            else:
                d.pop()
                N=len(d)
        else:
            if ind == 0 and plist[-1] >= mx:
                plist.append( values[ ind ] )
                d.popleft()
                N=len(d)
            elif ind == 1 and plist[-1] >= mx:
                plist.append( values[ ind ] )
                d.pop()
                N = len( d )
            else:
                break
    if N == 0:
        printout.append( "Yes" )
    else:
        printout.append( "No" )
for m in range(case):
    print("%s"%(printout[m]))

