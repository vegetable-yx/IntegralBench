import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Assign the exact value directly
result = mp.mpf(1)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))