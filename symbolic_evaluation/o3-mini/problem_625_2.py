import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by pi
pi_times_sqrt2 = mp.pi * sqrt2

# Divide by 4 to get the final result
result = pi_times_sqrt2 / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))