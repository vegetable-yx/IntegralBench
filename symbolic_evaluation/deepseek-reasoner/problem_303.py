import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute the first integral term
term1 = mp.mpf(0.5)
term2 = (mp.mpf(15)/8) * mp.log(mp.mpf('2.5'))
term3 = (mp.mpf(15)/16) * mp.log(mp.mpf('15')/4)
integral1 = term1 - term2 + term3

# Compute the second integral using series expansion
def series_term(n):
    return 1 / (mp.power(2, 4*n + 2) * mp.power(2*n + 1, 2))

series_sum = mp.nsum(series_term, [0, mp.inf])

part1_second = (mp.pi/2) * mp.asin(mp.mpf('0.25'))
part2_second = 2 * series_sum
integral2 = part1_second - part2_second

# Combine all terms for final result
result = (mp.pi/16) * mp.asin(mp.mpf('0.25')) - (integral1/8) - (integral2/8)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))