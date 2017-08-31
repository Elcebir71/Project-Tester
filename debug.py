import collections

N = int( input() )
d = collections.deque()
for i in range( N ):
    Input = input()
    if Input.__len__() == 3:
        if d.__len__() == 0:
            continue
        else:
            d.pop()
    elif Input.__len__() == 7:
        if d.__len__() == 0:
            continue
        else:
            d.popleft()
    else:
        comnd , item = Input[ :-2 ] , Input[ -1 ]
        if comnd == 'append':
            d.append( int( item ) )
        else:
            d.appendleft( int( item ) )
for i in range( d.__len__() ):
    print( d.__getitem__( i ) , sep=" " , end=" " )
