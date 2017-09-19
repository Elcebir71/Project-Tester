def digit_sum(n):
    n = abs( n )
    total = 0
    while n >= 1:
        total += (n % 10)
        n = n // 10
    return total


print( digit_sum( 10 ) )
