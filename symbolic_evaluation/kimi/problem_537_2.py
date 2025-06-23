import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Assign the constant value 3 to the result
result = mp.mpf(3)

# Output the result with exactly 10 decimal places
print(mp.nstr(result, n=10))