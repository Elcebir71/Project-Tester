S = input()
fr = sorted( S ,
             key=lambda x: (x.isnumeric() , x.isnumeric() and int( x ) % 2 == 0 , not x.islower() , x.islower() , x) )
res = '%s' * len( fr ) % tuple( fr )
print( res )
