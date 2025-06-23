import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Assign the constant value 2 to the result variable
result = mp.mpf(2)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))