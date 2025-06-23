import mpmath as mp
mp.dps = 15

# Calculate the Bessel function of the first kind of order 1 at 1/2
x = mp.mpf('0.5')
j1_value = mp.besselj(1, x)

# Multiply by 2π to get the final result
result = 2 * mp.pi * j1_value

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))