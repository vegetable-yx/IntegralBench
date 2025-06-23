import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Assign the exact solution directly
result = mp.mpf(1)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))