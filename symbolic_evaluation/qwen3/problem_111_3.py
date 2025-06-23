import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate the difference between π squared and 8
difference = pi_squared - 8

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply components to get final result
result = sqrt2 * difference

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))