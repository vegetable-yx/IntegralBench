import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute the natural logarithm of 4
ln4 = mp.log(4)

# Negate the result to get -ln(4)
result = -ln4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))