import mpmath as mp
mp.dps = 15

# Calculate Bessel function of the first kind J_3.0(2.0)
order = mp.mpf('3.0')
argument = mp.mpf('2.0')
result = mp.besselj(order, argument)

print(mp.nstr(result, n=10))