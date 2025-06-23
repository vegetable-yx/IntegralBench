import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute the Bessel function of the first kind of order 3 at 2.0
j3_value = mp.besselj(3, 2.0)

# Divide the result by 2.0
result = j3_value / 2.0

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))