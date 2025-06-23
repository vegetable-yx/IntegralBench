import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Assign the constant value -2 directly to the result variable
result = mp.mpf(-2)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))