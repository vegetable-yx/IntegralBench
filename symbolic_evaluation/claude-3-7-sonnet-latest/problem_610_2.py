import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# Assign the analytical result (constant value 1) to a variable
result = mp.mpf(1)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))