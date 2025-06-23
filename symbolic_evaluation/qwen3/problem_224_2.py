import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate 2π
term1 = mp.mpf(2) * mp.pi

# Calculate π squared divided by 2
pi_squared = mp.pi ** 2
term2 = pi_squared / 2

# Compute final result by subtracting terms
result = term1 - term2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))