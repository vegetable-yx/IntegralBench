import mpmath as mp
mp.dps = 15

# Compute the Struve H function of order 0 at 1
h0 = mp.struveh(0, 1)

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply components together
result = sqrt2 * mp.pi * h0

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))