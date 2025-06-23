import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Assign the analytical result (constant value 3) to a variable
result = mp.mpf(3)

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))