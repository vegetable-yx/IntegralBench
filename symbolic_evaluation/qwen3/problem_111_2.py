import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π squared
pi_squared = mp.pi ** 2

# Compute the difference between π squared and 8
difference = pi_squared - 8

# Multiply by square root of 2
result = mp.sqrt(2) * difference

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))