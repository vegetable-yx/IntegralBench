import mpmath as mp

# Set internal decimal places for calculations to 15
mp.dps = 15

# The analytical result is the constant 1
result = mp.mpf(1)

# Print the result to exactly 10 significant digits
print(mp.nstr(result, n=10))