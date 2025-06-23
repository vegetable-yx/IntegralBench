import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Assign the analytical result directly
result = mp.mpf(2)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))