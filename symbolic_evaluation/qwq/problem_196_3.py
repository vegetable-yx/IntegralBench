import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Divide by 96 to get the final result
result = pi_squared / 96

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))